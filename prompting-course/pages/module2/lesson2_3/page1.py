import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_3_page1():
    st.title("Lesson 2.3: Structured Output Formatting")
    
    # Introduction
    st.markdown("""
    ### Mastering Structured Outputs
    
    In this lesson, you'll learn how to:
    - Request specific output formats (JSON, XML, etc.)
    - Create custom data structures
    - Ensure consistent formatting
    - Validate structured responses
    
    Structured outputs make AI responses more reliable and easier to process.
    """)

    # Key Concepts
    st.markdown("""
    ### Common Output Formats
    
    1. **Data Formats**
       - JSON
       - XML
       - YAML
       - CSV
    
    2. **Text Structures**
       - Tables
       - Lists
       - Key-value pairs
       - Hierarchical formats
    """)

    # Interactive Example
    st.markdown("### 👉 Let's Compare Format Approaches")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Prompt:**")
        st.code("""Analyze this product review:
"Great laptop, fast performance, but battery life could be better. Screen is crystal clear."
""", language="text")
        
    with col2:
        st.markdown("**Structured Format Prompt:**")
        st.code("""Analyze this product review and provide the results in JSON format with the following structure:
{
    "sentiment": string,  // Overall sentiment (positive/negative/mixed)
    "rating": number,     // Estimated rating out of 5
    "aspects": [
        {
            "feature": string,    // Product feature
            "sentiment": string,  // Sentiment about this feature
            "comment": string     // Relevant quote or summary
        }
    ],
    "summary": string     // Brief overall summary
}

Review text: "Great laptop, fast performance, but battery life could be better. Screen is crystal clear."
""", language="text")

    # Try it out section
    st.info("""
    👉 Let's see how structured format requests affect AI responses. Notice how the 
    formatted output is more consistent and easier to process.
    """)

    if st.button("Compare Responses", key="compare_responses"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt("""Analyze this product review:
"Great laptop, fast performance, but battery life could be better. Screen is crystal clear."
""")
                
                structured_response = client.send_prompt("""Analyze this product review and provide the results in JSON format with the following structure:
{
    "sentiment": string,  // Overall sentiment (positive/negative/mixed)
    "rating": number,     // Estimated rating out of 5
    "aspects": [
        {
            "feature": string,    // Product feature
            "sentiment": string,  // Sentiment about this feature
            "comment": string     // Relevant quote or summary
        }
    ],
    "summary": string     // Brief overall summary
}

Review text: "Great laptop, fast performance, but battery life could be better. Screen is crystal clear."
""")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Basic Response:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**Structured Response:**")
                    st.code(structured_response['response'], language="json")
                
                st.success("""
                Notice how the structured format:
                - Organizes information clearly
                - Makes data extraction easier
                - Ensures consistent structure
                - Separates different aspects
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a structured format prompt to analyze movie data. Design a format that captures:
    - Basic movie information
    - Cast and crew details
    - Ratings and reviews
    - Technical details
    
    Start with this example structure and modify it:
    ```json
    {
        "title": string,
        "year": number,
        "genre": string[],
        "credits": {
            "director": string,
            "mainCast": string[]
        },
        "ratings": {
            "score": number,
            "reviews": number
        }
    }
    ```
    
    Add or modify fields to capture the information you want!
    """)

    user_prompt = st.text_area(
        "Your structured format prompt:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.code(response['response'], language="json")
                
                # Provide feedback on format structure
                st.info("""
                💡 **Format Analysis:**
                - Is the structure clear and logical?
                - Are data types specified correctly?
                - Is all necessary information captured?
                - How well is the hierarchy organized?
                
                Try parsing the response as JSON to verify its structure!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_2/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_3/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_3_page1() 