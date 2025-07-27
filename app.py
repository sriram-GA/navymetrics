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
    def inputs():
        st.session_state.name=st.text_input("Enter your name")
        st.session_state.gender=st.radio("select gender",['Male','Female'])
        st.session_state.weight=st.number_input("Enter your weight in kg")
        st.session_state.height=st.number_input("Enter your height in meters")
        st.session_state.waist=st.number_input("enter your waist length in cm")
        st.session_state.neck=st.number_input("enter your neck length in cm")
        st.session_state.hip=st.number_input("enter your hip circumstance in cm""NOTE only if your women")
        st.session_state.pulse = st.number_input("Enter your resting heart rate (bpm):", min_value=30, max_value=200)
    inputs()
    if st.button("🔁 Reset All"):
        st.session_state.clear()
        st.rerun()

    c1,c2=st.columns(2)
    with c1:
        st.header("Body mass index")
        if st.button("click here to check your BMI"):
            bm.bmi(st.session_state.height,st.session_state.weight)
    with  c2:
         st.header("Waist to hip ratio")
         if st.button("click here to check your WTHR"):
             wf.wf(st.session_state.waist,st.session_state.hip,st.session_state.gender)
    c3,c4=st.columns(2)
    with c3:
        st.header("Body fat percentage")
        if st.button("clicke here to check your BFP"):
            bf.bf(st.session_state.gender,st.session_state.waist,st.session_state.neck,st.session_state.hip,st.session_state.height*100)
    with c4:
        st.header("Pulse checker")
        if st.button("click here to check your PC"):
            ps.check_pulse(st.session_state.pulse)
    
elif pages == 'contact us':
    tr.contactus()
import pdf_gen

details = {...}
results = {...}
pdf_gen.pd(details, results)



