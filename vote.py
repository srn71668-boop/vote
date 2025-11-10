try:
    age = int(input("enter your age: ")
    if age >= 18:
       print(f"your eligible to vote")
    else:
      print(f"your  not eligible to vote")
except ValueError:
      print(f"not valid")
