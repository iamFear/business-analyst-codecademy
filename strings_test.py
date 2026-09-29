def username_generator(first_name, last_name):
  user_name = ""
  first_slice = ""
  last_slice = ""

  if (len(first_name) < 3 or len(last_name) < 4):
    first_slice = first_name
    last_slice = last_name
  else:
    # First three letters of his first name
    first_slice = first_name[:3]
    # First four letters of his last name
    last_slice = last_name[:4]

  user_name = first_slice + last_slice

  print(user_name)
  return user_name

# username_generator("Daniel", "Burgoa")
# username_generator("Ki", "Ko")

def password_generator(user_name):
  password = ""

  for char in range(0, len(user_name)):
    # print(password[char])
    password = password + user_name[char - 1]
  
  # print(password)
  return password
  

password_generator("DanBurg")

fruit = "watermelon"

# print(0 / 2)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

author_last_names = []

# Great work, but now it turns out they didn’t want poets’ first names 
# (why didn’t they just say that the first time!?)
# Create another list called author_last_names that only contains 
# the last names of the poets in the provided string.

for author in range(0, len(author_names)):
  result = author_names[author].split()[1]
  # print(result)
  
print("Hello\tWorld")
