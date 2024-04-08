class HttpConflictException(Exception):
    def __init__(self, message: str = "Conflict"):
        super().__init__(409, message)
        self.message = message
        self.status_code = 409
        self.error = "Conflict"
