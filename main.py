from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CityStateMap.settings")
django.setup()
from CityStateMap.urls import api_router

from django.apps import apps
from CityStateMap import settings as state_settings
from django.conf import settings

try:
    settings.configure(state_settings)
except RuntimeError:  # Avoid: 'Settings already configured.'
    pass

apps.populate(settings.INSTALLED_APPS)

app = FastAPI(title="CityStateMapping")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
