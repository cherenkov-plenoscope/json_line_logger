import json_line_logger
import json_utils
import io


def test_log_to_stream():
    stream = io.StringIO()

    logger = json_line_logger.LoggerStream(stream=stream)
    logger.debug("1")
    logger.info("2")
    logger.critical("3")

    stream.seek(0)

    logs = []
    with json_utils.lines.Reader(file=stream) as rrr:
        for obj in rrr:
            logs.append(obj)

    assert len(logs) == 3
    assert logs[0]["l"] == "DEBUG"
    assert logs[0]["m"] == "1"

    assert logs[1]["l"] == "INFO"
    assert logs[1]["m"] == "2"
    assert logs[1]["t"] >= logs[0]["t"]

    assert logs[2]["l"] == "CRITICAL"
    assert logs[2]["m"] == "3"
    assert logs[2]["t"] >= logs[1]["t"]
