from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field, root_validator


class Point(BaseModel):
    """
    A point in 3D space at a particular time
    """

    x: Optional[float] = Field(None, description="The X-coordinate of the point")
    y: Optional[float] = Field(None, description="The Y-coordinate of the point")
    z: Optional[float] = Field(None, description="The Z-coordinate of the point")


class VirtualMarkerDefinition(BaseModel):
    """
    A virtual marker, defined by combining multiple markers with weights to generate a new marker/point
    """
    marker_names: List[str] = Field(
        default_factory=list, description="The names of the markers that define this virtual marker"
    )
    marker_weights: List[float] = Field(
        default_factory=list, description="The weights of the markers that define this virtual marker, must sum to 1"
    )

    @root_validator
    def check_weights(cls, values):
        marker_weights = values.get("marker_weights")
        if sum(marker_weights) != 1:
            raise ValueError(f"Marker weights must sum to 1, got {marker_weights}")
        return values

class SegmentLength(BaseModel):
    body_height: Optional[float] = Field(None, description="The length of the segment in units of body height. Estimated based on Anthropometry tables in Winter (2009)")
    measured_length: Optional[float] = Field(None, description="The length of the segment in units of milimeters. Measured from the recorded data")

class SegmentSchema(BaseModel):
    """
    A schema for a segment of a skeleton, defined by a set of tracked points and connections between them
    """
    name: str = Field(description="The name of the segment")
    origin: Optional[str] = Field(None, description="The origin of the segment")
    center: Optional[Union[VirtualMarkerDefinition, str]] = Field(None, description="The center of the segment")
    pole: Optional[str] = Field(None, description="The pole of the segment, i.e. the part that points/lies on local +Y")
    length: Optional[SegmentLength] = Field(None, description="The length of the segment (from origin to pole)")
    point_names: List[str] = Field(
        default_factory=list, description="The names of the tracked points that define this segment"
    )
    virtual_marker_definitions: Optional[Dict[str, VirtualMarkerDefinition]] = Field(
        default_factory=dict, description="The virtual markers that define this segment (if any)"
    )
    connections: List[Tuple[str, str]] = Field(
        default_factory=list, description="The connections between the tracked points"
    )

    parent: Optional[str] = Field(None, description="The name of the parent of this segment")


class SkeletonSchema(BaseModel):
    body: SegmentSchema = Field(default_factory=SegmentSchema, description="The tracked points that define the body")
    hands: Dict[str, SegmentSchema] = Field(
        default_factory=dict, description="The tracked points that define the hands: keys - (left, right)"
    )
    face: SegmentSchema = Field(default_factory=SegmentSchema, description="The tracked points that define the face")

    def __init__(self, schema_dict: Dict[str, Dict[str, Any]]):
        super().__init__()
        self.body = SegmentSchema(**schema_dict["body"])
        self.hands = {hand: SegmentSchema(**hand_schema) for hand, hand_schema in schema_dict["hands"].items()}
        self.face = SegmentSchema(**schema_dict["face"])

    def dict(self):
        d = {}
        d["body"] = self.body.dict()
        d["hands"] = {hand: hand_schema.dict() for hand, hand_schema in self.hands.items()}
        d["face"] = self.face.dict()
        return d


class HierarchySegment(SegmentSchema):
    children: Dict[str, SegmentSchema] = Field(default_factory=dict, description="The children of this segment")

    def __init__(self, name: str, children=None, *args, **kwargs):
        super().__init__(name=name, *args, **kwargs)
        if children is None:
            children = {}
        self.children = children


class SkeletonBody(BaseModel):
    """
    A model for a body, defining the hierarchical structure of segments
    """
    Root: HierarchySegment

