def calculate_bmi(weight, height):
    return weight / (height ** 2)


def calculate_calories_burned(duration):
    calorie_burn_rate = 5  # 5 calories burned per minute of exercise
    return duration * calorie_burn_rate


def filter_overweight_people(people_data):
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people


# Main program
people_data = []
# Sample data to test the functions
print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")
