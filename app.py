#core modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging
import os

#routers
from routers import home

from config.config import Settings
settings = Settings.get_settings()

def main_app():
    # settings = Settings.get_settings()
    origins = settings.cors_origins.split(",") if settings.cors_origins else []
    app = FastAPI(root_path=settings.base_path)
    

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    #include the routes
    app.include_router(home.router)

    if os.path.exists("api/ui"):
        app.mount("/ui", StaticFiles(directory="api/ui"), name="ui")
    else:
        logging.error("UI folder 'ui' unavailable. Hosting only API..")

    if os.path.exists("api/static"):
        app.mount("/static", StaticFiles(directory="api/static"), name="static")
    else:
        logging.error("UI folder 'static' unavailable. Hosting only API..")

    return app
