
def home_view(request):
  from django.http import HttpResponse

  # Generate some random number to show it's dynamic!
  import random
  response = random.random()

  return HttpResponse(response)


