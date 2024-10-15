from mtconnect.schema import mtconnect_stream_schema_1_7
from xsdata.formats.dataclass.parsers import XmlParser
from mtconnect.schema.mtconnect_stream_schema_1_7.mtconnect_streams_1_7 import MtconnectStreams, EventsType


class MTStream:
    MTstream_parser = XmlParser()

    def __init__(self, xml_filepath):
        self.xml_filepath = xml_filepath
        self.update_tree()
        self.component_stream = self.root.streams.device_stream[1].component_stream

    def update_tree(self):
        self.root = self.MTstream_parser.parse(self.xml_filepath, MtconnectStreams)

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


if __name__ == "__main__":
    fp = "test/test_data/current.xml"
    test: MTStream = MTStream(fp)
    test.return_events()
    print(test)

