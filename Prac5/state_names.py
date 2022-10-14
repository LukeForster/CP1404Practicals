"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# This file has been reformatted so the dictionary code follows PEP 8 convention

states = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT" : "Northern Territory",
                "WA" : "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania"}
print(states)

state = input("Enter short state: ").upper()
while state != "":
    if state in states:
        print(state, "is", states[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()