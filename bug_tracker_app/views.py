from django.shortcuts import render, HttpResponseRedirect, reverse
from bug_tracker_app.models import MyUser, Ticket
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from bug_tracker_app.forms import LoginForm
from bugtracker.settings import AUTH_USER_MODEL


@login_required
def index_view(request):
    my_ticket = Ticket.objects.all()
    return render(request, 'index.html', {"titles": my_ticket})



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def add_ticket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data.get("title"),
                description = data.get("description"),
                ticket_author = request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddTicketForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def ticket_detail_view(request, ticket_id):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, "ticket_detail.html", {"tickets": my_ticket})


def user_detail_view(request, user_id):
     my_user = User.objects.filter(id=user_id).first()
     return render(request, "user_detail.html", {"user": user})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


