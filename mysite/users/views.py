from django.http import JsonResponse


# Create your views here.

def index(request):
    data = {
    'Name' : 'Peter Godoy',
    'Track' : 'Backend(Python)',
    'Message' : 'Hi, mentor, you are doing a great job, thank you so much for the opportunity.'
}
    return JsonResponse(data)

