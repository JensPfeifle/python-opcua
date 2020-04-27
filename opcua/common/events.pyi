"""
typing stub file
"""

from typing import List, Any, Dict
from opcua.ua.object_ids import ObjectIds
from opcua.ua.uatypes import Variant

class Event:
    def __init__(self, emitting_node: ObjectIds = ObjectIds.Server) -> None:
        self.server_handle: Any
        self.select_clauses: Any
        self.event_fields: Any
        self.data_types: Dict[Any, Any]
        self.emitting_node: ObjectIds
        self.internal_properties: List[str]
    def get_event_props_as_fields_dict(self) -> Dict[str, Variant]: ...
