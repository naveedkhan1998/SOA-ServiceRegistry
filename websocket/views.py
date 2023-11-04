from django.shortcuts import render

def websocket_example(request):
    return render(request, 'websocket/index.html')
