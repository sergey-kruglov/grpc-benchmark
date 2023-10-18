from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindRequest(_message.Message):
    __slots__ = ["search"]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    search: str
    def __init__(self, search: _Optional[str] = ...) -> None: ...

class FindReply(_message.Message):
    __slots__ = ["orders"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderData]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderData, _Mapping]]] = ...) -> None: ...

class OrderData(_message.Message):
    __slots__ = ["mongo_id", "id", "otn", "tracking_number"]
    MONGO_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OTN_FIELD_NUMBER: _ClassVar[int]
    TRACKING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    mongo_id: str
    id: str
    otn: str
    tracking_number: str
    def __init__(self, mongo_id: _Optional[str] = ..., id: _Optional[str] = ..., otn: _Optional[str] = ..., tracking_number: _Optional[str] = ...) -> None: ...
