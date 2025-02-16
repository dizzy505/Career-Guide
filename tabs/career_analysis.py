import streamlit as st
from typing import Union, List, Dict
from dataclasses import dataclass
from enum import Enum

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

def render_career_analysis(expert_system):
    try:
        col1, col2 = st.columns(2)
        
        with col1:
            selected_job = st.selectbox(
                "Pilih Karir Yang Diinginkan:", 
                sorted(expert_system.rules.keys()), 
                key="selected_job"
            )
            # ... rest of your existing code ...

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

    try:
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

    except Exception as e:
        display_error(SystemError(
            message="Error: Analysis Failed",
            details={
                "Error": str(e),
                "Job": selected_job,
                "Education": education_level
            }
        ))
        return

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