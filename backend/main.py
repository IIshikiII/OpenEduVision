from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OpenEduVision API",
    description="Backend for AI-powered educational analytics",
    version="0.1.0",
)

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "OpenEduVision API is running!"}

# Placeholders for additional routers (courses, analytics, students)
# from app.api import courses, analytics, students
# app.include_router(courses.router, prefix="/api/courses")
# app.include_router(analytics.router, prefix="/api/analytics")
# app.include_router(students.router, prefix="/api/students")
