import pathlib
from dataclasses import dataclass, is_dataclass, fields
from typing import Any, List, Type, Optional

from xsdata.formats.dataclass.parsers import XmlParser

from mtconnect.schema import mtconnect_stream_schema_1_7
from mtconnect.schema.mtconnect_stream_schema_1_7.mtconnect_streams_1_7 import (
    ComponentStreamType,
    EventsType,
    MtconnectStreams,
)


def find_dataclasses(
    dataclass_instance: Any,
    target_type: Optional[Type] = None,
    attribute_name: Optional[str] = None,
    attribute_value: Optional[Any] = None,
    max_depth: int = 10,
    current_depth: int = 0,
) -> List[Any]:
    """
    Recursively search through a dataclass and its children to find dataclass instances
    that match the given criteria.

    The function can match by:
    - Dataclass type (`target_type`)
    - Dataclass field name (`attribute_name`)
    - Dataclass field value (`attribute_value`)

    If `target_type`, `attribute_name`, and `attribute_value` are all provided, only dataclasses
    matching all those conditions are returned.

    Parameters:
    - dataclass_instance (Any): The root dataclass instance to search through.
    - target_type (Optional[Type]): The type of dataclass to search for. Default is None.
    - attribute_name (Optional[str]): The field name to search for. Default is None.
    - attribute_value (Optional[Any]): The field value to search for. Default is None.
    - max_depth (int): The maximum recursion depth. Default is 10.
    - current_depth (int): The current recursion depth. Internal use only.

    Returns:
    - List[Any]: A list of matching dataclass instances.

    Raises:
    - ValueError: If none of `target_type`, `attribute_name`, or `attribute_value` is provided.
    """

    # Ensure at least one of target_type, attribute_name, or attribute_value is provided
    if target_type is None and attribute_name is None and attribute_value is None:
        raise ValueError("At least one of target_type, attribute_name, or attribute_value must be provided.")

    # Ensure the instance is a dataclass and we haven't exceeded the max depth
    if not is_dataclass(dataclass_instance) or current_depth > max_depth:
        return []

    matching_instances = []

    # Check if the dataclass matches all provided conditions
    type_matches = target_type is None or isinstance(dataclass_instance, target_type)
    field_name_matches = True  # Default to True if attribute_name is not provided
    field_value_matches = True  # Default to True if attribute_value is not provided

    for field in fields(dataclass_instance):
        field_value = getattr(dataclass_instance, field.name)

        # If attribute_name is provided, check if the dataclass has a field with this name
        if attribute_name is not None:
            if field.name == attribute_name:
                field_name_matches = True
                if attribute_value is not None:
                    # If attribute_value is provided, check if the field value matches
                    field_value_matches = field_value == attribute_value
                else:
                    field_value_matches = True
                # If field_name matches, no need to continue checking other fields for this condition
                break
            else:
                field_name_matches = False

        # If attribute_value is provided but attribute_name is not, check all fields for matching value
        if attribute_name is None and attribute_value is not None:
            if field_value == attribute_value:
                field_value_matches = True
                break
            else:
                field_value_matches = False

        # If the field itself is a dataclass, search within it recursively
        #TODO: This is broken
        if not is_dataclass(field_value):
            continue
        elif isinstance(field_value, list):
            if not is_dataclass(field_value[0]):
                break
            else: 
                continue
        
        matching_instances.extend(
            find_dataclasses(
                field_value,
                target_type,
                attribute_name,
                attribute_value,
                max_depth,
                current_depth + 1,
            )
        )

    # Add the dataclass instance if all conditions are satisfied
    if type_matches and field_name_matches and field_value_matches:
        matching_instances.append(dataclass_instance)

    return matching_instances


class MTStream:
    """
    Class to handle MT data streams
    Call method "update_tree" to parse an XML file.
    """

    MTstream_parser = XmlParser()
    parser_class = MtconnectStreams

    def __init__(self):
        pass

    def update_tree(self, xml_string_or_filepath: str | pathlib.Path):
        """
        Parse an XML file. Takes a string, filepath string, or pathlib.path object and creates self.root
        """
        self.xml = xml_string_or_filepath
        self.root = self.MTstream_parser.parse(self.xml, self.parser_class)
        self.component_stream: list[ComponentStreamType] = self.root.streams.device_stream[1].component_stream

    def find_component_by_component_attribute(self, component_attribute_string: str):
        results = [x for x in self.component_stream if x.component == component_attribute_string]
        if len(results) == 0:
            raise IndexError(f"No components with attribute {component_attribute_string} found")
        elif len(results) > 1:
            raise IndexError(f"Multiple results returned for component attribute search {component_attribute_string}")
        else:
            return results[0]

    def return_events(self) -> EventsType | None:
        pathobj = self.find_component_by_component_attribute("Path")
        return pathobj.events

    def find_type_in_root(self, target_type: Type):
        return find_dataclasses(dataclass_instance=self.root, target_type=target_type)

    def find_type_in_component_stream(self, target_type: Type):
        return find_dataclasses(dataclass_instance=self.component_stream, target_type=target_type)

    def find_type_in_events(self, target_type: Type):
        return find_dataclasses(dataclass_instance=self.return_events(), target_type=target_type)
