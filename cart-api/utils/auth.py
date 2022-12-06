from functools import wraps
import json
from flask import request, _request_ctx_stack
from six.moves.urllib.request import urlopen
from jose import jwt

from apps.config import Config

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    '''Obtains access token from header
    '''

    auth = request.headers.get("Authorization", None)

    if not auth:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization header is expected"
        }, 401)
    
    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must start with Bearer"
        }, 401)
    elif len(parts) == 1:
        raise AuthError({
            "code": "invalid_header",
            "description": "Token not found"
        }, 401)
    elif len(parts) > 2:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must be Bearer token"
        }, 401)

    token = parts[1]
    return token


def requires_auth(f):
    '''Determines if access token is valid
    '''

    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://" + Config.AUTH0_DOMAIN + "/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=["RS256"],
                    audience=Config.API_AUDIENCE,
                    issuer="https://"+Config.AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({
                    "code": "token_expired",
                    "description": "Token is expired"
                }, 401)
            except jwt.JWTClaimsError:
                raise AuthError({
                    "code": "invalid_claims",
                    "description": "incorrect claims"
                }, 401)
            except Exception:
                raise AuthError({
                    "code": "invalid_header",
                    "description": "unable to parse auth token"
                }, 401)
            
            _request_ctx_stack.top.current_user = payload
            print(payload)

            return f(*args, **kwargs)
        raise  AuthError({
            "code": "invalid_header",
            "description": "Unable to find appropriate key"
        }, 401)
    
    return decorated


def requires_scope(required_scope):
    '''Determines if the requiredd scope is present in the Access Token
    Args: 
        required_scope(str): The scope required to access the resource
    '''
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
        token_scopes = unverified_claims["scope"].split()
        for token_scope in token_scopes:
            if token_scopes == required_scope:
                return True
    return False