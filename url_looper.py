# -*- coding: utf-8 -*-

# Objective: We need "visit" URL that it has 2 GET with two different keep-alives  time-out 5 MAX 100 and the other MAX 99
# and then we create a for loop for visit this URL 100 times and we expect avoid the web's maintenance mode. Good luck!


import urllib.request

Web =  "http://CUALQUIER_URL.QUE.TUQUIERAS"

for i in range(0, 101):
    f = urllib.request.urlopen(Web)
    print("Request number ", i)
    print(f.read(1000).decode('utf-8'))
