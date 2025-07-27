import streamlit as st
import personal as pp

def bmi(h,w):
    if h==0 or w==0:
        st.error("⚠️ Oops! Looks like something’s missing or incorrect. Please check your input and try again."

)
        
    else:
        bmi=(w/(h*h))
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        elif bmi < 35:
            category = "Obesity (Class 1)"
        elif bmi < 40:
            category = "Obesity (Class 2)"
        else:
            category = "Extreme obesity"
        st.success(f"Body mass index:{bmi:.2f}-{category}")
        st.info("""
**Diclaimer:** BMI is a rough estimate and may not accurately reflect your health condition.
It does not distinguish between weight from fat and weight from muscle.
""")
        return f"{bmi:.2f} you are {category}"

