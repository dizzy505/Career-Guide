import streamlit as st

def render_career_recommendation(expert_system):
    st.markdown("## Rekomendasi Karir")
    
    if 'analysis_results' in st.session_state:
        user_traits = st.session_state.get('user_traits', [])
        education_level = st.session_state.get('education_level', "Sarjana")
        experience_years = st.session_state.get('experience_years', 0)
        
        recommendations = expert_system.get_career_recommendations(
            user_traits, education_level, experience_years
        )
        
        for job, score in recommendations:
            with st.expander(f"{job} - Nilai Kecocokan: {score:.1f}%"):
                st.write(f"Type of expert_system.rules[job]: {type(expert_system.rules[job])}")
    else:
        st.warning("Silakan lengkapi profil Anda terlebih dahulu untuk mendapatkan rekomendasi karir.")