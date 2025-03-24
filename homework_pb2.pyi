from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("token", "info", "error", "unknownTask", "adderTask", "matrixTask")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNTASK_FIELD_NUMBER: _ClassVar[int]
    ADDERTASK_FIELD_NUMBER: _ClassVar[int]
    MATRIXTASK_FIELD_NUMBER: _ClassVar[int]
    token: str
    info: str
    error: str
    unknownTask: UnknownTask
    adderTask: AdderTask
    matrixTask: MatrixTask
    def __init__(self, token: _Optional[str] = ..., info: _Optional[str] = ..., error: _Optional[str] = ..., unknownTask: _Optional[_Union[UnknownTask, _Mapping]] = ..., adderTask: _Optional[_Union[AdderTask, _Mapping]] = ..., matrixTask: _Optional[_Union[MatrixTask, _Mapping]] = ...) -> None: ...

class UnknownTask(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BeginData(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class AdderTask(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: float
    def __init__(self, a: _Optional[int] = ..., b: _Optional[float] = ...) -> None: ...

class AdderTaskResponse(_message.Message):
    __slots__ = ("token", "result")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    token: str
    result: float
    def __init__(self, token: _Optional[str] = ..., result: _Optional[float] = ...) -> None: ...

class MatrixTask(_message.Message):
    __slots__ = ("rows",)
    class Row(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[MatrixTask.Row]
    def __init__(self, rows: _Optional[_Iterable[_Union[MatrixTask.Row, _Mapping]]] = ...) -> None: ...

class MatrixTaskResponse(_message.Message):
    __slots__ = ("token", "determinant")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DETERMINANT_FIELD_NUMBER: _ClassVar[int]
    token: str
    determinant: int
    def __init__(self, token: _Optional[str] = ..., determinant: _Optional[int] = ...) -> None: ...

class FlipLineRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class FlipLineResponse(_message.Message):
    __slots__ = ("token", "point")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    token: str
    point: Point
    def __init__(self, token: _Optional[str] = ..., point: _Optional[_Union[Point, _Mapping]] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class Homework(_service.service): ...

class Homework_Stub(Homework): ...
