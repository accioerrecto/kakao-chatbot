from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, datetime

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['안녕','반가워']
    })

@csrf_exempt
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
            'message': {
                'text': content
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['안녕', '방가방가', 'ㅎㅎ']
            }

        })
