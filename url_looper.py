# -*- coding: utf-8 -*-

# Objective: We need "visit" URL that it has 2 GET with two different keep-alives  time-out 5 MAX 100 and the other MAX 99
# and then we create a for loop for visit this URL 100 times and we expect avoid the web's maintenance mode. Good luck!


import urllib2

Web =  "http://34.253.233.243/search/index.php"

for i in range(0, 100):
    with urllib.request.urlopen('web) as f:
    print(f.decode('utf-8')
