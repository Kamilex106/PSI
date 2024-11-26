from fastapi import HTTPException, Request
from fastapi.responses import Response
from uuid import UUID

sessions = {}

def set_cookie(response: Response, session_id: UUID):
    response.set_cookie(key="session", value=str(session_id), httponly=True)

def get_cookie(request: Request):
    cookie = request.cookies.get("session")
    if not cookie:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        session_id = UUID(cookie)
        return session_id
    except ValueError:
        print(f"Invalid cookie format: {cookie}")
        raise HTTPException(status_code=400, detail="Invalid session cookie format")


def create_session(user_id: int) -> UUID:
    session_id = UUID(int=user_id)
    sessions[session_id] = {"user_id": user_id}
    return session_id

def get_session(session_id: UUID):
    if session_id in sessions:
        return sessions[session_id]
    raise HTTPException(status_code=401, detail="Session not found")
