import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_3_page2():
    st.title("Lesson 2.3: Advanced Structured Outputs")
    
    # Introduction
    st.markdown("""
    ### Complex Data Structures and Validation
    
    Now let's explore advanced structured output techniques:
    - Nested data structures
    - Mixed format outputs
    - Data validation rules
    - Error handling strategies
    """)

    # Advanced Concepts
    st.markdown("""
    ### Advanced Formatting Techniques
    
    1. **Nested Structures**
       - Parent-child relationships
       - Array of objects
       - Conditional nesting
       - Optional fields
    
    2. **Validation Rules**
       - Data type checking
       - Required fields
       - Value constraints
       - Format patterns
    """)

    # Interactive Example
    st.markdown("### 👉 Complex Structure Example")
    
    st.markdown("Let's analyze a complex dataset with nested information:")
    
    st.code("""Create a detailed analysis of this company data using the following nested JSON structure:
{
    "company": {
        "name": string,
        "industry": string,
        "size": {
            "employees": number,
            "revenue": string,  // Format: "$X million/billion"
            "locations": number
        }
    },
    "performance": {
        "financial": {
            "growth_rate": number,  // Percentage
            "profit_margin": number,  // Percentage
            "key_metrics": [
                {
                    "name": string,
                    "value": number,
                    "trend": "up" | "down" | "stable",
                    "impact": "positive" | "negative" | "neutral"
                }
            ]
        },
        "operational": {
            "efficiency_score": number,  // 1-100
            "challenges": string[],
            "opportunities": string[]
        }
    },
    "recommendations": [
        {
            "area": string,
            "suggestion": string,
            "priority": "high" | "medium" | "low",
            "estimated_impact": {
                "timeframe": string,
                "potential_benefit": string
            }
        }
    ]
}

Company Info: "Tech Solutions Inc. is a mid-sized software company with 500 employees across 5 locations. Annual revenue is $75 million, showing 15% growth. They have strong product development but face scaling challenges."
""", language="text")

    # Try it out section
    st.info("""
    👉 See how the AI handles complex nested structures and validation requirements.
    Notice the relationships between different data elements.
    """)

    if st.button("Generate Analysis", key="generate_analysis"):
        try:
            with st.spinner("Getting structured analysis..."):
                response = client.send_prompt("""Create a detailed analysis of this company data using the following nested JSON structure:
{
    "company": {
        "name": string,
        "industry": string,
        "size": {
            "employees": number,
            "revenue": string,  // Format: "$X million/billion"
            "locations": number
        }
    },
    "performance": {
        "financial": {
            "growth_rate": number,  // Percentage
            "profit_margin": number,  // Percentage
            "key_metrics": [
                {
                    "name": string,
                    "value": number,
                    "trend": "up" | "down" | "stable",
                    "impact": "positive" | "negative" | "neutral"
                }
            ]
        },
        "operational": {
            "efficiency_score": number,  // 1-100
            "challenges": string[],
            "opportunities": string[]
        }
    },
    "recommendations": [
        {
            "area": string,
            "suggestion": string,
            "priority": "high" | "medium" | "low",
            "estimated_impact": {
                "timeframe": string,
                "potential_benefit": string
            }
        }
    ]
}

Company Info: "Tech Solutions Inc. is a mid-sized software company with 500 employees across 5 locations. Annual revenue is $75 million, showing 15% growth. They have strong product development but face scaling challenges."
""")
                
                st.markdown("**Structured Analysis:**")
                st.code(response['response'], language="json")
                
                st.success("""
                Notice how the structured format:
                - Maintains complex relationships
                - Enforces data types
                - Provides clear hierarchy
                - Enables detailed analysis
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a complex structured format for analyzing a research paper. Include:
    
    1. **Basic Information**
       - Title, authors, publication
       - Keywords and categories
       - Impact metrics
    
    2. **Content Analysis**
       - Abstract summary
       - Key findings
       - Methodology details
    
    3. **Impact Assessment**
       - Citations and references
       - Field contributions
       - Future implications
    
    Design your structure with appropriate nesting and validation rules!
    """)

    user_prompt = st.text_area(
        "Your complex structured prompt:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.code(response['response'], language="json")
                
                # Provide feedback on structure
                st.info("""
                💡 **Structure Analysis:**
                - How well are relationships represented?
                - Are validation rules clear?
                - Is the nesting logical?
                - Are data types appropriate?
                
                Test the structure with different research papers!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_3/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_4/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_3_page2() 