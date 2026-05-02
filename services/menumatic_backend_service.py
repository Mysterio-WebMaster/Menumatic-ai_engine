import requests
from flask import current_app


class MenumaticBackendService:
    def __init__(self):
        self.base_url = "http://localhost:5000"
        self.timeout = 15

    def getAllMenu(self):
        try:
            response = requests.get(
                f"{self.base_url}/engine/menu", timeout=self.timeout
            )
            response.raise_for_status()
            # print(response.json())
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Logging Backend Error: {e}")
            # Re-raise so the controller's 'except' block catches it
            raise Exception("Could not connect to the Spring Boot backend.")
