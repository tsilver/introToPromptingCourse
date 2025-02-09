import streamlit as st
from utils.navigation import handle_navigation, scroll_to_top
from datetime import datetime
import uuid
from utils.teacher_client import TeacherClient

def show_course_certificate():
    # Generate unique certificate ID if not already exists
    if 'certificate_id' not in st.session_state:
        st.session_state.certificate_id = str(uuid.uuid4())
    if 'certificate_date' not in st.session_state:
        st.session_state.certificate_date = datetime.now().strftime("%B %d, %Y")

    # Certificate Container with border and styling
    st.markdown("""
        <style>
            .main {
                padding: 2rem;
                border: 2px solid #1f77b4;
                border-radius: 10px;
                background-color: white;
                margin: 1rem 0;
            }
            .centered {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="main">', unsafe_allow_html=True)
        
        # Header
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.title("🎓 Certificate of Completion")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Logo and Title
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            # Logo would go here
            st.markdown("## AIxponential")
            st.markdown("### This is to certify that")
            st.markdown("# [Student Name]")
            st.markdown("### has successfully completed the")
            st.markdown("## AI Prompting Mastery Course")
        
        # Competencies
        st.markdown("### Demonstrated Proficiency in:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Fundamental Prompt Engineering
            - Basic prompting concepts
            - Context and constraints
            - Effective communication
            
            #### Advanced AI Interaction
            - Few-shot prompting
            - Role-based techniques
            - Structured outputs
            """)
        
        with col2:
            st.markdown("""
            #### Ethical AI Usage
            - Bias detection
            - Responsible implementation
            - Privacy considerations
            
            #### Practical Applications
            - Real-world scenarios
            - Project development
            - Best practices
            """)
        
        # Certificate Details
        st.divider()
        detail_col1, detail_col2 = st.columns(2)
        
        with detail_col1:
            st.markdown(f"**Issue Date:** {st.session_state.certificate_date}")
        
        with detail_col2:
            st.markdown(f"**Certificate ID:** {st.session_state.certificate_id}")
        
        # Signature
        st.divider()
        sig_col1, sig_col2, sig_col3 = st.columns([1,2,1])
        
        with sig_col2:
            st.markdown("___________________")
            st.markdown("""
            **Tom Silverstrim**  
            Founder  
            AIxponential
            """)
        
        # Verification Text
        st.divider()
        st.caption("""
        This certificate verifies completion of the AIxponential AI Prompting Mastery Course,
        a comprehensive program in artificial intelligence interaction and prompt engineering.
        The holder has demonstrated competency in AI communication, ethical considerations,
        and practical application of advanced prompting techniques.
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Navigation and Download Options
    st.divider()
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Back to Course Completion", 
                 on_click=handle_navigation,
                 args=("course_completion",),
                 use_container_width=True)
    
    with col3:
        st.download_button(
            label="Download Certificate 📥",
            data="Certificate PDF content would go here",
            file_name=f"AIxponential_Certificate_{st.session_state.certificate_id}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_course_certificate() 