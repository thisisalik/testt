from django.test import TestCase
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.db import models
from models.models import Web_model
import uuid
import numpy as np
import datetime
import sys
import pylab as pl
import ionofunclib as myfunc
import ionoconslib as mycons
import nedm2020funclib as nedm
import timeit
from .forms import Webmodelform

def model(request,pk):
    web_id=Web_model.objects.get(id=pk)
    lat_a=web_id.objects.values_list('lat_a')[0][0]
   
    print(lat_a)
    #just comment