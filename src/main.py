from fastapi import FastAPI, HTTPException

from typing import Union, List
from domain.episode import (
    Episode,
    PostEpisodeInput,
    PostEpisodeOutput,
    DeleteEpisodeOutput,
)

from .dependency import interactor

app = FastAPI()


@app.get("/")
def read_root():
    return "root"


@app.get("/episodes", status_code=200, response_model=List[Episode])
def get_episodes():
    return interactor.exescute_get_episodes()


@app.get("/episodes/{episode_id}", status_code=200, response_model=Episode)
def get_episode(episode_id: str):
    result = interactor.execute_get_episode(episode_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Episode not found")
    return result


@app.post("/episodes/", status_code=201, response_model=PostEpisodeOutput)
def post_episode(payload: PostEpisodeInput):
    payload = dict(payload)
    return interactor.execute_post_episode(payload)


@app.delete(
    "/episodes/{episode_id}", status_code=200, response_model=DeleteEpisodeOutput
)
def delete_episode(episode_id: str):
    return interactor.execute_del_episode(episode_id)
