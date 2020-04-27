"""
typing stub file
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, List, Optional, Union

import opcua
from opcua.client.ua_client import UaClient
from opcua.server.internal_server import InternalSession
from opcua.ua.object_ids import ObjectIds
from opcua.ua.uaprotocol_auto import ReferenceDescription, NodeClass, BrowseDirection
from opcua.ua.uatypes import DataValue, LocalizedText, NodeId, QualifiedName

class Node:
    def __init__(
        self,
        server: Union[InternalSession, UaClient],
        nodeid: Union[Node, NodeId, str, bytes, int],
    ) -> None:
        self.nodeid: NodeId
        self.server: Union[InternalSession, UaClient]
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def get_browse_name(self) -> QualifiedName: ...
    def get_display_name(self) -> LocalizedText: ...
    def get_data_type(self) -> NodeId: ...
    def get_node_class(self) -> NodeClass: ...
    def get_description(self) -> LocalizedText: ...
    def get_value(self) -> Any: ...
    def get_data_value(self) -> DataValue: ...
    def call_method(self, methodid: NodeId, *args) -> Any: ...
    def get_children(
        self, refs: ObjectIds = ..., nodeclassmask: NodeClass = ...
    ) -> List[opcua.Node]: ...
    def get_references(
        self,
        refs: ObjectIds = ...,
        nodeclassmask: NodeClass = ...,
        includesubtypes: bool = ...,
    ) -> List[ReferenceDescription]: ...
    def get_referenced_nodes(
        self,
        refs: ObjectIds = ...,
        direction: BrowseDirection = ...,
        nodeclassmask: NodeClass = ...,
        includesubtypes: bool = True,
    ) -> List[opcua.Node]: ...
    def read_raw_history(
        self,
        starttime: Optional[datetime] = ...,
        endtime: Optional[datetime] = ...,
        numvalues: int = ...,
    ) -> List[DataValue]: ...
    def get_children_descriptions(
        self,
        refs: ObjectIds = ...,
        nodeclassmask: NodeClass = ...,
        includesubtypes: bool = ...,
    ) -> List[ReferenceDescription]: ...
