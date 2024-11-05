from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import blog.JWTtoken as JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(data: str = Depends(oauth2_scheme)):
    creadentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate creadentials",
        headers={"WWW-Authentificate": "Bearer"}
    )
    return JWTtoken.verify_token(data, creadentials_exception)