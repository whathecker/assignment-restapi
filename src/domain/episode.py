""" 
This module contains the Pydantic models that define the core data structure (input, output, core models).
"""
from uuid import UUID
from typing import List
from typing_extensions import TypedDict, Literal  # TO support new type constructs
from pydantic import BaseModel


class PersonInput(TypedDict):
    name: str


class PostEpisodeInput(BaseModel):
    episodeTitle: str
    podcastTitle: str
    thumbnailUrl: str
    guests: List[PersonInput]
    audioUrl: str
    episodeDurationSeconds: int


class PostEpisodeOutput(BaseModel):
    resourceUrl: str


class DeleteEpisodeOutput(BaseModel):
    result: Literal["Success", "Fail"]


class Person(BaseModel):
    name: str


class Episode(BaseModel):
    id: UUID  # uuid version 4
    episodeTitle: str
    podcastTitle: str
    thumbnailUrl: str
    guests: List[Person]
    audioUrl: str
    episodeDurationSeconds: int
