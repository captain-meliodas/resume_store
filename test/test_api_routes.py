# !/usr/bin/python3
# coding= utf-8
"""
This code provides testing over fastapi
"""

import pytest
import requests_mock
from fastapi.testclient import TestClient
from pymongo import MongoClient

from config.config import Settings
settings = Settings.get_settings()

from app import main_app
#creating a testclient from the fast api application
app = TestClient(main_app())


class TestMyApplication:
    """
    Unit Test cases for the application 
    """

    @pytest.fixture(scope="module")
    def db_client_conn(self):
        # connecting to mongo with your testing credentials
        #This mongo will be created on the fly with the CI pipelines and will be deleted after that
        db_client = MongoClient(
            host="localhost",
            port=27017
        )

        # Creating an app for testclient
        # storing the db_connection and app
        yield db_client

        db = db_client[settings.db_name] if db_client else None
        if db is None:
            print(f"Unable to connect to mongo db '0.0.0.0' 27017 {settings.ingests_db}")
            return
        
        #before closing db connection remove all data created in the mongo
        #Todo: cleanup from the db
        
        # Close connections after successful running of all test cases
        db_client.close()

    @pytest.fixture
    def get_tokens(self):
        """
        This method returns config file
        """
        #create tokens for testing purpose if applicable this fixture then can be used with each test to get the tokens 
        tokens = {"test_token_1":"asdasdsadasd","test_token_2": "adssadwqdadacza"}
        return tokens 

    def test_home_page(self,get_tokens, db_client_conn):
        """
        This method tests root
        db_client_conn: it is the db connection client uses to interact with db
        """
        headers = {"Authorization": f"Bearer {get_tokens.get('test_token_1')}", "Content-Type": "application/json"}
        
        with requests_mock.Mocker(real_http=True) as m:
            #mocking the external request
            m.get(f"https://www.google.com/",status_code=200)

            response = app.get("/", headers=headers)
        
        expected_data = {"message": "The API is up and running"}

        #asserting the response status and data
        assert response.status_code == 200
        assert response.json() == expected_data