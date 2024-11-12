import urllib.request
import json
with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
    is_it_raining_in_seattle = response.read().decode()

if is_it_raining_in_seattle == "true":
    print("Yes!")
else:
    print("No!")