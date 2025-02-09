import streamlit as st
from utils.navigation import handle_navigation, scroll_to_top

def show_module3_intro():
    st.title("Module 3: Critical Thinking & AI Ethics")
    
    # Introduction
    st.markdown("""
    ### Developing Critical AI Interaction Skills
    
    Welcome to Module 3! In this module, you'll learn essential skills for:
    - Evaluating AI responses critically
    - Identifying and addressing biases
    - Detecting AI hallucinations
    - Making ethical AI decisions
    
    This knowledge will help you use AI more responsibly and effectively.
    """)

    # Module Overview
    st.markdown("""
    ### What You'll Learn
    
    **Lesson 3.1: Identifying AI Biases**
    - Understanding types of AI bias
    - Detecting bias in responses
    - Writing bias-aware prompts
    - Mitigating bias through prompting
    
    **Lesson 3.2: Spotting AI Hallucinations**
    - Recognizing false information
    - Fact-checking strategies
    - Verification techniques
    - Reducing hallucinations
    
    **Lesson 3.3: Responsible AI Usage**
    - Ethical considerations
    - Privacy concerns
    - Data sensitivity
    - Best practices
    
    **Lesson 3.4: AI Ethics in Practice**
    - Real-world applications
    - Ethical decision-making
    - Impact assessment
    - Future considerations
    """)

    # Prerequisites
    st.info("""
    **Prerequisites:**
    - Completion of Module 1 (Fundamentals)
    - Completion of Module 2 (Advanced Techniques)
    - Basic understanding of AI capabilities
    - Familiarity with prompt engineering
    """)

    # Module Structure
    st.markdown("""
    ### Module Structure
    
    1. **Theoretical Foundation**
       - Understanding AI limitations
       - Ethical frameworks
       - Critical thinking principles
    
    2. **Practical Applications**
       - Real-world examples
       - Interactive exercises
       - Case studies
    
    3. **Hands-on Practice**
       - Bias detection exercises
       - Hallucination identification
       - Ethical decision-making scenarios
    
    4. **Assessment & Reflection**
       - Knowledge checks
       - Discussion questions
       - Self-evaluation
    """)

    # Learning Objectives
    st.markdown("""
    ### Learning Objectives
    
    By the end of this module, you'll be able to:
    - ✅ Identify and address AI biases
    - ✅ Detect and verify AI hallucinations
    - ✅ Make informed ethical decisions
    - ✅ Apply responsible AI practices
    - ✅ Evaluate AI responses critically
    """)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Back to Module 2", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_5/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Begin Lesson →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_1/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_module3_intro() 