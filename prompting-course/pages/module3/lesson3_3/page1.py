import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_3_page1():
    st.title("Lesson 3.3: Responsible AI Usage")
    
    # Introduction
    st.markdown("""
    ### Understanding Ethical AI Interaction
    
    In this lesson, you'll learn about:
    - Ethical considerations in AI prompting
    - Privacy and data sensitivity
    - Responsible information handling
    - Best practices for AI usage
    
    Responsible AI usage is crucial for maintaining trust and preventing harm.
    """)

    # Key Concepts
    st.markdown("""
    ### Core Ethical Principles
    
    1. **Privacy Protection**
       - Personal data handling
       - Sensitive information
       - Data minimization
       - Access controls
    
    2. **Fairness & Inclusion**
       - Equal treatment
       - Diverse representation
       - Accessibility
       - Cultural sensitivity
    
    3. **Transparency**
       - Clear disclosure
       - Source attribution
       - Purpose declaration
       - Limitation acknowledgment
    """)

    # Interactive Example
    st.markdown("### 👉 Ethical Prompting Exercise")
    
    st.markdown("Analyze these scenarios for ethical considerations:")
    
    scenarios = [
        {
            "title": "Healthcare Advice",
            "problematic_prompt": """Generate medical advice for treating depression, including medication recommendations and dosages.""",
            "issues": [
                "Practicing medicine without license",
                "Potential harm from incorrect advice",
                "Missing professional oversight",
                "Legal liability concerns"
            ],
            "ethical_prompt": """Provide general, publicly available information about depression, including:

1. Educational Resources
   - Reputable mental health organizations
   - Official health agency websites
   - Educational materials

2. Support Options
   - Types of mental health professionals
   - Ways to find licensed therapists
   - Support group information
   - Crisis hotline numbers

3. General Wellness Information
   - Lifestyle factors
   - Self-care strategies
   - Warning signs to watch for

Important Notice: This information is for educational purposes only. 
Always consult qualified healthcare professionals for medical advice and treatment decisions."""
        },
        {
            "title": "Personal Data Analysis",
            "problematic_prompt": """Analyze this customer database with names, addresses, and purchase history to identify spending patterns.""",
            "issues": [
                "Privacy violation",
                "Personal data exposure",
                "Consent requirements",
                "Data protection regulations"
            ],
            "ethical_prompt": """Analyze anonymized purchasing patterns with these privacy safeguards:

1. Data Requirements
   - Use aggregated data only
   - Remove all personal identifiers
   - Maintain statistical significance
   - Respect privacy thresholds

2. Analysis Framework
   - Focus on general trends
   - Use broad categories
   - Avoid individual tracking
   - Maintain anonymity

3. Reporting Guidelines
   - Present aggregate insights
   - Use range-based groupings
   - Exclude unique identifiers
   - Follow data protection standards

Ensure compliance with privacy regulations and data protection laws."""
        }
    ]

    for scenario in scenarios:
        st.markdown(f"**{scenario['title']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Problematic Prompt:*")
            st.code(scenario["problematic_prompt"], language="text")
            
            st.markdown("**Ethical Issues:**")
            for issue in scenario["issues"]:
                st.markdown(f"- {issue}")
        
        with col2:
            st.markdown("*Ethical Prompt:*")
            st.code(scenario["ethical_prompt"], language="text")
            
            if st.button(f"Test Ethical Prompt for {scenario['title']}", key=f"test_{scenario['title']}"):
                try:
                    with st.spinner("Getting ethical response..."):
                        response = client.send_prompt(scenario["ethical_prompt"])
                        st.markdown("*Ethical Response:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how this response:
                        - Maintains ethical boundaries
                        - Protects privacy
                        - Provides appropriate disclaimers
                        - Follows best practices
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create an ethically-sound prompt for this scenario:
    
    *"Analyze social media posts to understand user behavior and preferences."*
    
    Consider these ethical aspects:
    
    1. **Privacy Protection**
       - Data anonymization
       - Consent considerations
       - Information security
       - Usage limitations
    
    2. **Ethical Analysis**
       - Fair representation
       - Bias prevention
       - Cultural sensitivity
       - Context preservation
    
    3. **Responsible Reporting**
       - Aggregate insights
       - Data protection
       - Clear disclaimers
       - Appropriate use cases
    
    Design a prompt that achieves the goal while maintaining ethical standards.
    """)

    user_prompt = st.text_area(
        "Your ethical prompt:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on ethical considerations
                st.info("""
                💡 **Ethics Analysis:**
                - How well is privacy protected?
                - Are ethical guidelines followed?
                - What safeguards are in place?
                - Are there appropriate disclaimers?
                
                Review the response for ethical compliance!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_2/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_3/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_3_page1() 