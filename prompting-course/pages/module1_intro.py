import streamlit as st
from utils.navigation import handle_navigation, scroll_to_top

def handle_lesson_start():
    """Navigate to the first page of Lesson 1.1"""
    handle_navigation("module1/lesson1_1/page1")
    st.rerun()  # Force a rerun after navigation is set up

def show_module1_intro():
    st.title("📘 Module 1: Fundamentals of Prompting")
    
    st.markdown("""
    ### Welcome to Your First Step in AI Prompting!
    
    In this foundational module, you'll learn the essential skills needed to effectively communicate 
    with AI language models. Through a series of interactive lessons, you'll discover how to craft 
    clear, effective prompts that get you the results you need.
    
    ### What You'll Learn
    
    **Lesson 1.1: Introduction to AI and Prompts**
    - Understanding what AI can and cannot do
    - Basic prompt structure and components
    - How AI processes and responds to prompts
    
    **Lesson 1.2: Adding Constraints and Context**
    - Using the PCTF (Persona, Context, Task, Format) framework
    - Setting clear boundaries for AI responses
    - Providing relevant background information
    
    **Lesson 1.3: Asking for Explanations**
    - Techniques for requesting detailed explanations
    - Getting AI to show its reasoning
    - Collaborative exercises with peers
    
    **Lesson 1.4: Question Answering and Conversation**
    - Engaging in effective AI conversations
    - Following up on AI responses
    - Building on previous exchanges
    
    ### Module Structure
    
    Each lesson follows this format:
    1. 📖 Introduction and concepts
    2. 🎯 Guided examples
    3. ✍️ Hands-on practice
    4. 🤝 Interactive exercises
    5. 📝 Reflection and review
    
    ### Time Commitment
    - Total Module Duration: ~2 hours
    - Individual Lessons: 25-30 minutes each
    - Self-paced learning
    """)
    
    # Progress tracking
    if 'module1_progress' not in st.session_state:
        st.session_state.module1_progress = 0
    
    # Navigation buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Back to Home", 
                 on_click=handle_navigation,
                 args=("home",),
                 use_container_width=True)
    
    with col3:
        st.button("Begin Lesson →", 
                 on_click=handle_navigation,
                 args=("module1/lesson1_1/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

    # Module prerequisites and preparation
    st.markdown("---")
    st.markdown("""
    ### Before You Begin
    
    **Prerequisites:**
    - No prior AI experience needed
    - Basic computer skills
    - Curiosity and willingness to learn
    
    **Preparation:**
    - Have a notebook ready for taking notes
    - Set aside uninterrupted time for practice
    - Consider finding a study partner for collaborative exercises
    """)
    
    # Tips for success
    st.info("""
    **💡 Tips for Success**
    
    - Complete all exercises in each lesson
    - Practice with real-world examples
    - Don't rush - take time to understand each concept
    - Participate in collaborative activities
    - Review and reflect on your learning
    """)

if __name__ == "__main__":
    show_module1_intro() 