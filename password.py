import random
import string

def generate_password(length):

  # High complexity includes letters, digits, and punctuation
  all_chars = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choices(all_chars, k=length))
  return password

# Get user input for length
while True:
  try:
    length = int(input("Enter desired password length : "))
    if length < 5:
      print("Password length should be at least 5. Please try again.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a number.")

# Generate and display password with high complexity
password = generate_password(length)
print("Your generated password is:",password)