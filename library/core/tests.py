import pytest
from model_bakery import baker

from .models import Book


@pytest.fixture
def book(db):
    return baker.make("core.Book")


def test_book_has_been_created(book):
    """Count Books must be 1."""
    assert Book.objects.count() == 1


def test_book_has_fields_from_abstract_model(book):
    """Book should inherit fields from the abstract model."""
    assert hasattr(book, "uuid")
    assert hasattr(book, "created_at")
    assert hasattr(book, "updated_at")
