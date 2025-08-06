user_input=input("Enetr some text to save in file:")
from datetime import datetime
current_datetime=datetime.now()
filename=str(current_datetime).replace(".","_")
with open(filename+".txt","w")as file:
    file.write(user_input)
print("your input had been saved to'sample.py.txt'")