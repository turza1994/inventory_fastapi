class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class ResourceNotFoundException(AppException):
    def __init__(self, resource: str, id: str):
        super().__init__(f"{resource} with id {id} not found", 404)

class ResourceAlreadyExistsException(AppException):
    def __init__(self, resource: str, field: str, value: str):
        super().__init__(f"{resource} with {field} '{value}' already exists", 409)
