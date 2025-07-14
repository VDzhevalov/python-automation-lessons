import os
from log_event_module import LOG_FILE
import pytest

@pytest.fixture()
def read_log_file():
    assert os.path.exists(LOG_FILE), "Файл логування не створено"
    with open(os.path.join(os.path.dirname(__file__),LOG_FILE), "r", encoding="utf-8") as f:
        yield f

def test_log_success(read_log_file):
    content = read_log_file.read()
    assert "INFO" in content
    assert "Username: alice, Status: success" in content

def test_log_expired(read_log_file):
    content = read_log_file.read()
    assert "WARNING" in content
    assert "Username: bob, Status: expired" in content

def test_log_failed(read_log_file):
    content = read_log_file.read()
    assert "ERROR" in content
    assert "Username: carol, Status: failed" in content

def test_log_unknown(read_log_file):
    content = read_log_file.read()
    assert "ERROR" in content
    assert "Username: dave, Status: invalid" in content

def test_for_admin(read_log_file):
    content = read_log_file.read()
    assert "ERROR" in content
    assert "INFO" in content
    assert "Username: admin, Status: unknown" in content