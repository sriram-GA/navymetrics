import streamlit as st


def wf(waist, hip, gender):
    if waist == 0 or hip == 0:
        st.error("⚠️ Oops! Looks like something’s missing or incorrect. Please check your input and try again.")
    else:
      a = waist/hip
      v = None
      if gender == 'Male':
        if a <= 0.90:
            v = "Good (Low Risk)"
        elif a <= 0.95:
            v = "Average (Moderate Risk)"
        else:
            v = "High Risk (Bad)"
      elif gender == 'Female':
        if a <= 0.80:
            v = "Good (Low Risk)"
        elif a <= 0.85:
            v = "Average (Moderate Risk)"
        else:
            v = "High Risk (Bad)"
      st.success(f"{a:.2f} {v}")
