from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from core import tasks

from api.api import api_router

from db.base_class import Base
from db.session import engine

from core.config import settings

templates = Jinja2Templates(directory="templates")


def get_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=
        "Boilerplate code for quick docker implementation of REST API with JWT Authentication using FastAPI, PostgreSQL and PgAdmin.",
        version="1.0.0",
        openapi_url=f"{settings.API}/openapi.json")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    Base.metadata.create_all(bind=engine)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    return app


app = get_application()
app.include_router(api_router, prefix=settings.API)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
