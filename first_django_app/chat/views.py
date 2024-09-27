from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('Receive data' + request.POST['textmessage'])
    return render(request, 'chat/index.html')
