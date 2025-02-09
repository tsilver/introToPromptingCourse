import streamlit as st
from utils.navigation import init_navigation, navigate_to, get_current_page, handle_navigation, check_navigation_rerun, scroll_to_top

# Configure the Streamlit page settings - MUST BE FIRST
st.set_page_config(
    page_title="Interactive Prompting Guide",
    page_icon="💭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add scroll to top functionality
scroll_to_top()

# At the top of the file, after page config
if 'scroll_to_top' in st.session_state and st.session_state.scroll_to_top:
    st.markdown("""
        <script>
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        </script>
    """, unsafe_allow_html=True)

from pages.module1_intro import show_module1_intro
from pages.module1.lesson1_1.page1 import show_lesson_1_1_page1
from pages.module1.lesson1_1.page2 import show_lesson_1_1_page2
from pages.module1.lesson1_2.page1 import show_lesson_1_2_page1
from pages.module1.lesson1_3.page1 import show_lesson_1_3_page1
from pages.module1.lesson1_4.page1 import show_lesson_1_4_page1
from pages.module2_intro import show_module2_intro
from pages.module2.lesson2_1.page1 import show_lesson_2_1_page1
from pages.module2.lesson2_1.page2 import show_lesson_2_1_page2
from pages.module2.lesson2_2.page1 import show_lesson_2_2_page1
from pages.module2.lesson2_2.page2 import show_lesson_2_2_page2
from pages.module2.lesson2_3.page1 import show_lesson_2_3_page1
from pages.module2.lesson2_3.page2 import show_lesson_2_3_page2
from pages.module2.lesson2_4.page1 import show_lesson_2_4_page1
from pages.module2.lesson2_4.page2 import show_lesson_2_4_page2
from pages.module2.lesson2_5.page1 import show_lesson_2_5_page1
from pages.module3_intro import show_module3_intro
from pages.module3.lesson3_1.page1 import show_lesson_3_1_page1
from pages.module3.lesson3_1.page2 import show_lesson_3_1_page2
from pages.module3.lesson3_2.page1 import show_lesson_3_2_page1
from pages.module3.lesson3_2.page2 import show_lesson_3_2_page2
from pages.module3.lesson3_3.page1 import show_lesson_3_3_page1
from pages.module3.lesson3_3.page2 import show_lesson_3_3_page2
from pages.module3.lesson3_4.page1 import show_lesson_3_4_page1
from pages.module3.lesson3_5.page1 import show_lesson_3_5_page1
from pages.course_completion import show_course_completion
from pages.comprehensive_analytics import show_comprehensive_analytics
from pages.course_certificate import show_course_certificate

# Initialize navigation
init_navigation()

# Set up session state for tracking progress
if 'current_module' not in st.session_state:
    st.session_state.current_module = 1
if 'show_content' not in st.session_state:
    st.session_state.show_content = True

# Get current page
current_page = get_current_page()

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    st.markdown("""
    - 🏠 Home
    - 📚 Course Modules
    - ℹ️ About
    """)

def handle_start_course():
    navigate_to("module1_intro")

def show_home_page():
    # Hero section with eye-catching title
    st.title("🚀 Master the Art of AI Prompting")
    
    st.markdown("""
    ### Unlock the Power of AI Through Better Prompts
    
    Welcome to your journey into the fascinating world of AI prompting! This interactive course 
    will teach you how to effectively communicate with AI language models, unlocking their full 
    potential for your learning, creativity, and problem-solving needs.
    """)

    # Create two columns for the call-to-action section
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("### Ready to Begin Your Journey?")
        if st.button(
            "🚀 Start Learning Now!",
            on_click=handle_start_course,
            use_container_width=True
        ):
            st.experimental_rerun()
    
    st.markdown("---")

    st.markdown("""
    #### What You'll Learn:
    
    **📘 Module 1: Fundamentals of Prompting**
    - Understanding AI and prompts
    - Adding constraints and context
    - Asking for explanations
    - Mastering question-answering conversations
    
    **🎯 Module 2: Advanced Techniques**
    - Few-shot prompting with examples
    - Persona prompting for style
    - Structured output formatting
    - Iterative prompt refinement
    
    **🤔 Module 3: Critical Thinking & Ethics**
    - Identifying AI biases
    - Spotting AI hallucinations
    - Using AI responsibly
    - Ethical considerations
    
    #### Why Take This Course?
    
    - 🎓 **Learn by Doing**: Hands-on exercises and real-time feedback
    - 🔄 **Interactive Practice**: Experiment with different prompting techniques
    - 🤝 **Collaborative Learning**: Work with peers on engaging exercises
    - 🎯 **Practical Skills**: Apply what you learn to real-world scenarios
    
    #### Who Is This For?
    
    Whether you're new to AI or looking to improve your skills, this course is designed for anyone who wants to:
    - Write clearer, more effective prompts
    - Get more accurate and useful responses from AI
    - Think critically about AI interactions
    - Use AI tools responsibly and ethically
    """)

    # Additional information section
    st.markdown("---")
    
    # Course features in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 Interactive Learning
        - Real-time feedback
        - Hands-on exercises
        - Progress tracking
        """)
    
    with col2:
        st.markdown("""
        ### 🤝 Collaborative Features
        - Partner exercises
        - Group discussions
        - Peer learning
        """)
    
    with col3:
        st.markdown("""
        ### 📈 Skill Development
        - Progressive difficulty
        - Practical applications
        - Real-world projects
        """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and ❤️*")

# Note: Future development will include:
# - Multiple pages in the 'pages' directory
# - Navigation system between lessons
# - Interactive exercises
# - Progress tracking
# - Dynamic content loading from YAML files

# Display the appropriate page based on current_page
if current_page == "home":
    show_home_page()
elif current_page == "module1_intro":
    show_module1_intro()
elif current_page == "module1/lesson1_1/page1":
    show_lesson_1_1_page1()
elif current_page == "module1/lesson1_1/page2":
    show_lesson_1_1_page2()
elif current_page == "module1/lesson1_2/page1":
    show_lesson_1_2_page1()
elif current_page == "module1/lesson1_3/page1":
    show_lesson_1_3_page1()
elif current_page == "module1/lesson1_4/page1":
    show_lesson_1_4_page1()
elif current_page == "module2_intro":
    show_module2_intro()
elif current_page == "module2/lesson2_1/page1":
    show_lesson_2_1_page1()
elif current_page == "module2/lesson2_1/page2":
    show_lesson_2_1_page2()
elif current_page == "module2/lesson2_2/page1":
    show_lesson_2_2_page1()
elif current_page == "module2/lesson2_2/page2":
    show_lesson_2_2_page2()
elif current_page == "module2/lesson2_3/page1":
    show_lesson_2_3_page1()
elif current_page == "module2/lesson2_3/page2":
    show_lesson_2_3_page2()
elif current_page == "module2/lesson2_4/page1":
    show_lesson_2_4_page1()
elif current_page == "module2/lesson2_4/page2":
    show_lesson_2_4_page2()
elif current_page == "module2/lesson2_5/page1":
    show_lesson_2_5_page1()
elif current_page == "module3_intro":
    show_module3_intro()
elif current_page == "module3/lesson3_1/page1":
    show_lesson_3_1_page1()
elif current_page == "module3/lesson3_1/page2":
    show_lesson_3_1_page2()
elif current_page == "module3/lesson3_2/page1":
    show_lesson_3_2_page1()
elif current_page == "module3/lesson3_2/page2":
    show_lesson_3_2_page2()
elif current_page == "module3/lesson3_3/page1":
    show_lesson_3_3_page1()
elif current_page == "module3/lesson3_3/page2":
    show_lesson_3_3_page2()
elif current_page == "module3/lesson3_4/page1":
    show_lesson_3_4_page1()
elif current_page == "module3/lesson3_4/page2":
    show_lesson_3_4_page2()
elif current_page == "module3/lesson3_5/page1":
    show_lesson_3_5_page1()
elif current_page == "module3/lesson3_5/page2":
    show_lesson_3_5_page2()
elif current_page == "course_completion":
    show_course_completion()
elif current_page == "comprehensive_analytics":
    show_comprehensive_analytics()
elif current_page == "course_certificate":
    show_course_certificate()
else:
    st.error(f"Page not found: {current_page}")
    st.button("Return Home", 
             on_click=handle_navigation,
             args=("home",))

# Debug info
st.sidebar.markdown("---")
st.sidebar.write("Debug Info:")
st.sidebar.write(f"Current Page: {current_page}")
st.sidebar.write(f"Query Params: {dict(st.query_params)}")
# Filter out internal Streamlit widget IDs from session state
safe_state = {k: v for k, v in st.session_state.items() if not k.startswith("$$")}
st.sidebar.write(f"Session State: {safe_state}")

# Add this at the end of your app.py
check_navigation_rerun() 