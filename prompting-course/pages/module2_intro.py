import streamlit as st
from utils.navigation import handle_navigation, scroll_to_top

def show_module2_intro():
    st.title("📘 Module 2: Advanced Prompting Techniques")
    
    st.markdown("""
    ### Welcome to Advanced Prompting!
    
    In this module, you'll learn sophisticated techniques to enhance your AI interactions:
    
    ### What You'll Learn
    
    **Lesson 2.1: Few-Shot Prompting with Examples**
    - Understanding few-shot learning
    - Creating effective examples
    - Pattern matching and consistency
    - When to use example-based prompts
    
    **Lesson 2.2: Persona and Role-Based Prompting**
    - Defining AI personas
    - Role-specific instructions
    - Style and tone control
    - Expert perspective prompting
    
    **Lesson 2.3: Structured Output Formatting**
    - JSON and XML outputs
    - Table and list formatting
    - Custom data structures
    - Format validation techniques
    
    **Lesson 2.4: Iterative Prompt Refinement**
    - Testing and evaluation
    - Error analysis
    - Systematic improvements
    - Optimization strategies
    """)
    
    # Progress tracking
    if 'module2_progress' not in st.session_state:
        st.session_state.module2_progress = 0
    
    # Create columns for the action buttons
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("### Ready to Dive Deeper?")
        st.button(
            "Begin Lesson 2.1: Few-Shot Prompting",
            on_click=handle_navigation,
            args=("module2/lesson2_1/page1",),
            key="start_lesson_2_1",
            use_container_width=True
        )

    # Module prerequisites and preparation
    st.markdown("---")
    st.markdown("""
    ### Before You Begin
    
    **Prerequisites:**
    - Completion of Module 1
    - Basic understanding of prompt components
    - Familiarity with AI interactions
    
    **Module Structure:**
    1. 📖 Advanced concepts introduction
    2. 🎯 Technique demonstrations
    3. ✍️ Complex exercises
    4. 🤝 Real-world applications
    5. 📝 Technique comparison and analysis
    
    **Time Commitment:**
    - Total Module Duration: ~3 hours
    - Individual Lessons: 35-45 minutes each
    - Practice Exercises: 15-20 minutes each
    """)
    
    # Tips for success
    st.info("""
    **💡 Tips for Success**
    
    - Practice each technique multiple times
    - Compare results between different approaches
    - Document your most effective prompts
    - Experiment with combining techniques
    - Share and discuss results with peers
    """)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Back to Module 1", 
                 on_click=handle_navigation,
                 args=("module1/lesson1_4/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Begin Lesson →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_1/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_module2_intro() 