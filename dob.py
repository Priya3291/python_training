from datetime import date, datetime
dob=input("Enter your DOB(YYYY-MM-DD)")
dob_year, dob_month, dob_day=map(int, dob.split("-"))
today= date.today()
age=today.year - dob_year-((today.month, today.day)<(dob_month, dob_day))
print("Your age is:",age)