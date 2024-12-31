from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import auth_routes, image_routes, report_routes, contact_routes

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(image_routes.router, prefix="/images", tags=["Images"])
app.include_router(report_routes.router, prefix="/reports", tags=["Reports"])
app.include_router(contact_routes.router, prefix="/contact", tags=["Contact"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Crop Disease Prediction System!"}

@app.get("/about")
def about():
    return {
        "message": "About the Crop Disease Prediction System. A platform to monitor and predict crop diseases using AI and data-driven insights."
    }
