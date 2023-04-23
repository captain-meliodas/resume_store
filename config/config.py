#!/usr/bin/python3
# coding= utf-8
""" config file """
import base64
import json
from pydantic import BaseSettings

class Settings(BaseSettings):
    base_path: str = ""
    cors_origins: str = "http://localhost,http://localhost:3000"
    ssl_cert: str = ""
    ssl_key: str = ""
    bind_ip: str = "0.0.0.0"
    port: int = 8000
    db_name: str = "resume_store"

    @classmethod
    def get_settings(cls):
        """ Get the setting values from config"""
        return Settings()