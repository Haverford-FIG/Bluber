"""
Brainstorm (3-3-15)

Users
-- Name *
-- Username *
-- Email *
-- Password *
[ForeignKey] -- Offered Trips
[ForeignKey] -- Requested Trips
[ForeignKey] -- Past Trips



Trips
[datetime] -- Start datetime
[string] -- Start location
[string] -- GPS start location

[string] -- End location
[string] -- GPS end location

[ForeignKey] -- List of users requesting this trip (Passengers)
[ForeignKey] -- Driver (User)
[string] -- Details
[integer] -- Max capacity
[float] -- Price [if price==0, then "free";
                  elif price<0, price is "no fixed price";
                  else price per person]
[ForeignKey] -- Comments/Questions



Comments
[datetime] -- Submission datetime
[ForeignKey] -- Submitted by (User)
[string] -- Content of the comment
[ForeignKey] -- Associated Trip


"""


from django.db import models
from django.contrib.auth.models import User



class Trip(models.Model):
    start_datetime = models.DateTimeField()

    start_location = models.CharField(max_length=120)
    end_location = models.CharField(max_length=120)

    start_gps = models.CharField(max_length=120)
    end_gps = models.CharField(max_length=120)

    requested_by = models.ManyToManyField(User)
    driver = models.ForeignKey(User, null=True, blank=True)

    max_capacity = models.IntegerField(default=4)
    price = models.FloatField(default=0)
    details = models.TextField(default="")

    comments = models.ManyToManyField(Comment)


class ExpandedUser(models.Model):
    user = models.ForeignKey(User, unique=True)

    offered_trips = models.ManyToManyField(Trip)
    requested_trips = models.ManyToManyField(Trip)

    saved_trips = models.ManyToManyField(Trip)
    past_trips = models.ManyToManyField(Trip)



class Comment(models.Model):
    submitted_on = models.DateTimeField()
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)
    content = models.TextField()






