import pathlib

from xsdata.formats.dataclass.parsers import XmlParser

from mtconnect.schema import mtconnect_stream_schema_1_7
from mtconnect.schema.mtconnect_stream_schema_1_7.mtconnect_streams_1_7 import (
    ComponentStreamType,
    EventsType,
    MtconnectStreams,
)


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
