from fpdf import FPDF
import bmi as bm
import bodyf as be
import waist as wf
import pulse as pf
import streamlit as st
def pd(details, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(0, 10, "NavyMetrics Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    details = {
    "name" : st.session_state.get("name","Not entered"),
    "weight": st.session_state.get("weight", "Not entered"),
    "height": st.session_state.get("height", "Not entered"),
    "waist": st.session_state.get("waist", "Not entered"),
    "hip": st.session_state.get("hip", "Not entered"),
    "neck": st.session_state.get("neck", "Not entered"),
    "pulse": st.session_state.get("pulse", "Not entered"),
    "gender": st.session_state.get("gender", "Not selected")
    }
# Only calculate if all needed inputs are present
    try:
        bmi_result = bm.bmi(details["height"], details[ "weight"])
        whr_result = wf.wf(details["waist"], details["hip"], details["gender"])
        bfp_result = be.bf(details["gender"], details["waist"], details["neck"], details["hip"], details["height"] * 100)
        pulse_result = pf.check_pulse(details["pulse"])
    except Exception as e:
        st.error("Error in calculation: " + str(e))
        bmi_result = whr_result = bfp_result = pulse_result = "Error"

    results = {
    "Body Mass Index": bmi_result,
    "Waist-to-Hip Ratio": whr_result,
    "Body Fat Percentage": bfp_result,
    "Pulse Status": pulse_result
    }


    for key, value in details.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    for key, value in results.items():
        pdf.cell(200,10,txt=f"{key}: {value}", ln=True)
    pdf.output("Navymetrics_report.pdf")
    with open("Navymetrics_report.pdf", "rb") as f:
        st.download_button("📥 Download Health Report PDF", f, file_name="Navymetrics_report.pdf")