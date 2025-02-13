import streamlit as st
from expert_system import CareerExpertSystem
from tabs.career_analysis import render_career_analysis
from tabs.career_comparison import render_career_comparison
from tabs.career_recommendation import render_career_recommendation

def main():
    st.set_page_config(page_title="CareerGuide.id", page_icon="👨‍💼", layout="wide")
    
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            height: 3em;
            margin-top: 2em;
        }
        .reportview-container {
            background: #f0f2f6
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("🎯 CareerGuide.id")
    st.markdown("---")

    expert_system = CareerExpertSystem()
    
    tabs = st.tabs(["Analisa Karir", "Perbandingan Karir", "Rekomendasi Karir"])
    
    with tabs[0]:
        render_career_analysis(expert_system)
    
    with tabs[1]:
        render_career_comparison(expert_system)
    
    with tabs[2]:
        render_career_recommendation(expert_system)

if __name__ == "__main__":
    main()