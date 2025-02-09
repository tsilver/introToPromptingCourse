import streamlit as st
import os
from PIL import Image
import base64

# Configure the Streamlit page settings - MUST BE FIRST
st.set_page_config(
    page_title="Professional AI Prompting Course",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add logo and tagline at the top of every page
logo_path = os.path.join(os.path.dirname(__file__), "images", "shortLogo.png")
if os.path.exists(logo_path):
    # Create columns for logo and tagline
    col1, col2 = st.columns([1, 4])
    with col1:
        # Read the image file and convert to base64
        with open(logo_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode()
        
        st.markdown(
            f'<div style="padding: 10px;">'
            f'<a href="https://aixponential.org" target="_blank">'
            f'<img src="data:image/png;base64,{image_data}" style="max-width: 150px;">'
            f'</a></div>',
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            '<div style="padding: 25px; font-size: 20px; color: #666;">'
            'Empowering a Future Shaped by Knowledge, Truth, and Access'
            '</div>',
            unsafe_allow_html=True
        )

from utils.navigation import init_navigation, navigate_to, get_current_page, handle_navigation
from pages.module1_intro import show_module1_intro
from pages.module1.lesson1_1.page1 import show_lesson_1_1_page1
from pages.module1.lesson1_1.page2 import show_lesson_1_1_page2

# Initialize navigation
init_navigation()

# Get current page
current_page = get_current_page()

# Sidebar navigation
with st.sidebar:
    st.title("Course Navigation")
    st.markdown("""
    - 📱 Dashboard
    - 📚 Course Content
    - 📊 Progress
    - 📝 Notes
    - ⚙️ Settings
    """)

# Set up session state for tracking progress
if 'current_module' not in st.session_state:
    st.session_state.current_module = 1
if 'show_content' not in st.session_state:
    st.session_state.show_content = True

# Development notes
FUTURE_DEVELOPMENT = """
Future Development Roadmap:
- Learning Management System (LMS) integration
- Enterprise customization options
- Analytics dashboard
- Team management features
- API documentation
- Custom module development
"""

def handle_start_course():
    navigate_to("module1_intro")

def show_professional_home():
    # Professional header
    st.title("Professional AI Prompting Mastery")
    
    st.markdown("""
    ### Transform Your AI Interactions with Expert Prompting Techniques
    
    In today's AI-driven workplace, the ability to effectively communicate with AI systems is becoming 
    an essential professional skill. This comprehensive course provides you with the expertise to leverage 
    AI language models for enhanced productivity, problem-solving, and innovation.
    """)

    # Call-to-action in a clean, professional layout
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("### Begin Your Professional Development")
        key = f"start_course_button_{st.session_state.navigation_key}"
        st.button(
            "Enroll Now - Start Learning",
            on_click=handle_start_course,
            key=key,
            use_container_width=True
        )
    
    st.markdown("---")

    # Course overview in a professional format
    st.markdown("""
    ### Professional Curriculum
    
    **Module 1: Essential Foundations**
    - Understanding AI capabilities and limitations
    - Crafting precise, effective prompts
    - Implementing context and constraints
    - Developing systematic questioning techniques
    
    **Module 2: Advanced Implementation**
    - Example-driven prompting methodologies
    - Role-based communication strategies
    - Output format optimization
    - Iterative refinement processes
    
    **Module 3: Professional Ethics & Critical Analysis**
    - Bias identification and mitigation
    - Quality assurance and fact verification
    - Ethical implementation guidelines
    - Risk assessment and management
    
    ### Business Impact
    
    This course enables professionals to:
    - ✓ Increase productivity through efficient AI interaction
    - ✓ Improve decision-making with better AI insights
    - ✓ Reduce errors in AI-generated content
    - ✓ Implement ethical AI usage practices
    - ✓ Drive innovation in AI applications
    
    ### Target Audience
    
    Designed for professionals seeking to:
    - Enhance workplace efficiency through AI tools
    - Develop advanced AI communication skills
    - Implement ethical AI practices
    - Lead AI initiatives in their organization
    """)

    # Professional features section
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Professional Development
        - Industry-standard methodologies
        - Real-world case studies
        - Performance analytics
        - Certification path
        """)
    
    with col2:
        st.markdown("""
        ### Enterprise Features
        - Team collaboration tools
        - Progress monitoring
        - Custom implementation guides
        - Best practice frameworks
        """)
    
    with col3:
        st.markdown("""
        ### Practical Application
        - Industry-specific examples
        - Implementation templates
        - ROI measurement tools
        - Integration strategies
        """)

    # Additional professional benefits
    st.markdown("---")
    st.markdown("""
    ### Professional Benefits
    
    | Skill Development | Career Impact | Organization Benefits |
    |------------------|---------------|----------------------|
    | Advanced AI communication | Career advancement | Improved efficiency |
    | Strategic thinking | Technical leadership | Cost reduction |
    | Problem-solving | Innovation capability | Quality enhancement |
    | Ethical decision-making | Professional credibility | Risk mitigation |
    """)

    # Course statistics in metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Hours of Content", value="40+")
    with col2:
        st.metric(label="Practical Exercises", value="50+")
    with col3:
        st.metric(label="Case Studies", value="25+")
    with col4:
        st.metric(label="Templates", value="30+")

    # Professional footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("© 2024 Professional AI Prompting Course")
    with col2:
        st.markdown("Terms & Conditions | Privacy Policy")
    with col3:
        st.markdown("Enterprise Solutions | Contact")

# Display the appropriate page based on current_page
if current_page == "home":
    show_professional_home()
elif current_page == "module1_intro":
    show_module1_intro()
elif current_page == "module1/lesson1_1/page1":
    show_lesson_1_1_page1()
elif current_page == "module1/lesson1_1/page2":
    show_lesson_1_1_page2()
else:
    st.error(f"Page not found: {current_page}")
    st.button("Return Home", 
             on_click=handle_navigation,
             args=("home",)) 