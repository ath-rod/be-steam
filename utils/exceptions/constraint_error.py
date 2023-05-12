class ConstraintError(Exception):
    def __init__(self, msg: str = "Constraint violation", *args, **kwargs):
        Exception.__init__(self, msg, args, kwargs)
        self.msg = msg
        self.args = args

        # Iterate kwargs
        [setattr(self, k, v) for k, v in kwargs.items()]
