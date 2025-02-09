import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_1_page1():
    st.title("Lesson 2.1: Few-Shot Prompting with Examples")
    
    # Introduction
    st.markdown("""
    ### Learning Through Examples
    
    Few-shot prompting is a powerful technique where you provide examples to guide the AI's responses. 
    In this lesson, you'll learn:
    - How to create effective example sets
    - When to use few-shot prompting
    - Best practices for pattern matching
    - Techniques for maintaining consistency
    """)

    # Key Concepts
    st.markdown("""
    ### Understanding Few-Shot Prompting
    
    Few-shot prompting works by showing the AI examples of:
    1. **Input**: What you might ask
    2. **Output**: How you want it answered
    3. **Pattern**: The consistent structure to follow
    
    This helps the AI understand exactly how you want it to respond to similar questions.
    """)

    # Interactive Example
    st.markdown("### 👉 Let's See Few-Shot Prompting in Action")
    
    st.markdown("Here's an example of classifying customer feedback with and without few-shot examples:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Prompt:**")
        st.code("""Classify this feedback as positive, negative, or neutral:
"The product works fine but shipping took longer than expected."
""", language="text")
        
    with col2:
        st.markdown("**Few-Shot Prompt:**")
        st.code("""Here are some examples of customer feedback classification:

Input: "Love the quality, fast delivery!"
Classification: Positive (Reason: Expresses satisfaction with product and service)

Input: "Item arrived damaged and support was unhelpful"
Classification: Negative (Reason: Product issues and poor service experience)

Input: "Product meets expectations, nothing special"
Classification: Neutral (Reason: Neither particularly positive nor negative)

Now classify this feedback:
"The product works fine but shipping took longer than expected."
""", language="text")

    # Try it out section
    st.info("""
    👉 Let's compare how the AI responds to both approaches. Notice how the few-shot examples 
    guide the AI to provide more structured and consistent responses.
    """)

    if st.button("Compare Responses", key="compare_responses"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt("""Classify this feedback as positive, negative, or neutral:
"The product works fine but shipping took longer than expected."
""")
                few_shot_response = client.send_prompt("""Here are some examples of customer feedback classification:

Input: "Love the quality, fast delivery!"
Classification: Positive (Reason: Expresses satisfaction with product and service)

Input: "Item arrived damaged and support was unhelpful"
Classification: Negative (Reason: Product issues and poor service experience)

Input: "Product meets expectations, nothing special"
Classification: Neutral (Reason: Neither particularly positive nor negative)

Now classify this feedback:
"The product works fine but shipping took longer than expected."
""")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Basic Response:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**Few-Shot Response:**")
                    st.markdown(few_shot_response['response'])
                
                st.success("""
                Notice how the few-shot prompt resulted in:
                - More structured classification
                - Clearer reasoning
                - Consistent format
                - More detailed analysis
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a few-shot prompt to help the AI generate creative writing prompts. 
    Start with these examples and add your own:
    
    ```
    Theme: "Lost in the woods"
    Writing Prompt: "You discover an ancient map carved into a tree trunk. As you trace its lines with your finger, the bark begins to glow."

    Theme: "Future technology"
    Writing Prompt: "Your smart home AI apologizes for a mistake, but you live in a normal house without any AI systems."
    ```
    
    Add 1-2 more examples following this pattern, then ask for a new prompt with your chosen theme.
    """)

    user_prompt = st.text_area(
        "Your few-shot prompt:",
        height=200,
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
                💡 **Few-Shot Analysis:**
                - Did you maintain consistent pattern?
                - Were your examples clear and varied?
                - Did you demonstrate the desired format?
                - Was the final request clear?
                
                Compare the AI's response format with your examples!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2_intro",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_1/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_1_page1() 