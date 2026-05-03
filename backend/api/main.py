from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.auth_routes import router as auth_router
from backend.api.routes.user_routes import router as user_router
from backend.api.routes.admin_routes import router as admin_router
from backend.api.routes.client_routes import router as client_router

app = FastAPI(title="Secure Auth System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix="/api/user", tags=["User"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])
app.include_router(client_router, prefix="/api/client", tags=["Client"])


@app.get("/")
def root():
    return {"message": "Secure Auth System API is running."}