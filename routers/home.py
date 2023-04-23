#!/usr/bin/python3
# coding= utf-8
""" home module """
from fastapi import APIRouter
import requests

router = APIRouter(
    prefix="",
    tags=["home"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_index():
    """
    Root route for API
    """

    #calling for external services to do some task
    requests.get("https://www.google.com/")

    #TODO: do your work and calculations here and return the response
    response = {"message":"The API is up and running"}
    
    return response
