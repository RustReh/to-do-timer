from dataclasses import dataclass
import datetime as dt
from datetime import timedelta

from jose import jwt
from jose.exceptions import JWTError

from exception import UserNotFoundException, UserNotCorrectPasswordException, TokenExpiredException, \
    TokenNotCorrectException
from models import UserProfile
from repository import UserRepository
from schema.user import UserLoginSchema
from settings import Settings


@dataclass
class AuthService:
    user_repository: UserRepository
    settings: Settings

    async def login(self, username:str, password:str) -> UserLoginSchema:
        user = await self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException

    def generate_access_token(self, user_id: int) -> str:
        expires_date_unix = (dt.datetime.utcnow() + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {'user_id': user_id, 'expire': expires_date_unix},
            self.settings.JWT_SECRET_KEY,
            algorithm=self.settings.JWT_ENCODE_ALGORITHM
        )
        return token

    def get_user_id_from_token(self, access_token: str) -> int:
        try:
            payload = jwt.decode(access_token, self.settings.JWT_SECRET_KEY, algorithms=self.settings.JWT_ENCODE_ALGORITHM)
        except JWTError:
            raise TokenNotCorrectException
        if payload['expire'] < dt.datetime.utcnow().timestamp():
            raise TokenExpiredException

        return payload['user_id']
