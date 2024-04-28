def calculate_bmi(weight, height):
    """
    Args:
    weight (float): Weight of the person in kilograms.
    height (float): Height of the person in meters.

    Returns:
    float: Body Mass Index (BMI) of the person.
    """
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

# Test calculate_bmi function
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']} has a BMI of {bmi:.2f}")

# Test calculate_calories_burned function
duration = 30
calories_burned = calculate_calories_burned(duration)
print(f"Calories burned after {duration} minutes of exercise: {calories_burned}")

# Test filter_overweight_people function
overweight_people = filter_overweight_people(people_data)
for person in overweight_people:
    print(f"{person['name']} is overweight with a BMI of {calculate_bmi(person['weight'], person['height']):.2f}")
    print("Overweight people:")