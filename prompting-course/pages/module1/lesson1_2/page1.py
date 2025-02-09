import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_1_2_page1():
    st.title("Lesson 1.2: Adding Constraints and Context")
    
    # Introduction
    st.markdown("""
    ### Understanding Constraints and Context in Prompts
    
    In this lesson, we'll explore how to make your prompts more effective by adding:
    - Clear constraints to guide the AI's output
    - Relevant context to frame the task
    - Specific requirements for format and style
    
    Using the PCTF framework (Persona, Context, Task, Format), you'll learn to craft prompts that 
    generate more precise and useful responses.
    """)

    # PCTF Framework Explanation
    st.markdown("""
    ### The PCTF Framework
    
    1. **Persona**: Who the AI should act as
    2. **Context**: Background information and situation
    3. **Task**: Specific instructions and goals
    4. **Format**: Desired structure and style of the response
    """)

    # Interactive Example
    st.markdown("### 👉 Let's See It in Action")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Prompt:**")
        st.code("Write about renewable energy.", language="text")
        
    with col2:
        st.markdown("**PCTF-Enhanced Prompt:**")
        st.code("""As an environmental science educator (Persona),
given the increasing focus on climate change solutions (Context),
explain three main types of renewable energy suitable for residential use (Task).
Structure your response with:
- Brief overview of each type
- Installation requirements
- Average cost and savings
- Environmental impact
(Format)""", language="text")

    # Try it out section
    st.info("""
    👉 Let's compare how the AI responds to both prompts. Notice how the PCTF framework 
    helps generate a more focused and useful response.
    """)

    if st.button("Compare Responses", key="compare_prompts"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt("Write about renewable energy.")
                pctf_response = client.send_prompt("""As an environmental science educator,
given the increasing focus on climate change solutions,
explain three main types of renewable energy suitable for residential use.
Structure your response with:
- Brief overview of each type
- Installation requirements
- Average cost and savings
- Environmental impact""")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Basic Response:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**PCTF-Enhanced Response:**")
                    st.markdown(pctf_response['response'])
                
                st.success("""
                Notice how the PCTF-enhanced prompt resulted in:
                - More focused information
                - Better organized content
                - Practical, actionable details
                - Consistent structure
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Transform this basic prompt using the PCTF framework:
    
    **Basic prompt:** *"Explain machine learning."*
    
    Use the text area below to write your enhanced version. Include:
    - A specific persona for the AI
    - Relevant context
    - Clear task requirements
    - Desired response format
    """)

    user_prompt = st.text_area(
        "Your PCTF-enhanced prompt:",
        height=150,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on PCTF elements
                st.info("""
                💡 **PCTF Analysis:**
                - Did you specify a clear persona?
                - Did you provide relevant context?
                - Is the task clearly defined?
                - Did you specify the desired format?
                
                Compare your response with the basic version to see the improvements!
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
        st.button("Begin Lesson 1.3 →",
                 on_click=handle_navigation,
                 args=("module1/lesson1_3/page1",),
                 use_container_width=True)
    scroll_to_top()
    
if __name__ == "__main__":
    show_lesson_1_2_page1() 