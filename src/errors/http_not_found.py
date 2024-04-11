class HttpNotFoundException(BaseException):
    def __init__(self, message: str = "Not found"):
        super().__init__(404, message)
        self.message = message
        self.status_code = 404
        self.error = "Not found"