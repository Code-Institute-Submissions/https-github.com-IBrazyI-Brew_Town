from django.shortcuts import render

def poll(request):
    template = 'poll/poll.html'
    return render(request, template)
