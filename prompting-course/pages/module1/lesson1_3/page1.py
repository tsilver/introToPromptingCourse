import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_1_3_page1():
    st.title("Lesson 1.3: Asking for Explanations")
    
    # Introduction
    st.markdown("""
    ### Getting Clear Explanations from AI
    
    In this lesson, you'll learn techniques for getting AI to:
    - Explain its reasoning step by step
    - Break down complex concepts
    - Show its work and thought process
    - Provide clear, verifiable explanations
    
    Understanding how to ask for explanations is crucial for learning from AI and verifying its responses.
    """)

    # Key Techniques
    st.markdown("""
    ### Techniques for Requesting Explanations
    
    1. **Ask for Step-by-Step Breakdowns**
       - Makes complex processes clearer
       - Helps identify potential issues
       - Easier to follow and verify
    
    2. **Request Multiple Perspectives**
       - Gets more comprehensive understanding
       - Reveals different approaches
       - Helps avoid bias
    
    3. **Use "Chain of Thought" Prompting**
       - Shows AI's reasoning process
       - Makes assumptions explicit
       - Helps catch logical errors
    """)

    # Interactive Example
    st.markdown("### 👉 Let's Compare Approaches")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Question:**")
        st.code("Why is the sky blue?", language="text")
        
    with col2:
        st.markdown("**Explanation-Focused Question:**")
        st.code("""Explain why the sky appears blue, with these requirements:
1. Break down the scientific process step by step
2. Use simple analogies to illustrate key concepts
3. Explain how we can verify this explanation
4. Address common misconceptions

Keep explanations accessible to a high school student.""", language="text")

    # Try it out section
    st.info("""
    👉 Let's see how the AI's explanations differ between these approaches. Notice how the 
    structured request leads to a more thorough and verifiable explanation.
    """)

    if st.button("Compare Explanations", key="compare_explanations"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt("Why is the sky blue?")
                detailed_response = client.send_prompt("""Explain why the sky appears blue, with these requirements:
1. Break down the scientific process step by step
2. Use simple analogies to illustrate key concepts
3. Explain how we can verify this explanation
4. Address common misconceptions

Keep explanations accessible to a high school student.""")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Basic Response:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**Detailed Explanation:**")
                    st.markdown(detailed_response['response'])
                
                st.success("""
                Notice how the detailed request resulted in:
                - Clear step-by-step explanation
                - Helpful analogies
                - Verifiable claims
                - Addressed misconceptions
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Transform this basic question into an explanation-focused prompt:
    
    **Basic question:** *"How does a computer work?"*
    
    Write a prompt that asks for:
    - Step-by-step explanation
    - Clear analogies
    - Verifiable details
    - Common misconception corrections
    """)

    user_prompt = st.text_area(
        "Your explanation-focused prompt:",
        height=150,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on explanation elements
                st.info("""
                💡 **Explanation Analysis:**
                - Did you request step-by-step breakdown?
                - Did you ask for analogies or examples?
                - Did you request verification methods?
                - Did you address misconceptions?
                
                Compare the detail and clarity with a basic response!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Back to Module 1", 
                 on_click=handle_navigation,
                 args=("module1_intro",),
                 use_container_width=True)
    
    with col3:
        st.button("Begin Lesson 1.4 →", 
                 on_click=handle_navigation,
                 args=("module1/lesson1_4/page1",),
                 use_container_width=True)
    scroll_to_top()
    
if __name__ == "__main__":
    show_lesson_1_3_page1() 