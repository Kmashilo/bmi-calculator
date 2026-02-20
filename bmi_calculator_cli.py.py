def calculate_bmi(weight, height):
    # Calculate BMI using the formula: BMI = weight (kg) / (height (m))**2
    bmi = weight / (height ** 2)
    return round(bmi, 2)  # Round BMI to 2 decimal places for better readability

def classify_bmi(bmi):
    # Classify BMI based on standard classification:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:  # Adjusted to include upper bound
        return "Normal weight"
    elif 25 <= bmi <= 29.9:  # Adjusted to include upper bound
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        # Get user input and ensure it is valid
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)

        print(f"Your BMI is: {bmi}")
        print(f"You are classified as: {classification}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()