from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "eat no meat for the entire month",
    "february": "walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month",
    "may" : "Walk for at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "index.html", {
        "months" : months
    })

def mounthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month >len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month= months[month-1]
    redirect_path = reverse("month-challenge.css", args=[redirect_month])
    return HttpResponseRedirect("/challenges/" + redirect_month)


def mounthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404()