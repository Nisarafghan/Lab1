name = input("what is your name?")
print(f"Hello {name}!")

from datetime import datetime
current_year = datetime.now().year

while True:
    try:
        yob = input("What is your year of birth? ")
        age = current_year - int(yob)
        if age < 0:
            raise RuntimeError('age is not right')
    except:
        print("your
        input is wrong")
    else:
        break
print(f"you must be {age} years old!")
print("goodbye")
