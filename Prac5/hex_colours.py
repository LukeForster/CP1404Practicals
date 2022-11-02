colour_to_code = {"Absolute Zero": "#0048ba",
                   "Acid Green": "	#b0bf1a",
                   "AliceBlue": "#f0f8ff",
                   "Alizarin crimson	": "#e32636",
                   "Amaranth": "#e52b50",
                   "Amber": "	#ffbf00",
                   "Amethyst": "#9966cc",
                   "AntiqueWhite": "#faebd7",
                   "Apricot": "#fbceb1",
                   "Aqua": "#00ffff"}
print(colour_to_code)
for colour in colour_to_code.items():
    print(f'{colour[0]}')

users_colour = input('Please name a colour from the prior list above: ').title()
print(repr(users_colour))
while users_colour != "":
    # if users_state in short_to_long_states:
    #     print(users_state, "is", short_to_long_states[users_state])
    # else:
    #     print("Invalid short state")
    try:
        print(f'{users_colour} colour code is {colour_to_code[users_colour]}')
    except KeyError:
        print("Colour not in list")

    users_colour = input("Enter short state: ").upper()
