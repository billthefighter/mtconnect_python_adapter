import pathlib
from dataclasses import dataclass, is_dataclass, fields
from typing import Any, List, Type

from xsdata.formats.dataclass.parsers import XmlParser

from mtconnect.schema import mtconnect_stream_schema_1_7
from mtconnect.schema.mtconnect_stream_schema_1_7.mtconnect_streams_1_7 import (
    ComponentStreamType,
    EventsType,
    MtconnectStreams,
)


def get_dataclasses_with_attribute(
    dataclass_instance: Any, attribute_name: str, max_depth: int = 10, current_depth: int = 0
) -> List[Any]:
    # Ensure the instance is a dataclass and the current depth is within the recursion limit
    if current_depth > max_depth:
        raise RecursionError(f"Data structure is too deep, max depth exceeds {max_depth} levels")
    if not is_dataclass(dataclass_instance):
        return []

    matched_dataclasses = []

    # Iterate through each field in the dataclass
    for field in fields(dataclass_instance):
        # Get the field value from the dataclass instance
        field_value = getattr(dataclass_instance, field.name)

        # Check if the field has the desired attribute in its metadata
        if attribute_name in field.metadata:
            matched_dataclasses.append(dataclass_instance)
            break

        # If the field itself is a dataclass, recursively check it
        if is_dataclass(field_value):
            matched_dataclasses.extend(
                get_dataclasses_with_attribute(
                    field_value,
                    attribute_name,
                    max_depth,
                    current_depth + 1,
                )
            )

    return matched_dataclasses


def find_all_dataclasses_of_type(
    dataclass_instance: Any, target_type: Type, max_depth: int = 10, current_depth: int = 0
) -> List[Any]:
    # Ensure the instance is a dataclass and the current depth is within the recursion limit
    if current_depth > max_depth:
        raise RecursionError(f"Data structure is too deep, max depth exceeds {max_depth} levels")

    matching_instances = []

    # Check if the current dataclass instance is of the target type
    if isinstance(dataclass_instance, target_type):
        matching_instances.append(dataclass_instance)

    # Recursively check all fields for nested dataclasses
    for field in fields(dataclass_instance):
        field_value = getattr(dataclass_instance, field.name)

        # If the field value is a dataclass, search within it
        if is_dataclass(field_value):
            matching_instances.extend(
                find_all_dataclasses_of_type(
                    field_value,
                    target_type,
                    max_depth,
                    current_depth + 1,
                )
            )

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
        return find_all_dataclasses_of_type(self.root, target_type)

    def find_type_in_component_stream(self, target_type: Type):
        return find_all_dataclasses_of_type(self.component_stream, target_type)

    def find_type_in_events(self, target_type: Type):
        return find_all_dataclasses_of_type(self.return_events(), target_type)
