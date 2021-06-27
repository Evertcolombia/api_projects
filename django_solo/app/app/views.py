from datetime import datetime

from django.http import HttpResponse, JsonResponse


def hello_world(request):
    """ Return a greeeting """
    return HttpResponse("Hi  Current server time is {now}".format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorted_integers(request):
    """ returns sorted list integers """
    # import pdb;
    #pdb.set_trace()
    print(request.GET)
    print(request.scheme)
    print(request.body)
    print(request.path)
    print(request.path_info)
    print(request.COOKIES)
    numbers = sorted(request.GET['numbers'].split(","))
    data = {
        'status': 'ok',
        'data': [int(n) for n in numbers],
        'message': "integers Sorted"
    }
    return JsonResponse(data)
    #return HttpResponse(JsonResponse(numbers, safe=False))

def validation(request, name, age):
    """ Validated parameters on request"""
    data = dict()
    data["age_message"] = "Required Age 12+"

    if age < 12:
        data["message"]  = "Sorry {} you are not allowed here".format(name)
        data["status"] = "Denegade"

    else:
        data["message"] = "Hello {}! Welcome to our site!".format(name)
        data["status"] = "Success"
    return JsonResponse(data)



