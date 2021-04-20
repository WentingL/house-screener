class ApiWrapperException(Exception):
    pass


class ApiConfigPropertyMissingException(ApiWrapperException):
    pass


class ApiRequestException(ApiWrapperException):
    pass


class ApiWrapperDeprecatedException(ApiWrapperException):
    pass
