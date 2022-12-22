import time
from turtle import delay
from django.core.exceptions import PermissionDenied

req = {}
class DelayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR')

        if ip not in req:
            req[ip] = 0

            if req[ip] % 4 == 0:
                time.sleep(5)
                response = self.get_response(request)

                return response

            else:
                response = self.get_response(request)

                return response


        else:
            req[ip] = req[ip] + 1

            if req[ip] % 4 == 0:
                time.sleep(5)
                response = self.get_response(request)
                print(req)
                return response

            else:
                response = self.get_response(request)
                print(req)
                return response



