COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff",
           "beige": "#f5f5dc", "bisque": "#ffe4c4", "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2",
           "burlywood": "#deb887", "cadetblue": "#5f9ea0"}

color_name = input("Enter a color name (or blank to quit): ").strip().lower()

# Continue prompting until the user enters a blank line
while color_name != "":
    if color_name in COLOURS:
        print(f"{color_name.capitalize()} is {COLOURS[color_name]}")
    else:
        print("Invalid color name. Please enter a valid color name.")

    # Prompt again for color_name
    color_name = input("Enter a color name (or blank to quit): ").strip().lower()
