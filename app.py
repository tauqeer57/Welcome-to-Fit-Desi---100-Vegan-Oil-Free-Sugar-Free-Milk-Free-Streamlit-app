# app.py

import streamlit as st
import pandas as pd
from bmi_calculator import calculate_bmi, health_risk_assessment
from calorie_calculator import daily_caloric_needs
from meal_planning import get_meal_options
from progress_tracking import ProgressTracker

# Initialize progress tracker
tracker = ProgressTracker()

# Set the page configuration for better presentation
st.set_page_config(page_title="Desi Vegan", layout="wide", initial_sidebar_state="expanded")

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .sidebar .sidebar-content {
        background-color: #F0F2F6;
    }
    .section-title {
        color: #2E8B57;
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .info-box {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .dataframe-table {
        background-color: #FFFFFF;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .dataframe-table table {
        width: 100%;
        border-collapse: collapse;
    }
    .dataframe-table th, .dataframe-table td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    .dataframe-table th {
        background-color: #f2f2f2;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Sidebar options for navigation
st.sidebar.title("Fit Desi")
app_mode = st.sidebar.radio(
    "Navigation",
    ["Home", "BMI Calculator", "Daily Calorie Intake Calculator", "Meal Planning", "Progress Tracking", "Recall"]
)

# Home section
if app_mode == "Home":
    st.title("Welcome to Fit Desi! - 100% Vegan , Oil-Free, Sugar-Free, Milk-Free")
    st.markdown("#### Your personalized fitness companion for achieving health goals with culturally tailored meal plans.")
    st.image("https://www.shape.com/thmb/Nti_HBKTZCavOIQkCKRJS2sx9W8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/shutterstock_1069332170-2000-364c5bccbb1e4e2a83a0e4cfdc15723a.jpg", use_column_width=True)

# BMI Calculator Section
if app_mode == "BMI Calculator":
    st.markdown("<div class='section-title'>BMI Calculator</div>", unsafe_allow_html=True)
    st.markdown("Calculate your Body Mass Index (BMI) and understand your health risk assessment.")
    
    with st.container():
        weight = st.number_input("Enter your weight (kg):", min_value=0.0, key="bmi_weight")
        height = st.number_input("Enter your height (cm):", min_value=0.0, key="bmi_height")
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        assessment = health_risk_assessment(bmi)
        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(assessment)

# Daily Calorie Intake Calculator Section
elif app_mode == "Daily Calorie Intake Calculator":
    st.markdown("<div class='section-title'>Daily Calorie Intake Calculator</div>", unsafe_allow_html=True)
    st.markdown("Calculate your daily caloric needs based on your age, weight, and activity level.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Enter your age:", min_value=1, key="cal_age")
        gender = st.selectbox("Select your gender:", ["male", "female"], key="cal_gender")
        height_cal = st.number_input("Enter your height (cm):", min_value=1, key="cal_height") / 100  # Convert cm to m
    
    with col2:
        weight_cal = st.number_input("Enter your weight (kg):", min_value=0.0, key="cal_weight")
        activity_level = st.selectbox("Select your activity level:", ["sedentary", "lightly active", "moderately active", "very active", "super active"], key="cal_activity")

    if st.button("Calculate Daily Caloric Needs"):
        daily_calories = daily_caloric_needs(age, gender, height_cal, weight_cal, activity_level)
        st.success(f"Your daily caloric needs are: {daily_calories:.2f} calories")

# Meal Planning Section
elif app_mode == "Meal Planning":
    st.markdown("<div class='section-title'>Meal Planning</div>", unsafe_allow_html=True)
    st.markdown("Choose a meal type to get culturally tailored vegetarian meal options without oil, sugar, or meat.")
    meal_type = st.selectbox("Select meal type:", ["Breakfast", "Lunch", "Dinner", "Snacks"], key="meal_type")

    if st.button("Get Meals"):
        meals_df = get_meal_options(meal_type)
        st.markdown("<div class='dataframe-table'>", 
                    unsafe_allow_html=True)
        st.table(meals_df)
        st.markdown("</div>", 
                    unsafe_allow_html=True)
# Progress Tracking Section
elif app_mode == "Progress Tracking":
    st.markdown("<div class='section-title'>Progress Tracking</div>", unsafe_allow_html=True)
    st.markdown("Log your weight and measurements to track your progress over time.")

    col1, col2 = st.columns(2)

    with col1:
        weight_entry = st.number_input("Log your weight (kg):", min_value=0.0, key="log_weight")

    with col2:
        measurements = {}
        for body_part in ["waist", "hip", "arm", "thigh"]:
            measurements[body_part] = st.number_input(f"Log your {body_part} measurement (cm):", min_value=0.0, key=f"log_{body_part}")

    if st.button("Log Progress"):
        tracker.log_weight(weight_entry)
        tracker.log_measurements(measurements)
        st.success("Progress logged!")

    # Display Progress
    if st.button("Show Progress"):
        progress = tracker.get_progress()
        st.write(progress)

# Recall Section to show previous results
elif app_mode == "Recall":
    st.markdown("<div class='section-title'>Recall</div>", unsafe_allow_html=True)
    st.markdown("Access your past calculations and logged progress.")

    recall_type = st.selectbox("Select data to recall:", ["BMI History", "Caloric Needs", "Logged Progress"], key="recall_type")

    if recall_type == "BMI History":
        st.info("Feature under development to show BMI calculation history.")
    
    elif recall_type == "Caloric Needs":
        st.info("Feature under development to show daily caloric needs history.")
    
    elif recall_type == "Logged Progress":
        progress = tracker.get_progress()
        if progress['weight'] or progress['measurements']:
            st.write("Weight Log:", progress['weight'])
            st.write("Measurements Log:", progress['measurements'])
        else:
            st.warning("No progress logged yet.")
# Footer
st.markdown("---")
st.markdown("Made with :heart: by Fit Desi")
st.markdown("Stay healthy, stay fit!")

