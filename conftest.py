import pytest
from main import BooksCollector

@pytest.fixture()
def set_collector():
    collector = BooksCollector()
    return collector