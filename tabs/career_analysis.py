import streamlit as st
from typing import Union, List, Dict
from dataclasses import dataclass
from enum import Enum
from visualization import create_radar_chart

class ErrorSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

@dataclass
class SystemError:
    message: str
    details: Union[str, List[str], Dict[str, str]] = None
    severity: ErrorSeverity = ErrorSeverity.ERROR

def display_error(error: SystemError):
    """Display formatted error messages using Streamlit components."""
    if error.severity == ErrorSeverity.ERROR:
        container = st.error
        icon = "🚫"
    elif error.severity == ErrorSeverity.WARNING:
        container = st.warning
        icon = "⚠️"
    else:
        container = st.info
        icon = "ℹ️"
    
    with container(f"{icon} {error.message}"):
        if error.details:
            if isinstance(error.details, str):
                st.markdown(f"```\n{error.details}\n```")
            elif isinstance(error.details, list):
                for detail in error.details:
                    st.markdown(f"- {detail}")
            elif isinstance(error.details, dict):
                for key, value in error.details.items():
                    st.markdown(f"**{key}:** {value}")

def check_dependencies():
    """Check for required dependencies and their versions."""
    try:
        import pkg_resources
        
        required = {
            'streamlit': '>=1.0.0',
            'matplotlib': '>=3.0.0',
            'pandas': '>=1.0.0'
        }
        
        issues = []
        for package, version in required.items():
            try:
                pkg_resources.require(f"{package}{version}")
            except pkg_resources.VersionConflict as e:
                issues.append(f"{package}: {str(e)}")
        
        if issues:
            display_error(SystemError(
                message="Dependency Version Conflicts Detected",
                severity=ErrorSeverity.WARNING,
                details=issues
            ))
            
    except Exception as e:
        display_error(SystemError(
            message="Failed to verify dependencies",
            details=str(e)
        ))

def render_career_analysis(expert_system):
    try:
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
            with st.spinner("Menganalisis kesesuaian karir..."):
                analysis_results = expert_system.create_detailed_analysis(
                    selected_job, user_traits, education_level, experience_years
                )
                
                if not analysis_results:
                    display_error(SystemError(
                        message="Warning: Analysis Incomplete",
                        severity=ErrorSeverity.WARNING,
                        details="Unable to generate complete analysis. Some data may be missing."
                    ))
                    return
                
                st.session_state['analysis_results'] = analysis_results

        if 'analysis_results' in st.session_state:
            render_analysis_results(expert_system, st.session_state['analysis_results'])

    except AttributeError as e:
        display_error(SystemError(
            message="Error: Expert System Configuration Issue",
            details={
                "Type": "Configuration Error",
                "Cause": "Invalid expert system rules or missing attributes",
                "Solution": "Please check expert system initialization"
            }
        ))
        return
    
    except ValueError as e:
        display_error(SystemError(
            message="Error: Invalid Input Values",
            details=str(e)
        ))
        return
    
    except Exception as e:
        display_error(SystemError(
            message="An unexpected error occurred",
            details={
                "Error Type": type(e).__name__,
                "Details": str(e),
                "Location": "Career Analysis Module"
            }
        ))
        return

def render_sidebar(expert_system, selected_job, user_traits, education_level, experience_years):
    try:
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

    except Exception as e:
        display_error(SystemError(
            message="Error: Sidebar Rendering Failed",
            details=str(e)
        ))

def render_analysis_results(expert_system, analysis):
    try:
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

    except Exception as e:
        display_error(SystemError(
            message="Error: Failed to Render Analysis Results",
            details={
                "Error": str(e),
                "Analysis Data": "Check analysis data structure and completeness"
            }
        ))

def render_career_prospects(analysis):
    try:
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

    except Exception as e:
        display_error(SystemError(
            message="Error: Failed to Render Career Prospects",
            details={
                "Error": str(e),
                "Section": "Career Prospects",
                "Analysis Data": "Check career prospects data structure"
            }
        ))

if __name__ == "__main__":
    check_dependencies()