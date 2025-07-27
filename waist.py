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
      st.success(f"Waist to hip ratio:{a:.2f}-{v}")
      st.info('''Waist-to-Hip Ratio is a general health indicator and not a medical diagnosis. It may not reflect muscle mass or individual differences. Consult a healthcare professional for accurate health assessments.''')
      return f"Waist to hip ratio:{a:.2f}-{v}"