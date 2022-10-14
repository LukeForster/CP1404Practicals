"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# This file has been reformatted so the dictionary code follows PEP 8 convention

short_to_long_states = {"QLD": "Queensland",
                        "NSW": "New South Wales",
                        "NT": "Northern Territory",
                        "WA": "Western Australia",
                        "ACT": "Australian Capital Territory",
                        "VIC": "Victoria", "TAS": "Tasmania"}
print(short_to_long_states)

users_state = input("Enter short state: ").upper()
while users_state != "":
    # if users_state in short_to_long_states:
    #     print(users_state, "is", short_to_long_states[users_state])
    # else:
    #     print("Invalid short state")
    try:
        print(users_state, "is", short_to_long_states[users_state])
    except KeyError:
        print("Invalid short state")

    users_state = input("Enter short state: ").upper()

for state_short, state_long in short_to_long_states.items():
    print(f'{state_short} is {state_long}')
