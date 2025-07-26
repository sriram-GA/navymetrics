import streamlit as st
import pandas as pd
import numpy as np
import aboutus as ap
import contactus as tr
import bmi as bm
import personal as pf
import bodyf as bf
import waist as wf
import pulse as ps
pages=st.sidebar.radio("Navigate",['Home','about us','contact us'])

if pages=='about us':
    ap.aboutusa()
elif pages=='Home':
    st.title("NavyMetrics")
    st.caption("Track. Compare. Conquer")
    weight=st.number_input("Enter your weight in kg")
    height=st.number_input("Enter your height in meters")
    gender=st.radio("select gender",['Male','Female'])
    waist=st.number_input("enter your waist length in cm")
    neck=st.number_input("enter your neck length in cm")
    hip=st.number_input("enter your hip circumstance in cm""NOTE only if your women")
    pulse = st.number_input("Enter your resting heart rate (bpm):", min_value=30, max_value=200)
    if st.button("🔁 Reset All"):
        st.session_state.clear()
        st.rerun()

    c1,c2=st.columns(2)
    with c1:
        st.header("Body mass index")
        if st.button("click here to check your BMI"):
            bm.bmi(height,weight)
    with  c2:
         st.header("Waist to hip ratio")
         if st.button("click here to check your WTHR"):
             wf.wf(waist,hip,gender)
    c3,c4=st.columns(2)
    with c3:
        st.header("Body fat percentage")
        if st.button("clicke here to check your BFP"):
            bf.bf(gender,waist,neck,hip,height*100)
    with c4:
        st.header("Pulse checker")
        if st.button("click here to check your PC"):
            ps.check_pulse(pulse)
    
elif pages == 'contact us':
    tr.contactus()

   


