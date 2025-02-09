import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_3_page2():
    st.title("Lesson 3.3: Advanced Ethical Considerations")
    
    # Introduction
    st.markdown("""
    ### Complex Ethical Scenarios
    
    Now let's explore advanced ethical considerations:
    - Handling sensitive information
    - Managing conflicting interests
    - Addressing ethical dilemmas
    - Implementing safeguards
    """)

    # Advanced Concepts
    st.markdown("""
    ### Advanced Ethical Frameworks
    
    1. **Data Ethics**
       - Consent management
       - Data lifecycle
       - Information rights
       - Usage boundaries
    
    2. **Ethical Decision-Making**
       - Risk assessment
       - Impact analysis
       - Stakeholder consideration
       - Mitigation strategies
    
    3. **Professional Responsibility**
       - Accountability
       - Transparency
       - Due diligence
       - Ethical guidelines
    """)

    # Interactive Example
    st.markdown("### 👉 Complex Ethical Scenarios")
    
    st.markdown("Analyze these advanced ethical challenges:")
    
    scenarios = [
        {
            "title": "Research Data Analysis",
            "complex_scenario": """A research project involves analyzing social media posts about mental health experiences. The data could help improve support services but contains sensitive personal information.""",
            "considerations": [
                "Privacy vs. public benefit",
                "Data sensitivity levels",
                "Consent implications",
                "Potential harm risks"
            ],
            "ethical_framework": """Design an ethical research analysis framework that:

1. Data Protection
   - Anonymization protocols
   - Data minimization strategies
   - Security measures
   - Access controls

2. Ethical Guidelines
   - IRB compliance requirements
   - Informed consent procedures
   - Participant rights
   - Withdrawal mechanisms

3. Analysis Safeguards
   - Aggregation methods
   - De-identification techniques
   - Privacy-preserving analytics
   - Restricted access levels

4. Reporting Standards
   - Confidentiality measures
   - Result aggregation
   - Finding generalization
   - Impact consideration

Include appropriate disclaimers and ethical statements."""
        },
        {
            "title": "AI System Development",
            "complex_scenario": """Developing an AI system to help with hiring decisions. The system needs to be fair and unbiased while maintaining efficiency and effectiveness.""",
            "considerations": [
                "Algorithmic fairness",
                "Protected characteristics",
                "Bias mitigation",
                "Transparency requirements"
            ],
            "ethical_framework": """Establish ethical AI development guidelines:

1. Fairness Requirements
   - Protected attribute handling
   - Bias testing protocols
   - Fairness metrics
   - Validation procedures

2. Transparency Measures
   - Decision explanation
   - Process documentation
   - Audit trails
   - User communication

3. Compliance Framework
   - Legal requirements
   - Industry standards
   - Best practices
   - Regular audits

4. Monitoring System
   - Performance metrics
   - Bias detection
   - Impact assessment
   - Feedback mechanisms

Include clear documentation of ethical considerations and limitations."""
        }
    ]

    for scenario in scenarios:
        st.markdown(f"**{scenario['title']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Scenario:*")
            st.markdown(scenario["complex_scenario"])
            
            st.markdown("**Key Considerations:**")
            for consideration in scenario["considerations"]:
                st.markdown(f"- {consideration}")
        
        with col2:
            st.markdown("*Ethical Framework:*")
            st.code(scenario["ethical_framework"], language="text")
            
            if st.button(f"Test Framework for {scenario['title']}", key=f"test_{scenario['title']}"):
                try:
                    with st.spinner("Getting ethical analysis..."):
                        response = client.send_prompt(scenario["ethical_framework"])
                        st.markdown("*Framework Implementation:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how this framework:
                        - Addresses multiple stakeholders
                        - Implements safeguards
                        - Ensures accountability
                        - Maintains transparency
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Develop an ethical framework for this complex scenario:
    
    *"Creating an AI system that provides personalized learning recommendations for students, using their academic history, learning style, and behavioral data."*
    
    Address these ethical dimensions:
    
    1. **Data Handling**
       - Student privacy
       - Data security
       - Access controls
       - Retention policies
    
    2. **Algorithmic Fairness**
       - Equal opportunity
       - Bias prevention
       - Accessibility
       - Inclusivity
    
    3. **Transparency**
       - Decision explanation
       - Parent/guardian rights
       - Student agency
       - System limitations
    
    4. **Impact Assessment**
       - Educational benefits
       - Potential risks
       - Mitigation strategies
       - Success metrics
    
    Create a comprehensive ethical framework that protects students while maximizing educational benefits.
    """)

    user_prompt = st.text_area(
        "Your ethical framework:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Test Your Framework", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on framework
                st.info("""
                💡 **Framework Analysis:**
                - How comprehensive is the protection?
                - Are all stakeholders considered?
                - What safeguards are included?
                - How is transparency maintained?
                
                Review the framework for completeness and effectiveness!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_3/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_4/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_3_page2() 