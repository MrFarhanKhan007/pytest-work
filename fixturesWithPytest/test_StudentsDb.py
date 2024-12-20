import pytest
from StudentDb import StudentDb


@pytest.fixture(scope="module")
def db():
    db = StudentDb()
    db.connect("C:/Users/hoffm/OneDrive/Desktop/pytest/data.json")
    yield db # yield because -> so that db.close() gets called in the end and act
             # as a teardown method
    db.close()


def test_scott_data(db):
    scott_data = db.get_data("Scott")
    assert scott_data["id"] == 1
    assert scott_data["name"] == "Scott"
    assert scott_data["result"] == "pass"


def test_mark_data(db):
    mark_data = db.get_data("Mark")
    assert mark_data["id"] == 2
    assert mark_data["name"] == "Mark"
    assert mark_data["result"] == "fail"
