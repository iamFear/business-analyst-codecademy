# The first element you draw is element 6. Pop the value assigned to the key 6 out of the elements dictionary and assign it as the value of the "catalyst" key of reading.

elements = {1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boron", 6: "Carbon", 7: "Nitrogen", 8: "Oxygen", 9: "Fluorine", 10: "Neon", 11: "Sodium", 12: "Magnesium", 13: "Aluminum", 14: "Silicon", 15: "Phosphorus", 16: "Sulfur", 17: "Chlorine", 18: "Argon", 19: "Potassium", 20: "Calcium", 21: "Scandium", 22: "Titanium"}

reading = {}

reading["catalyst"] = elements.pop(6)