# bmi_calculator.py

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI given weight (kg) and height (cm)."""
    #Height in cm
    height = height / 100
    return weight / (height ** 2)

def health_risk_assessment(bmi: float) -> str:
    """Assess health risk based on BMI."""
    if bmi < 18.5:
        return "Underweight: Risk of nutritional deficiency and osteoporosis."
    elif 18.5 <= bmi < 24.9:
        return "Normal: Low risk of weight-related health issues."
    elif 25 <= bmi < 29.9:
        return "Overweight: Increased risk of cardiovascular diseases."
    else:
        return "Obese: High risk of weight-related health problems."
