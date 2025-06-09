from enum import Enum

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

class ProjectName(str, Enum):
    cameras = "cameras"
    beambreak = "beambreak"
    decibel = "decibel"


app = FastAPI()

@app.get("/project", response_class=HTMLResponse)
async def items_index(request: Request):
    beambreak_url = request.url_for("get_project", project_name="beambreak")
    cameras_url = request.url_for("get_project", project_name="cameras")
    decibel_url = request.url_for("get_project", project_name="decibel")
    return f"""
        <h1>Items Index</h1>
        <ul>
            <li><a href="{beambreak_url}">Beam Break</a></li>
            <li><a href="{cameras_url}">Cameras</a></li>
            <li><a href="{decibel_url}">Decibel</a></li>
        </ul>
    """

@app.get("/project/{project_name}")
async def get_project(project_name: ProjectName):
    if project_name == ProjectName.cameras:
        return {"project_name": project_name, "message": "Too Intrusive"}

    if project_name == ProjectName.beambreak:
        return {"project_name": project_name, "message": "Very Low Range and hard to interpret"}

    if project_name == ProjectName.decibel:
        return {"project_name": project_name, "message": "Seems Perfect!"}
