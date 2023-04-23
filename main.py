""" main module - entry point for api """

import uvicorn
from fastapi.responses import FileResponse
from app import main_app

from config.config import Settings
settings = Settings.get_settings()

def main():
    """
    This function creates fastapi object,
    loads settings, adds api routers and certificate configuration
    """
    settings = Settings.get_settings()
    app = main_app()

    @app.exception_handler(404)
    async def custom_404_handler(request, __):
        return FileResponse('index.html')

    if settings.ssl_cert and settings.ssl_key:
        uvicorn.run(app, host=settings.bind_ip, port=settings.port,
                    ssl_keyfile=settings.ssl_key, ssl_certfile=settings.ssl_cert)
    else:
        uvicorn.run(app, host=settings.bind_ip, port=settings.port)


if __name__ == "__main__":
    main()
