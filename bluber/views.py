
def home_view(request):
  from django.shortcuts import render
  from models import Trip

  make_test_trip()

  trips = Trip.objects.all()

  return render(request, "home_view.html", {"trips":trips})




def make_test_trip():
    from models import Trip
    import datetime
    trip = Trip()
    trip.start_location = "Here"
    trip.end_location = "There"

    trip.start_datetime = datetime.datetime.now()
    trip.end_datetime = datetime.datetime.now()

    trip.save()
