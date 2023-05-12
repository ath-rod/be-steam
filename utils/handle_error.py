from config import logging
from utils.response import ErrorRes
from utils.exceptions import ConstraintError


def handle_error(err: ConstraintError) -> ErrorRes:
    logging.warn(f"Handling error: {err.__dict__}")
    code = hasattr(err, "code") and err.code or 400
    msg = hasattr(err, "msg") and err.msg or "Unexpected Error Occurred"
    errors = hasattr(err, "errors") and err.errors or []
    return ErrorRes(status_code=code, data=dict(errors=errors, msg=msg))
