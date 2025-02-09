import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_1_page1():
    st.title("Lesson 3.1: Identifying AI Biases")
    
    # Introduction
    st.markdown("""
    ### Understanding and Addressing AI Bias
    
    In this lesson, you'll learn how to:
    - Recognize different types of AI bias
    - Detect bias in AI responses
    - Write bias-aware prompts
    - Mitigate bias through careful prompting
    
    Understanding bias is crucial for responsible AI usage.
    """)

    # Key Concepts
    st.markdown("""
    ### Types of AI Bias
    
    1. **Training Data Bias**
       - Historical data prejudices
       - Underrepresented groups
       - Cultural assumptions
       - Geographic skew
    
    2. **Language Bias**
       - Gender stereotypes
       - Cultural stereotypes
       - Age-related assumptions
       - Socioeconomic prejudices
    
    3. **Algorithmic Bias**
       - Pattern amplification
       - Statistical skew
       - Sampling bias
       - Confirmation bias
    """)

    # Interactive Example
    st.markdown("### 👉 Let's Identify Bias in Action")
    
    st.markdown("Examine these prompts and responses for potential biases:")
    
    examples = [
        {
            "prompt": "Describe a typical doctor's day at work.",
            "biased_response": "He starts his morning rounds at 7 AM, checking on his patients...",
            "issue": "Gender bias - assumes doctor is male",
            "improved_prompt": """Describe a typical doctor's day at work. 
Be mindful of gender representation and avoid assumptions about the doctor's identity."""
        },
        {
            "prompt": "What makes a good leader?",
            "biased_response": "A good leader is assertive, decisive, and commands respect from his subordinates...",
            "issue": "Gender and cultural bias - stereotypical masculine traits",
            "improved_prompt": """Describe effective leadership qualities that are:
- Applicable across different cultures
- Not limited by gender stereotypes
- Based on measurable outcomes
- Inclusive of diverse leadership styles"""
        }
    ]

    for i, example in enumerate(examples, 1):
        st.markdown(f"**Example {i}:**")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Original Prompt:*")
            st.code(example["prompt"], language="text")
            st.markdown("*Potentially Biased Response:*")
            st.markdown(example["biased_response"])
            st.error(f"Issue: {example['issue']}")
        
        with col2:
            st.markdown("*Improved Prompt:*")
            st.code(example["improved_prompt"], language="text")
            
            if st.button(f"Test Improved Prompt {i}", key=f"test_improved_{i}"):
                try:
                    with st.spinner("Getting unbiased response..."):
                        response = client.send_prompt(example["improved_prompt"])
                        st.markdown("*Improved Response:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how the improved prompt:
                        - Avoids stereotypical assumptions
                        - Encourages inclusive language
                        - Considers multiple perspectives
                        - Focuses on objective criteria
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Identify and correct potential biases in this prompt:
    
    *"Write a story about a successful entrepreneur who built a tech company from scratch."*
    
    Consider:
    1. **Representation**
       - Gender assumptions
       - Cultural perspectives
       - Age considerations
    
    2. **Language**
       - Inclusive terminology
       - Neutral descriptions
       - Balanced examples
    
    3. **Context**
       - Global perspectives
       - Diverse experiences
       - Various paths to success
    """)

    user_prompt = st.text_area(
        "Your bias-aware prompt:",
        height=200,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on bias awareness
                st.info("""
                💡 **Bias Analysis:**
                - How well does it avoid stereotypes?
                - Is the language inclusive?
                - Are different perspectives represented?
                - What assumptions might still exist?
                
                Review the response carefully for subtle biases!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3_intro",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_1/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_1_page1() 