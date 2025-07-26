import streamlit as st
import math
def bf(gender,waist,neck,hip,height):
  if waist==0 or neck==0 or hip==0 or height==0:
    st.error("⚠️ Oops! Looks like something’s missing or incorrect. Please check your input and try again.")
  else:
    if gender=='Male' or gender =='male':
          a=round(86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76, 2)
          if a<= 13:
             v= "✅ Excellent (Fit)"
          elif a <= 17:
             v= "🟡 Good"
          elif a<= 21:
            v= "⚠️ Borderline"
          elif a <= 25:
            v= "❌ Over Limit (Bad)"
          else:
            v= "🚫 Fails Standard"
    elif gender =='Female' or 'female':
          body_fat = (163.205 * math.log10(waist + hip - neck) -
                    97.684 * math.log10(height) -
                    78.387)
          a=round(body_fat, 2)
          if a <= 22:
            v="✅ Excellent (Fit)"
          elif a <= 26:
            v= "🟡 Good"
          elif a <= 30:
            v= "⚠️ Borderline"
          elif a<= 33:
            v="❌ Over Limit (Bad)"
          else:
           v= "🚫 Fails Standard"
        
    st.success(f"sucess {a}{v}")
    st.info('''Disclaimer: The body fat percentage shown is an estimate based on the U.S. Navy Body Fat Formula.
It does not account for muscle mass, bone density, or fat distribution, so it may not be fully accurate, especially for athletes or individuals with high muscle mass.
For the most precise results, consult a healthcare professional or use medical-grade tools like DEXA scans or calipers.''')