# calorie_calculator.py

def daily_caloric_needs(age: int, gender: str, height: float, weight: float, activity_level: str) -> float:
    """Calculate daily caloric needs based on Mifflin-St Jeor Equation."""
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "super active": 1.9,
    }

    return bmr * activity_multipliers.get(activity_level, 1.2)
