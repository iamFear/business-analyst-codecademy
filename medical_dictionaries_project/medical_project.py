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

# Convert the pairs into a dictionary mapping patient names to ages.
names_to_ages = dict(zipped_ages)

# get() returns Marina's age, or None if her name is not in the dictionary.
marina_age = names_to_ages.get("Marina")
print(f"Marina's age is {marina_age}")

# Start an empty dictionary to hold patients' medical records.
medical_records = {}

# Store Marina's medical details in a nested dictionary under her name.
medical_records["Marina"] = {
    "Age": 27,
    "Sex": "Female",
    "BMI": 31.1,
    "Children": 2,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6607.0
}

# Add each remaining patient's details using the same nested-dictionary structure.
medical_records["Vinay"] = {
    "Age": 24,
    "Sex": "Male",
    "BMI": 26.9,
    "Children": 0,
    "Smoker": "Non-smoker",
    "Insurance_cost": 3225.0
}

medical_records["Connie"] = {
    "Age": 43,
    "Sex": "Female",
    "BMI": 25.3,
    "Children": 3,
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0
}

medical_records["Isaac"] = {
    "Age": 35,
    "Sex": "Male",
    "BMI": 20.6,
    "Children": 4,
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
}

medical_records["Valentina"] = {
    "Age": 52,
    "Sex": "Female",
    "BMI": 18.7,
    "Children": 1,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
}

print(medical_records)

# Look up Connie's record first, then retrieve her insurance cost inside it.
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")

# Remove Vinay's name and its entire nested medical record.
medical_records.pop("Vinay")

# items() provides each patient's name and nested record together.
for name, record in medical_records.items():
    # Insert the name and medical details into the requested summary.
    print(
        f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} "
        f"with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}"
    )
