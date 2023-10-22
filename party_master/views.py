from django.shortcuts import render, redirect
from party_master.forms import PartyMasterForm
from party_master.models import PartyMaster


def party_list(request):
    parties = (
        PartyMaster.objects.all()
    )  # Replace this with your query to retrieve parties
    return render(request, "party_master/party_list.html", {"parties": parties})


def add_party(request):
    if request.method == "POST":
        form = PartyMasterForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect("party_list")  # Redirect to a party list view
    else:
        form = PartyMasterForm()

    return render(request, "party_master/party_form.html", {"form": form})
