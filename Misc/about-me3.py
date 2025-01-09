from datetime import date, datetime


name = input("Hello! Please enter your name and tap Enter: ");

dayOfBirthStr = input("Enter your day of birth (year/month/day) and tap Enter: ");
dayOfBirth = datetime.strptime(dayOfBirthStr,"%Y/%m/%d");
age = datetime.today().year - dayOfBirth.year;

hobby = input("Enter your hobbies and tap Enter: ");
print();
print("Thank you! Your profile is ready!");
print();
print(f"Name: {name}");
print(f"Age: {age}");
print(f"Hobby: {hobby}");
input("Please tap Enter to Exit.");
