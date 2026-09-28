print("====================================")
print("       FITNESS AND DIET LOG     ")
print("====================================")

while True:

    print("1. Add Daily Fitness Record")
    print("2. View Fitness Records")
    print("3. BMI Calculator")
    print("4. Daily Calorie Calculator")
    print("5. Calorie Goal & Remaining Calories")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Record
    if choice == "1":

        print("----- DAILY FITNESS RECORD -----")

        name = input("Enter your name: ")
        weight = float(input("Enter your weight in kg: "))

        food = input("Enter food you ate: ")
        quantity = float(input("Enter quantity: "))

        calories = float(input("Enter calories per quantity: "))

        exercise = float(input("Enter exercise minutes: "))

        calories_in = calories * quantity
        calories_out = exercise * 5
        net_calories = calories_in - calories_out

        file = open("fitness_records.txt", "a")

        file.write("Name: " + name + "\n")
        file.write("Weight: " + str(weight) + " kg\n")
        file.write("Food: " + food + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Calories In: " + str(calories_in) + "\n")
        file.write("Exercise: " + str(exercise) + " minutes\n")
        file.write("Calories Out: " + str(calories_out) + "\n")
        file.write("Net Calories: " + str(net_calories) + "\n")
        file.write("-----------------------------\n")

        file.close()

        print("Record saved successfully!")

        print("Calories Consumed:", calories_in)
        print("Calories Burned:", calories_out)
        print("Net Calories:", net_calories)

    # View Records
    elif choice == "2":

        print("----- FITNESS RECORDS -----")

        file = open("fitness_records.txt", "r")

        records = file.read()

        print(records)

        file.close()

    # BMI Calculator
    elif choice == "3":

        print("----- BMI CALCULATOR -----")

        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        bmi = weight / (height * height)

        print("Your BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
            print("\n----- FITNESS ADVICE -----")
            print("Exercise: Strength training and light cardio.")
            print("Food: Eat balanced meals with enough protein and calories.")
            print("Nutrition: Include milk/curd, eggs, dal, nuts, fruits and vegetables.")
            print("Sleep: Aim for 8-10 hours of sleep.")
            print("Tip: Focus on healthy weight gain, not junk food.")

        elif bmi < 25:
            print("Category: Normal Weight")
            print("\n----- FITNESS ADVICE -----")
            print("Exercise: Continue regular strength training and cardio.")
            print("Food: Eat a balanced diet with protein, carbs, healthy fats and vegetables.")
            print("Nutrition: Get vitamins and minerals mainly from varied foods.")
            print("Sleep: Aim for 8-10 hours of sleep.")
            print("Tip: Maintain your current healthy habits.")

        elif bmi < 30:
            print("Category: Overweight")
            print("\n----- FITNESS ADVICE -----")
            print("Exercise: Focus on regular walking, cardio and strength training.")
            print("Food: Choose more vegetables, fruits, whole grains and protein-rich foods.")
            print("Nutrition: Avoid relying heavily on sugary drinks and highly processed foods.")
            print("Sleep: Aim for 8-10 hours of sleep.")
            print("Tip: Focus on healthy habits rather than rapid weight loss.")

        else:
            print("Category: Obese")
            print("\n----- FITNESS ADVICE -----")
            print("Exercise: Start with comfortable activities like walking and gradually increase activity.")
            print("Food: Focus on balanced meals with vegetables, fruits, whole grains and protein.")
            print("Nutrition: Get vitamins and minerals from a varied diet.")
            print("Sleep: Aim for 8-10 hours of sleep.")
            print("Tip: Make gradual, sustainable lifestyle changes.")

    # Daily Calorie Calculator
    elif choice == "4":

        print("----- DAILY CALORIE CALCULATOR -----")

        age = int(input("Enter your age: "))
        gender = input("Enter your gender (M/F): ").upper()
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))

        print("\nActivity Level:")
        print("1. Sedentary")
        print("2. Lightly Active")
        print("3. Moderately Active")
        print("4. Very Active")

        activity = input("Enter activity level (1-4): ")

        # Mifflin-St Jeor estimate
        if gender == "M":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif gender == "F":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        else:
            print("Invalid gender!")
            continue

        activity_factors = {
            "1": 1.2,
            "2": 1.375,
            "3": 1.55,
            "4": 1.725
        }

        if activity not in activity_factors:
            print("Invalid activity level!")
            continue

        daily_calories = bmr * activity_factors[activity]

        print("\nEstimated BMR:", round(bmr), "calories/day")
        print("Estimated Daily Calories:", round(daily_calories), "calories/day")
        print("Note: This is only an estimate, not a medical recommendation.")

    # Calorie Goal & Remaining Calories
    elif choice == "5":

        print("----- CALORIE GOAL & REMAINING CALORIES -----")

        calorie_goal = float(input("Enter your daily calorie goal: "))
        calories_consumed = float(input("Enter calories consumed: "))
        calories_burned = float(input("Enter calories burned through exercise: "))

        net_calories = calories_consumed - calories_burned
        remaining = calorie_goal - net_calories

        print("\nDaily Calorie Goal:", calorie_goal)
        print("Calories Consumed:", calories_consumed)
        print("Calories Burned:", calories_burned)
        print("Net Calories:", net_calories)

        if remaining > 0:
            print("Calories Remaining:", round(remaining, 2))
            print("Status: You are within your daily calorie goal.")
        elif remaining == 0:
            print("Calories Remaining: 0")
            print("Status: You have reached your daily calorie goal.")
        else:
            print("Calories Over Goal:", round(abs(remaining), 2))
            print("Status: You are above your daily calorie goal.")

    # Exit
    elif choice == "6":

        print("Thank you for using Fitness and Diet Log!")

        break

    else:

        print("Invalid choice! ENTER BETWEEN 1-6")