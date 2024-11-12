#!/usr/bin/env python3
""" Auth module """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ require_auth """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != "/":
            path += "/"
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user """
        return None