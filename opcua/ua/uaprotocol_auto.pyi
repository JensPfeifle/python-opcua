"""
typing stub file
"""

from enum import IntEnum
from opcua.ua import uatypes
from typing import List, Any

class NodeClass(IntEnum):
    Unspecified: int = ...
    Object: int = ...
    Variable: int = ...
    Method: int = ...
    ObjectType: int = ...
    VariableType: int = ...
    ReferenceType: int = ...
    DataType: int = ...
    View: int = ...

class BrowseDirection(IntEnum):
    Forward: int = ...
    Inverse: int = ...
    Both: int = ...
    Invalid: int = ...

class CallMethodRequest:
    def __init__(self) -> None:
        self.ObjectId: uatypes.NodeId
        self.MethodId: uatypes.NodeId
        self.InputArguments: List[Any]

class EUInformation:
    def __init__(self) -> None:
        self.NamespaceUri: str
        self.UnitId: int
        self.DisplayName: uatypes.LocalizedText
        self.Description: uatypes.LocalizedText

class WriteValue:
    def __init__(self):
        self.NodeId: uatypes.NodeId
        self.AttributeId: int
        self.IndexRange: Any
        self.Value: uatypes.DataValue

class WriteParameters:
    def __init__(self) -> None:
        self.NodesToWrite: List[Any]

class TimeZoneDataType:
    def __init__(self) -> None:
        self.Offset: int
        self.DaylightSavingInOffset: bool

class Range:
    def __init__(self):
        self.Low: float
        self.High: float

class ReferenceDescription:
    def __init__(self) -> None:
        self.ReferenceTypeId: uatypes.NodeId
        self.IsForward: bool
        self.NodeId: uatypes.ExpandedNodeId
        self.BrowseName: uatypes.QualifiedName
        self.DisplayName: uatypes.LocalizedText
        self.NodeClass: NodeClass
        self.TypeDefinition: uatypes.ExpandedNodeId

class EnumValueType:
    def __init__(self) -> None:
        self.Value: int
        self.DisplayName: uatypes.LocalizedText
        self.Description: uatypes.LocalizedText
