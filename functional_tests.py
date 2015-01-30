# Functional Tests for Bluber

from selenium import webdriver
import unittest

# Unit Test: CreatingNewRide

# Dan, your average Havebro, has just finished finals and needs to go to the
# airport. He has heard about a site called Bluber, a website kind of like Uber but
# without the shady business practices, and for BiCo students only. He's going
# to offer his car up as transport to PHL Airport to offset gas prices


# He visits the website, and is greeted with an invitation telling him what the site does. 

# The website has a call to action, inviting him to login with his Haverford ID.
# He does so. 

# Upon logging in with his BiCo ID, it invites him to a panel that has two
# simple buttons: 'Start a ride' or 'Join/Request a ride'. He clicks the first
# button. 

# He's offered a panel that offers a starting destination picker from Google
# Maps, and an ending destination picker on Google Maps. Oh, and a time picker
# too. He sets the date and time of departure as May 19th, 2016, the departure
# point as Haverford College and the destination as Bryn Mawr College. 

# In the notes he writes: "I would be grateful if any fellow rider could help me
# cover fuel costs."

# He hits 'Create ride' and is presented with a URL (access restricted to those
# with Haverford logins) that he can share with his friends on Facebook to get
# rideshare signups. 

# He clicks a button somewhere that says "My Rides" and sees that the ride he
# just created is there. Satisfied, he closes his browser. 

# TODO: Outline unit test for JoiningARide
