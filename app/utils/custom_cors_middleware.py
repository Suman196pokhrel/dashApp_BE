from fastapi import Request, Response
from fastapi.middleware.base import BaseHTTPMiddleware

class CustomCorsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        allowed_origins = ['http://64.227.166.179:3000/auth/login', 'http://localhost:3000']  # Your allowed origins

        origin = request.headers.get('origin')
        if origin not in allowed_origins:
            return Response(content='Origin not allowed', status_code=403)

        response = await call_next(request)
        return response
