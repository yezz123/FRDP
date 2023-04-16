from api.api import api_router as router
from core import tasks
from core.config import settings
from core.database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request


def get_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Boilerplate code for quick docker implementation of REST API with JWT Authentication using FastAPI, PostgreSQL and PgAdmin.",
        version="1.0.0",
        openapi_url=f"{settings.API}/openapi.json",
    )
    Base.metadata.create_all(bind=engine)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    return app


app = get_application()
app.include_router(router, prefix=settings.API)


@app.get("/health", response_model=str)
async def home(request: Request):
    return {"message": "Hello World"}
