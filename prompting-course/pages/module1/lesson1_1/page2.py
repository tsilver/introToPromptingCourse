import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_1_1_page2():
    st.title("Lesson 1.1: Components of an Effective Prompt")
    
    # Introduction to prompt components
    st.markdown("""
    ### Understanding Prompt Components
    
    An effective prompt typically consists of several key components that help guide the AI's response:
    
    1. **Clear Instruction**: What you want the AI to do
    2. **Context**: Background information or constraints
    3. **Format**: How you want the response structured
    4. **Examples**: (Optional) Demonstrations of desired output
    
    Let's explore each component through examples.
    """)

    # Interactive Example 1
    st.markdown("### 👉 Example 1: Basic vs. Detailed Prompt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Prompt:**")
        st.code("Explain photosynthesis.", language="text")
        
    with col2:
        st.markdown("**Detailed Prompt:**")
        st.code("""Explain photosynthesis in simple terms, focusing on:
1. What it is
2. Why it's important
3. Basic steps involved

Keep the explanation suitable for a middle school student.""", language="text")

    # Try it out section
    st.markdown("### Let's Try It Out!")
    
    st.info("""
    👉 Let's see how the AI responds to both prompts. Notice how the detailed prompt 
    provides more guidance and structure for the response.
    """)

    if st.button("Compare Responses", key="compare_prompts"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt("Explain photosynthesis.")
                detailed_response = client.send_prompt("""Explain photosynthesis in simple terms, focusing on:
1. What it is
2. Why it's important
3. Basic steps involved

Keep the explanation suitable for a middle school student.""")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Response to Basic Prompt:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**Response to Detailed Prompt:**")
                    st.markdown(detailed_response['response'])
                
                st.success("""
                Notice how the detailed prompt resulted in:
                - More structured information
                - Age-appropriate language
                - Clear organization of concepts
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Try improving this basic prompt by adding components we discussed:
    
    **Basic prompt:** *"Write about climate change."*
    
    Use the text area below to write your improved version. Consider adding:
    - Specific instructions
    - Context or constraints
    - Desired format
    - Target audience
    """)

    user_prompt = st.text_area(
        "Your improved prompt:",
        height=150,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on prompt structure
                st.info("""
                💡 **Prompt Analysis:**
                - Did your prompt specify clear instructions?
                - Did you include context or constraints?
                - Did you specify a format or structure?
                - Was the target audience clear?
                
                Compare your response with the basic prompt to see the improvements!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Key takeaways
    st.markdown("### 🔑 Key Takeaways")
    st.markdown("""
    - Clear instructions lead to better responses
    - Context helps AI understand your needs
    - Formatting guidance structures the output
    - Examples can clarify expectations
    """)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module1/lesson1_1/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Begin Lesson 1.2 →", 
                 on_click=handle_navigation,
                 args=("module1/lesson1_2/page1",),
                 use_container_width=True)
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_1_1_page2() 