from mtconnect.schema import mtconnect_stream_schema_1_7
from xsdata.formats.dataclass.parsers import XmlParser
from mtconnect.schema.mtconnect_stream_schema_1_7.mtconnect_streams_1_7 import MtconnectStreams, EventsType
from mtconnect.mtstream import MTStream


if __name__ == "__main__":
    fp = "tests/test_data/current.xml"
    test: MTStream = MTStream()
    test.update_tree(fp)
    test.component_stream
    events = test.return_events()
    print(test)
