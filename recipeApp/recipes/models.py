from django.db import models

# Create your models here.

PRODUCERS = {
  'soufien': {'name': 'Soufien'},
}


RECIPES = [
  {'name': 'tiramisu', 'producers': [PRODUCERS['soufien']]},
  {'name': 'crêpes', 'producers': [PRODUCERS['soufien']]},
  {'name': 'omelette au fromage', 'producers': [PRODUCERS['soufien']]}
]
