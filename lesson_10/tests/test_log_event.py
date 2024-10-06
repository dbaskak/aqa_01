from aqa_01.lesson_10.homework_10 import log_event
from aqa_01.lesson_10.src.logger_util import setup_logger


# 'log_event' test suite

def test_log_success():
    log_file = 'test_log.log'
    setup_logger(log_file)

    log_event("user1", "success")

    with open(log_file, 'r') as file:
        log_content = file.read()

    assert "Login event - Username: user1, Status: success" in log_content


def test_log_expired():
    log_file = 'test_log.log'
    setup_logger(log_file)

    log_event("user2", "expired")

    with open(log_file, 'r') as file:
        log_content = file.read()

    assert "Login event - Username: user2, Status: expired" in log_content


def test_log_failed():
    log_file = 'test_log.log'
    setup_logger(log_file)

    log_event("user3", "failed")

    with open(log_file, 'r') as file:
        log_content = file.read()

    assert "Login event - Username: user3, Status: failed" in log_content


def test_log_unknown_status():
    log_file = 'test_log.log'
    setup_logger(log_file)

    log_event("user4", "unknown")

    with open(log_file, 'r') as file:
        log_content = file.read()

    assert "Login event - Username: user4, Status: unknown" in log_content
