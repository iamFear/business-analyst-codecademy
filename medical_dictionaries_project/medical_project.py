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

# Start the running total at zero, then add each patient's insurance cost.
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost

# Divide the total by the number of patients to find the average cost.
average_cost = total_cost / len(medical_costs)

# Matching positions in these lists connect each patient's name to their age.
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# zip() pairs matching positions; list() stores the pairs as a reusable list.
zipped_ages = list(zip(names, ages))


