import streamlit as st
from visualization import create_radar_chart

def render_career_analysis(expert_system):
    col1, col2 = st.columns(2)
    
    with col1:
        selected_job = st.selectbox("Pilih Karir Yang Diinginkan:", sorted(expert_system.rules.keys()), key="selected_job")
        education_level = st.selectbox("Pendidikan Terakhir:", ["SMA", "Diploma", "Sarjana", "Magister", "Doktor"], key="education_level")
        experience_years = st.slider("Pengalaman Kerja:", 0, 20, 0, key="experience_years")
        
    with col2:
        user_traits = st.multiselect(
            "Pilih Karakteristik & Keterampilan:",
            sorted(list(set(trait for info in expert_system.rules.values() for trait in info['traits']))),
            key="user_traits"
        )
        salary_expectation = st.slider(
            "Ekspektasi Gaji Per Tahun (dalam jutaan):",
            10, 1000, (50, 500), 5,
            key="salary_expectation"
        )

    render_sidebar(expert_system, selected_job, user_traits, education_level, experience_years)

    if st.button("Analisa Kesesuaian Karir"):
        st.session_state['analysis_results'] = expert_system.create_detailed_analysis(
            selected_job, user_traits, education_level, experience_years
        )

    if 'analysis_results' in st.session_state:
        render_analysis_results(expert_system, st.session_state['analysis_results'])

def render_sidebar(expert_system, selected_job, user_traits, education_level, experience_years):
    st.sidebar.header("Profil User")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Karir yang Dipilih")
    st.sidebar.write(selected_job if selected_job else "Belum memilih karir")

    st.sidebar.subheader("Karakteristik")
    if user_traits:
        for trait in user_traits:
            st.sidebar.write(f"• {trait}")
    else:
        st.sidebar.write("Belum ada karakteristik yang dipilih")

    st.sidebar.subheader("Pendidikan")
    st.sidebar.write(education_level if education_level else "Belum memilih pendidikan")

    st.sidebar.subheader("Ekspektasi Gaji")
    if selected_job:
        potential_salary = expert_system.calculate_salary_potential(selected_job, experience_years)
        st.sidebar.write(f"Proyeksi berdasarkan pengalaman: Rp {potential_salary[0]/1000000:.0f} - {potential_salary[1]/1000000:.0f} juta/tahun")

    st.sidebar.subheader("Pengalaman")
    st.sidebar.write(f"{experience_years} tahun")

def render_analysis_results(expert_system, analysis):
    st.markdown("## Analisa Kecocokan Karir")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Nilai Kecocokan", f"{analysis['overall_score']:.1f}%")
    with col2:
        st.metric("Kecocokan Karakteristik", f"{analysis['subscores']['trait_score']:.1f}%")
    with col3:
        st.metric("Kecocokan Pendidikan", f"{analysis['subscores']['education_score']:.1f}%")

    st.markdown("### Detail Analisis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.pyplot(create_radar_chart(analysis))
    
    with col2:
        st.markdown("#### Strengths & Gaps")
        if analysis['matching_traits']:
            st.success("Karakteristik Yang Sesuai: " + ", ".join(analysis['matching_traits']))
        if analysis['missing_traits']:
            st.warning("Lingkup Pengembangan: " + ", ".join(analysis['missing_traits']))
        if analysis['education_gap']:
            st.info(f"Kesenjangan Pendidikan: {analysis['education_gap']} direkomendasikan")
    
    render_career_prospects(analysis)

def render_career_prospects(analysis):
    st.markdown("### Prospek Karir")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Rekomendasi Sertifikasi")
        for cert in analysis['recommended_certifications']:
            st.write(f"• {cert}")
    
    with col2:
        st.markdown("#### Prospek Karir")
        for position in analysis['career_growth']:
            st.write(f"📈 {position}")