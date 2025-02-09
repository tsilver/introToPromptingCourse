import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_1_page2():
    st.title("Lesson 2.1: Advanced Few-Shot Techniques")
    
    # Introduction
    st.markdown("""
    ### Mastering Few-Shot Patterns
    
    Now that we understand the basics, let's explore advanced few-shot techniques:
    - Pattern variations and combinations
    - Handling complex scenarios
    - Troubleshooting common issues
    - Best practices for different tasks
    """)

    # Advanced Concepts
    st.markdown("""
    ### Advanced Few-Shot Strategies
    
    1. **Multiple Pattern Types**
       - Input-Output pairs
       - Step-by-step reasoning
       - Conditional responses
       - Format variations
    
    2. **Quality Considerations**
       - Example diversity
       - Pattern consistency
       - Clear transitions
       - Edge case handling
    """)

    # Interactive Example
    st.markdown("### 👉 Complex Few-Shot Example")
    
    st.markdown("Let's look at a more complex example using multiple patterns for analyzing text:")
    
    st.code("""Here are examples of text analysis with multiple aspects:

Text: "The new electric car shows promising performance, but the high price tag may limit its market impact."
Analysis:
- Sentiment: Mixed (positive performance, negative price concern)
- Key Points: Performance, Price, Market impact
- Recommendation: Consider target market segmentation

Text: "Studies show increasing ocean temperatures are causing coral bleaching at unprecedented rates."
Analysis:
- Sentiment: Negative (environmental concern)
- Key Points: Ocean temperatures, Coral bleaching, Rate of change
- Recommendation: Highlight urgency of climate action

Now analyze this text:
"Remote work has increased productivity for many companies, though some struggle with team collaboration."
""", language="text")

    # Try it out section
    st.info("""
    👉 Notice how this advanced pattern guides the AI to consider multiple aspects in its analysis. 
    Let's see how it handles the complex prompt.
    """)

    if st.button("See Analysis", key="see_analysis"):
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt("""Here are examples of text analysis with multiple aspects:

Text: "The new electric car shows promising performance, but the high price tag may limit its market impact."
Analysis:
- Sentiment: Mixed (positive performance, negative price concern)
- Key Points: Performance, Price, Market impact
- Recommendation: Consider target market segmentation

Text: "Studies show increasing ocean temperatures are causing coral bleaching at unprecedented rates."
Analysis:
- Sentiment: Negative (environmental concern)
- Key Points: Ocean temperatures, Coral bleaching, Rate of change
- Recommendation: Highlight urgency of climate action

Now analyze this text:
"Remote work has increased productivity for many companies, though some struggle with team collaboration."
""")
                st.markdown("**AI Analysis:**")
                st.markdown(response['response'])
                
                st.success("""
                Notice how the response follows the established pattern with:
                - Consistent structure across all aspects
                - Clear categorization
                - Balanced analysis
                - Actionable recommendations
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a complex few-shot prompt for analyzing movie reviews. Include examples that analyze:
    - Overall rating
    - Acting performance
    - Plot strength
    - Technical aspects
    
    Start with this example and add your own:
    ```
    Review: "The stunning visuals couldn't make up for the weak storyline, though the lead actress gave a compelling performance."
    Analysis:
    - Rating: 3/5 (Above average)
    - Acting: Strong lead performance, supporting cast adequate
    - Plot: Weak, lacks coherence
    - Technical: Excellent visuals and cinematography
    ```
    """)

    user_prompt = st.text_area(
        "Your complex few-shot prompt:",
        height=300,
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
                💡 **Advanced Pattern Analysis:**
                - Did you maintain consistent categories?
                - Were your examples diverse?
                - Did you cover all aspects clearly?
                - How well did the AI follow your pattern?
                
                Compare the response structure with your examples!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_1/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_2/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_1_page2() 