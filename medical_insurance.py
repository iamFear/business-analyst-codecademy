age = 28
# Female = 0 / Male = 1
sex = 0
bmi = 26.2
num_of_children = 3
# 0 = non / 1 = yes
smoker = 0

insurance_cost = 250 * age - 128 * sex + 370 * bmi 
+ 425 * num_of_children + 24000 * smoker - 12500

age_mod = 4
# age += age_mod

bmi_mod = 3.1
# bmi += bmi_mod

sex_mod = 1
sex += sex_mod

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi 
+ 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

# "f" at the beginning of the string to add variables; 
# using variable manipulation to show no decimals

# print(f"This person's insurance cost is {insurance_cost:.0f} dollars.")
# print(f"This person's new insurance cost is {new_insurance_cost:.0f} dollars.")
# print(f"The change in cost of insurance after increasing the age by {age_mod} years is {change_in_insurance_cost:.0f} dollars.")

print(f"This person's insurance cost is {insurance_cost:.0f} dollars.")
print(f"This person's new insurance cost is {new_insurance_cost:.0f} dollars.")
print(f"The change in cost of insurance after increasing the BMI by {bmi_mod} is {change_in_insurance_cost:.0f} dollars.")


