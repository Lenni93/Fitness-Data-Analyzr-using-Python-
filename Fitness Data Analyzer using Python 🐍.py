def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI) given weight and height."""
    return weight / (height ** 2)


def calculate_calories_burned(duration, calorie_burn_rate=5):
    """Calculate the estimated number of calories burned during exercise."""
    return duration * calorie_burn_rate


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi > 25:
            overweight_people.append(person)
    return overweight_people


def Health_Fit(people_date):
    health_people = []
    for person in people_date:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi < 21:
            health_people.append(person)
    return health_people


# Main program
people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")

name = input("Enter person's name: ").strip()
weight = float(input("Enter person's weight in kilograms: "))
height = float(input("Enter person's height in meters: "))
duration = float(input("Enter exercise duration in minutes: "))
person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
print(person)

overweight_people = filter_overweight_people(people_data)
if calculate_bmi(weight,height) > 25:
    print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")

health_people = Health_Fit(people_data)
if calculate_bmi(weight, height) < bmi:
    print("\nHealth_fit:")
for person in health_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")
