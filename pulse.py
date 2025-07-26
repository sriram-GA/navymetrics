import streamlit as st

def check_pulse(pulse):
    if pulse < 40:
        result = "Too Low (Bradycardia - See a doctor)"
    elif pulse <= 60:
        result = "Excellent (Athlete Level)"
    elif pulse <= 75:
        result = "Good (Fit)"
    elif pulse <= 90:
        result = "Average (Acceptable)"
    elif pulse <= 100:
        result = "Borderline (Needs Improvement)"
    else:
        result = "Poor (Fails Navy Standard – Possible Tachycardia)"
    
    st.success(f"Pulse: {pulse} bpm - {result}")
