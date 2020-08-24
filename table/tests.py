"""
@author: jcachaldora
test.py - test class 
Instruction: 
   In sv, $python manage.py shell
   from table import tests
   tests.function_name() to run test
"""

from django.test import TestCase
from os import path
from table.models import Spectrum

#Prints information on spectral plots in "table/static/"
def checkplots():
    i = 0
    fields = list()
    for spectrum in Spectrum.objects.all():
        isfile = path.exists("table/static"+spectrum.fig_name)
        if(isfile == True):
            i+=1
        elif(spectrum.field not in fields):
            fields.append(spectrum.field)
            
    print("# Figures: "+str(i))
    print("# Spectra: "+str(Spectrum.objects.count()))
    print("Figure/Spectra ratio: "+str(i/Spectrum.objects.count()))
    print("Fields missing plots:")
    for x in fields:
        print(x)

