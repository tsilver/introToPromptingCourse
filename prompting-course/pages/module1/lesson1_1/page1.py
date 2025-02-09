import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_1_1_page1():
    st.title("Lesson 1.1: Introduction to AI and Prompts")
    
    # Introduction section
    st.markdown("""
    ### What is AI?
    
    Artificial Intelligence (AI) refers to computer systems that can perform tasks typically requiring 
    human intelligence. Modern AI language models, like the one you're learning to work with, can:
    
    - Understand and generate human language
    - Answer questions and provide explanations
    - Help with writing and analysis
    - Engage in back-and-forth conversations
    
    However, AI also has important limitations. It:
    - Doesn't truly "understand" like humans do
    - Can make mistakes or provide incorrect information
    - May exhibit biases from its training data
    - Cannot access real-time information
    """)

    # Interactive Example
    st.markdown("### Let's Try It Out!")
    
    st.info("""
    👉 Let's ask the AI a simple question to see how it responds. 
    Watch how it processes our question and provides an answer.
    """)

    example_prompt = "What is artificial intelligence in simple terms?"
    
    st.markdown("**Example Question:**")
    st.code(example_prompt, language="text")
    
    if st.button("Ask the AI", key="first_interaction"):
        try:
            with st.spinner("Getting response from AI..."):
                response = client.send_prompt(example_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                st.success("""
                Notice how the AI provided an explanation in clear, simple terms. 
                This is because we asked for "simple terms" in our prompt!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Reflection section
    st.markdown("### Key Points to Remember")
    st.markdown("""
    - AI is a tool that can understand and respond to human language
    - It works by processing your input (prompt) and generating appropriate responses
    - The quality of the response depends on how well you communicate with it
    - Always verify important information from AI responses
    """)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module1_intro",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module1/lesson1_1/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_1_1_page1() 