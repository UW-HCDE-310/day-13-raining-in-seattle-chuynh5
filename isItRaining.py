import urllib.request
import json
with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
    is_it_raining_in_seattle = response.read().decode().strip().lower()

if is_it_raining_in_seattle == "true":
    print("Yes!")
elif is_it_raining_in_seattle == "false":
    print("No!")
else:
    print("Unexpected response:", is_it_raining_in_seattle)