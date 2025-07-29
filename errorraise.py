num=input("Enter a number:")
try:
    if not num.isnumeric():
        raise ValueError("Input is not a valid number.")
except ValueError as e:
    print(e)
