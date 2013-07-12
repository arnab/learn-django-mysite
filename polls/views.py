from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = { 'latest_poll_list': latest_poll_list }
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', { 'poll': poll })


def results(request, poll_id):
    return HttpResponse("Results for %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Voting on %s" % poll_id)
