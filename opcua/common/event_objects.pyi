"""
Typing stub file
"""

import datetime
from typing import Any, Optional

from opcua.common.events import Event
from opcua.ua.object_ids import ObjectIds
from opcua.ua.uaprotocol_auto import TimeZoneDataType
from opcua.ua.uatypes import LocalizedText, NodeId, Variant

class BaseEvent(Event):
    def __init__(
        self,
        sourcenode: NodeId = None,
        message: Any = None,
        severity: int = 1,
        emitting_node: ObjectIds = ObjectIds.Server,
    ) -> None:
        self.EventId: Optional[bytes]
        self.EventType: NodeId
        self.SourceNode: Optional[NodeId]
        self.SourceName: Optional[str]
        self.Time: Optional[datetime.datetime]
        self.ReceiveTime: Optional[datetime.datetime]
        self.LocalTime: TimeZoneDataType
        self.Message: LocalizedText
        self.Severity: int

class AuditEvent(BaseEvent):
    def __init__(
        self,
        sourcenode: NodeId = None,
        message: Any = None,
        severity: int = 1,
        emitting_node: ObjectIds = ObjectIds.Server,
    ) -> None:
        self.EventType: NodeId
        self.ActionTimeStamp: datetime.datetime
        self.Status: bool
        self.ServerId: Optional[str]
        self.ClientAuditEntryId: Optional[str]
        self.ClientUserId: Optional[str]

class BaseModelChangeEvent(BaseEvent): ...
