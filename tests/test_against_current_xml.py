from mtconnect.mtstream import find_dataclasses, MTStream
from mtconnect.schema.mtconnect_stream_schema_1_7.mtconnect_streams_1_7 import (
    ComponentStreamType,
    EventsType,
    MtconnectStreams,
    Program,
)
import pytest


@pytest.fixture
def MTStream_fixture():
    stream = MTStream()
    data_path = "tests/test_data/current.xml"
    stream.update_tree(data_path)
    return stream


def test_find_program_block(MTStream_fixture: MTStream):
    events = MTStream_fixture.return_events()
    result = find_dataclasses(dataclass_instance=events, target_type=Program)
    assert len(result) == 1
    assert isinstance(result[0], Child)
    assert result[0].name == "John"
