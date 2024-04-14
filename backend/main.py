import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import router as app_router


def get_application() -> FastAPI:
    project_name = "Hackathon_2024"
    version = "0.0.1"
    application = FastAPI(
        title=project_name,
        version=version,
    )
    application.include_router(app_router)
    return application


app = get_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)
