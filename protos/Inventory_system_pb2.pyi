import Book_pb2 as _Book_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
available: Status
taken: Status

class InventoryItem(_message.Message):
    __slots__ = ["Inventory_number", "book_object", "status"]
    BOOK_OBJECT_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    Inventory_number: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book_object: _Book_pb2.Book
    status: Status
    def __init__(self, Inventory_number: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., book_object: _Optional[_Union[_Book_pb2.Book, _Mapping]] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
