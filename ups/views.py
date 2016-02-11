# -*- coding: utf-8 -*-
import serial
from django.http import HttpResponse
from django.template import RequestContext, loader
def ups(request):

    #ser = serial.Serial("/dev/ttyS0", baudrate=2400)
    #ser.open()
    #ser.write(b"F\r")
    #ups= ser.read(10)

    #ser.write(b"Q1\r")
    #ups1= ser.read(47)
    #battery_voltage_nominal = ups1[0:6]
    #input_frequency_nominal = ups1[7:11]
    #input_voltage = ups1[13:18]
    #input_voltage_fault = ups1[19:24]
    #output_voltage = ups1[25:30]
    #ups_load = ups1[31:34]
    #input_frequency = ups1[35:39]
    #battery_voltage = ups1[40:44]
    #ups_temperature = ups1[45:50]
    #ser.write(b"D\r")
    #ups2= ser.read(14)

    template = loader.get_template('index_1.html')
    #context = RequestContext(request, {
    #    'battery_voltage_nominal': battery_voltage_nominal,
    #    'input_frequency_nominal': input_frequency_nominal,
    #    'input_voltage': input_voltage,
    #    'input_voltage_fault': input_voltage_fault,
    #    'output_voltage': output_voltage,
    #    'ups_load': ups_load,
     #   'input_frequency': input_frequency,
    #    'battery_voltage': battery_voltage,
     #   'ups_temperature': ups_temperature,

    #})


    return HttpResponse(template.render())