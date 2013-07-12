from django.http import HttpResponse

def index(request):
    return HttpResponse("All polls")

def detail(request, poll_id):
    return HttpResponse("Details for %s" % poll_id)

def results(request, poll_id):
    return HttpResponse("Results for %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Voting on %s" % poll_id)
