from cerberus import Validator as validator
from utils.exceptions import ConstraintError


class Validator:
    """
    Wraps Cerberus Validator module
    to provide a flexible schema validator

    ::param schema dict
    """

    def __init__(self, schema: dict, *args, **kwargs) -> "Validator":
        self.validator = validator(schema)
        self.errors = None

    def validate(self, data: object, use_exception: bool = True) -> object:
        result = self.validator.validate(data)
        self.errors = [{k: v} for k, v in self.validator.errors.items()]

        if use_exception and not result:
            raise ConstraintError("Input Contraint Violation", errors=self.errors)
        return result
