from fastapi import FastAPI
from dotenv import load_dotenv


# Load the .env file
load_dotenv(".env")

app = FastAPI()
