from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FICTION: GENRE
HORROR: GENRE
ROMANTIC: GENRE
THRILLER: GENRE
available: Status
taken: Status

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishing_year", "rating", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: GENRE
    isbn: str
    publishing_year: int
    rating: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., rating: _Optional[int] = ..., publishing_year: _Optional[int] = ..., genre: _Optional[_Union[GENRE, str]] = ...) -> None: ...

class ISBN(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["Inventory_number", "book_object", "status"]
    BOOK_OBJECT_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    Inventory_number: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book_object: Book
    status: Status
    def __init__(self, Inventory_number: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., book_object: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class GENRE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
