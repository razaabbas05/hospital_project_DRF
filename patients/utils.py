from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response.__class__({
            "success": False,
            "data": None,
            "message": response.data
        }, status=response.status_code)

    return response