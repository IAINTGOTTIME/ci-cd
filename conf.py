import os

from dotenv import load_dotenv

load_dotenv(".env")


class UserData:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")


class Links:
    HOST = "https://opensource-demo.orangehrmlive.com/web/index.php"
    LOGIN_LINK = f"{HOST}/auth/login"
    DASHBOARD = f"{HOST}/dashboard/index"
