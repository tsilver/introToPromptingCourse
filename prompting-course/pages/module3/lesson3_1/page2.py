import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_1_page2():
    st.title("Lesson 3.1: Advanced Bias Detection & Mitigation")
    
    # Introduction
    st.markdown("""
    ### Advanced Bias Detection Strategies
    
    Now let's explore more sophisticated techniques for:
    - Systematic bias detection
    - Intersectional bias analysis
    - Bias mitigation strategies
    - Testing and validation approaches
    """)

    # Advanced Concepts
    st.markdown("""
    ### Complex Bias Patterns
    
    1. **Intersectional Bias**
       - Multiple demographic factors
       - Compounded stereotypes
       - Hidden assumptions
       - Overlapping prejudices
    
    2. **Contextual Bias**
       - Situational stereotypes
       - Domain-specific assumptions
       - Regional variations
       - Temporal context
    
    3. **Systemic Bias**
       - Institutional patterns
       - Historical inequities
       - Power dynamics
       - Structural barriers
    """)

    # Interactive Example
    st.markdown("### 👉 Advanced Bias Detection Exercise")
    
    st.markdown("Analyze these complex scenarios for multiple types of bias:")
    
    scenarios = [
        {
            "title": "Career Advice Scenario",
            "content": """Prompt: "Provide career advice for someone interested in tech leadership."
            
Response: "To succeed in tech leadership, you'll need to be aggressive in pursuing your goals. 
Work late hours, compete with your peers, and assert dominance in meetings. 
Young candidates have an advantage as they can dedicate more time to work."
""",
            "biases": [
                "Age discrimination",
                "Gender stereotyping",
                "Work-life balance assumptions",
                "Cultural bias in leadership style"
            ],
            "improved_prompt": """Provide inclusive career advice for aspiring tech leaders that:
1. Considers diverse leadership styles
2. Balances work-life integration
3. Values experience at all career stages
4. Embraces different cultural approaches
5. Focuses on measurable skills and outcomes

Include examples of successful leaders with varying:
- Leadership styles
- Career paths
- Cultural backgrounds
- Work approaches"""
        },
        {
            "title": "Healthcare Access Scenario",
            "content": """Prompt: "Describe how to improve healthcare access."
            
Response: "People should just work harder to afford better insurance. 
Anyone can access care by driving to the nearest hospital or using their smartphone 
to schedule telehealth appointments."
""",
            "biases": [
                "Socioeconomic privilege",
                "Geographic accessibility assumptions",
                "Technology access bias",
                "Healthcare system knowledge bias"
            ],
            "improved_prompt": """Analyze healthcare access improvements considering:

1. Diverse Populations
   - Various socioeconomic levels
   - Different geographic locations
   - Multiple transportation options
   - Technology accessibility ranges

2. Access Barriers
   - Financial constraints
   - Geographic limitations
   - Language barriers
   - Cultural considerations
   - Physical accessibility needs

3. Solution Framework
   - Multiple delivery methods
   - Varied payment options
   - Cultural competency
   - Accessibility requirements

Provide examples addressing different community needs."""
        }
    ]

    for scenario in scenarios:
        st.markdown(f"**{scenario['title']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Original Scenario:*")
            st.code(scenario["content"], language="text")
            
            st.markdown("**Identified Biases:**")
            for bias in scenario["biases"]:
                st.markdown(f"- {bias}")
        
        with col2:
            st.markdown("*Improved Prompt:*")
            st.code(scenario["improved_prompt"], language="text")
            
            if st.button(f"Test Improved Prompt for {scenario['title']}", key=f"test_{scenario['title']}"):
                try:
                    with st.spinner("Getting inclusive response..."):
                        response = client.send_prompt(scenario["improved_prompt"])
                        st.markdown("*Improved Response:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how this response:
                        - Considers multiple perspectives
                        - Acknowledges systemic factors
                        - Provides inclusive solutions
                        - Addresses various needs
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Analyze and improve this complex scenario:
    
    *"Design an AI assistant for a global education platform that helps students learn better."*
    
    Consider these intersectional factors:
    
    1. **Access & Resources**
       - Technology availability
       - Internet connectivity
       - Device compatibility
       - Economic constraints
    
    2. **Cultural Context**
       - Learning styles
       - Educational values
       - Language preferences
       - Cultural references
    
    3. **Individual Needs**
       - Learning differences
       - Physical accessibility
       - Time zone variations
       - Prior knowledge levels
    
    Create a prompt that addresses these complexities while avoiding biases.
    """)

    user_prompt = st.text_area(
        "Your inclusive prompt:",
        height=300,
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
                💡 **Intersectional Analysis:**
                - How well are multiple factors considered?
                - Are various barriers addressed?
                - Is the solution truly inclusive?
                - What perspectives might be missing?
                
                Consider how different users would experience this solution!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_1/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Begin Lesson 3.2 →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_2/page1",),
                 use_container_width=True)

if __name__ == "__main__":
    show_lesson_3_1_page2() 