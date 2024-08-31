from dataclasses import dataclass
from typing import Optional, List


@dataclass
class MediaItemDTO:
    """Data Transfer Object for a Media Item."""

    title: str
    source: str
    resolution: Optional[str] = None
    format: Optional[str] = None
    size: Optional[str] = None
    rate: Optional[str] = None
    fps: Optional[str] = None


MediaItems = List[MediaItemDTO]
