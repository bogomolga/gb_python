# 1. Приложение
# Модуль 1: data_provider
# Модуль 2: logger
# Модуль 3: user_interface
# Модуль 4: html_creater
# Модуль 5: main

import pytest
from random import randint

def get_temperature(sensor):
    #return 0 #заглушка
    return randint(-20,0) if sensor else randint(0,20)

def get_preassure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)

def get_wind_speed(sensor):
    if sensor ==1:
        return randint(0,30)
    else:
        return(30,50)

def data_collection(sensor = 1):
    return(get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))



