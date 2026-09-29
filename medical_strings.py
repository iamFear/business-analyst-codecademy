medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Print current data
# print(medical_data)

# Replace all instances of # with $ to represent insurance costs in US dollars
updated_medical_data = medical_data.replace("#", "$")

# Print the updated medical_data
# print(updated_medical_data)

# Calculate the number of medical records in our data
num_records = 0

for character in updated_medical_data:
  if character == "$":
    num_records += 1

# print("There are {num_records} medical records in the data.".format(num_records=num_records))

# Split the updated medical data into a list of each medical record
medical_data_split = updated_medical_data.split(";")
# print(medical_data_split)

# Individual medical records
medical_records = []

for record in medical_data_split:
  medical_records.append(record.split(","))

# print(medical_records)

# Store properly formatted medical data
medical_records_clean = []

# for record in medical_records:
#   record_clean = []
#   for item in record:
#     record_clean.append(item.strip())
#   medical_records_clean.append(record_clean)

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())

  medical_records_clean.append(record_clean)

# print(medical_records_clean)

# for record in medical_records_clean:
#   print(record[0].upper())

# Store each name, age, BMI, and insurance cost in separate lists
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# print(names)
# print(ages)
# print(bmis)
# print(insurance_costs)

total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
# print(f"Average BMI: {round(average_bmi, 2)}")

total_insurance_cost = 0

for cost in insurance_costs:
  total_insurance_cost += float(cost.replace("$", ""))

average_insurance_cost = total_insurance_cost / len(insurance_costs)
print(f"Average Insurance Cost: {round(average_insurance_cost, 2)}")

for name, age, bmi, cost in zip(names, ages, bmis, insurance_costs):
  print(f"{name} is {age} years old with a BMI of {bmi} and an insurance cost of {cost}.")
