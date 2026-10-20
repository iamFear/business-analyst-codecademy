# Medical dictionaries educational project.
# Add assignment data and implement each requirement as it is provided.

# Start with an empty dictionary to store patients and their insurance costs.
medical_costs = {}

# Use each patient's name as the key and their insurance cost as the value.
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# update() adds multiple patient-cost pairs in a single line.
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

# Assigning to an existing key replaces its value with the corrected cost.
medical_costs["Vinay"] = 3325.0

# print the medical_costs dictionary
print(medical_costs)
