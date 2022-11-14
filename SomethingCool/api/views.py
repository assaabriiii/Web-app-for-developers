from django.http import JsonResponse


def getRoutes(request) : 
    routes = [
        {"GET" : "api/project"},
        {"GET" : "api/project/id"},
        {"POST" : "api/project/id/vote"},
        {"POST" : "api/users/token"},
        {"POST" : "api/users/token/refresh"}
    ]
    return JsonResponse(routes , safe=False)