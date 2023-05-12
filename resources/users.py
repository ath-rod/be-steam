from flask import Blueprint, request, abort

# locals
from config import logging
from services.users import UserService
from services.authentication import Authentication
from utils import handle_error
from utils.response import SuccessRes, ErrorRes
from utils.exceptions import ConstraintError
from utils.validator import Validator
from schemas import username, password


user_service = UserService()
auth_service = Authentication()
resourse = Blueprint("users", __name__)


@resourse.route("", methods=["POST"])
def post_users():
    user_data = request.get_json()
    error = None
    res = None

    schema = username | password
    validator = Validator(schema)

    try:
        assert validator.validate(user_data)
        result = user_service.create_user(user_data["username"], user_data["password"])
        res = SuccessRes(status_code=201, data=result)
    except ConstraintError as err:
        error = handle_error(err)
    except:
        error = ErrorRes(status_code=500, msg="UnexpecterServerError")
    finally:
        if error:
            return abort(error.json)
        return res.json


@resourse.route("/login", methods=["POST"])
def post_users_login():
    user_data = request.get_json()
    error = None
    res = None

    schema = username | password
    validator = Validator(schema)

    try:
        assert validator.validate(user_data)
        result = auth_service.authenticate(user_data["username"], user_data["password"])
        res = SuccessRes(status_code=200, data=result)
    except ConstraintError as err:
        error = handle_error(err)
    except Exception as err:
        error = ErrorRes(status_code=500, msg="UnexpecterServerError")
    finally:
        if error:
            return abort(error.json)
        return res.json
