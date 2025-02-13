import streamlit as st

def render_career_comparison(expert_system):
    st.markdown("## Perbandingan Karir")
    job1 = st.selectbox("Karir Pertama:", sorted(expert_system.rules.keys()), key="job1")
    job2 = st.selectbox("Karir Kedua:", sorted(expert_system.rules.keys()), key="job2")
    
    if st.button("Bandingkan"):
        if 'analysis_results' in st.session_state:
            user_traits = st.session_state.get('user_traits', [])
            education_level = st.session_state.get('education_level', "Sarjana")
            experience_years = st.session_state.get('experience_years', 0)
            
            comparison = {
                job1: expert_system.create_detailed_analysis(job1, user_traits, education_level, experience_years),
                job2: expert_system.create_detailed_analysis(job2, user_traits, education_level, experience_years)
            }
            
            render_comparison_results(expert_system, job1, job2, comparison)

def render_comparison_results(expert_system, job1, job2, comparison):
    col1, col2 = st.columns(2)
    for idx, (job, analysis) in enumerate(comparison.items()):
        with col1 if idx == 0 else col2:
            st.subheader(job)
            st.metric("Nilai Kecocokan", f"{analysis['overall_score']:.1f}%")
            st.markdown("#### Keterampilan Yang Dibutuhkan")
            for skill in analysis['required_skills']:
                st.write(f"• {skill}")