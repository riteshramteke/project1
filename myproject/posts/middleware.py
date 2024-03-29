import json
from datetime import datetime

class ResponseStandardizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'application/json' in response.get('Content-Type', ''):
            try:
                response_data = json.loads(response.content)
            except json.JSONDecodeError:
                # Unable to decode JSON, so it might not be JSON data
                pass
            else:
                standardized_response = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                    "path": request.path,
                    "method": request.method,
                    "result": response_data
                }
                response.content = json.dumps(standardized_response)

        return response
