import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_1_4_page1():
    st.title("Lesson 1.4: Question Answering and Conversation")
    
    # Introduction
    st.markdown("""
    ### Mastering AI Conversations
    
    In this lesson, you'll learn how to:
    - Structure effective questions for detailed answers
    - Maintain context in multi-turn conversations
    - Follow up on AI responses effectively
    - Guide conversations toward desired outcomes
    
    Understanding conversational prompting is key to getting the most out of AI interactions.
    """)

    # Key Principles
    st.markdown("""
    ### Core Principles of AI Conversation
    
    1. **Question Clarity**
       - Be specific and precise
       - One question at a time
       - Clear scope and constraints
    
    2. **Context Management**
       - Reference previous responses
       - Build on established information
       - Maintain conversation thread
    
    3. **Follow-up Techniques**
       - Ask for clarification
       - Request examples
       - Explore alternatives
       - Deepen understanding
    """)

    # Interactive Example
    st.markdown("### 👉 Let's See Conversation in Action")
    
    st.markdown("""
    We'll explore a conversation about climate change solutions. Notice how each follow-up 
    question builds on previous responses and maintains context.
    """)

    conversation_prompts = [
        "What are the main approaches to addressing climate change?",
        """Based on your previous response about climate change solutions, 
        explain in detail how renewable energy specifically helps with:
        1. Reducing emissions
        2. Economic benefits
        3. Implementation challenges""",
        """Regarding the implementation challenges you mentioned for renewable energy,
        what are some successful strategies that countries have used to overcome them?
        Include specific examples and results."""
    ]

    if st.button("Start Conversation", key="start_conversation"):
        try:
            for i, prompt in enumerate(conversation_prompts, 1):
                st.markdown(f"**Question {i}:**")
                st.code(prompt, language="text")
                
                with st.spinner(f"Getting response {i}..."):
                    response = client.send_prompt(prompt)
                    st.markdown(f"**AI Response {i}:**")
                    st.markdown(response['response'])
                
                if i < len(conversation_prompts):
                    st.markdown("👇 **Notice how the next question builds on this response:**")
            
            st.success("""
            Notice how the conversation:
            - Maintains context throughout
            - Builds on previous responses
            - Gets increasingly specific
            - Explores different aspects systematically
            """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a series of connected questions about artificial intelligence, starting with 
    this basic question:
    
    **Initial question:** *"What is machine learning?"*
    
    Write 2-3 follow-up questions that:
    - Build on previous information
    - Maintain clear context
    - Get increasingly specific
    - Explore practical applications
    """)

    user_prompts = []
    for i in range(3):
        prompt = st.text_area(
            f"Question {i+1}:",
            height=100,
            key=f"question_{i}"
        )
        if prompt:
            user_prompts.append(prompt)

    if st.button("Test Your Conversation", key="test_conversation") and user_prompts:
        try:
            for i, prompt in enumerate(user_prompts, 1):
                with st.spinner(f"Getting response {i}..."):
                    response = client.send_prompt(prompt)
                    st.markdown(f"**Response to Question {i}:**")
                    st.markdown(response['response'])
                
                # Provide feedback after each response
                st.info(f"""
                💡 **Question {i} Analysis:**
                - How well did it build on previous information?
                - Was the context clear?
                - Did it get more specific?
                - Did it explore practical aspects?
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
        st.button("Begin Module 2 →", 
                 on_click=handle_navigation,
                 args=("module2_intro",),
                 use_container_width=True)
    scroll_to_top()
                
if __name__ == "__main__":
    show_lesson_1_4_page1() 