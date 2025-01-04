import hashlib
import base64
import secrets
import os

def generate_code_verifier(length: int = 127) ->str:
    """PKCEのcode_verifierを生成
       長さは43から128文字の間
    Returns:
        string: code_verifier
    """
    if length < 43 or length > 128:
        raise ValueError("length must be between 43 and 128")
    num_bytes = (length * 3) // 4
    return base64.urlsafe_b64encode(os.urandom(num_bytes)).rstrip(b'=').decode('utf-8')

def generate_code_challenge(verifier):
    """PKCEのcode_challengeを生成

    Args:
        verifier (str): code_verifier

    Returns:
        str: code_challenge
    """
    digest = hashlib.sha256(verifier.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b'=').decode('utf-8')

def generate_state(length=32):
    """stateを生成

    Args:
        length (int, optional): stateの長さ. Defaults to 32.

    Returns:
        str: state
    """
    return secrets.token_urlsafe(length)