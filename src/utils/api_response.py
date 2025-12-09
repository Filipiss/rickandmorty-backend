class ApiResponse:

    @staticmethod
    def success(message, data=None):
        return {
            "success": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message, data=None):
        return {
            "success": False,
            "message": message,
            "data": data
        }