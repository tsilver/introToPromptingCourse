import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_4_page1():
    st.title("Lesson 3.4: AI Ethics in Practice")
    
    # Introduction
    st.markdown("""
    ### Applying Ethical Principles in Real-World Scenarios
    
    In this lesson, you'll learn to:
    - Apply ethical principles to real situations
    - Make informed ethical decisions
    - Assess AI system impacts
    - Plan for future implications
    
    Understanding how to apply ethics in practice is crucial for responsible AI development.
    """)

    # Key Concepts
    st.markdown("""
    ### Real-World Applications
    
    1. **Impact Assessment**
       - Societal effects
       - Individual impacts
       - Environmental considerations
       - Economic implications
    
    2. **Decision Frameworks**
       - Ethical guidelines
       - Risk evaluation
       - Benefit analysis
       - Stakeholder consideration
    
    3. **Future Planning**
       - Long-term effects
       - Emerging challenges
       - Adaptive strategies
       - Continuous improvement
    """)

    # Interactive Example
    st.markdown("### 👉 Real-World Ethics Exercise")
    
    st.markdown("Analyze these real-world scenarios for ethical implications:")
    
    scenarios = [
        {
            "title": "AI in Education",
            "scenario": """A school district plans to implement an AI system that tracks student behavior, 
attendance, and academic performance to predict which students might need additional support.""",
            "considerations": [
                "Student privacy rights",
                "Data security requirements",
                "Potential discrimination",
                "Transparency needs"
            ],
            "ethical_analysis": """Conduct an ethical analysis of the AI education system:

1. Privacy Protection
   - Data collection limits
   - Storage security
   - Access controls
   - Deletion policies

2. Fairness Assessment
   - Bias detection
   - Equal treatment
   - Cultural sensitivity
   - Socioeconomic factors

3. Transparency Requirements
   - System explanation
   - Decision criteria
   - Appeal process
   - Regular audits

4. Impact Evaluation
   - Student benefits
   - Potential risks
   - Parent concerns
   - Teacher input

Include specific recommendations for ethical implementation."""
        },
        {
            "title": "AI in Healthcare",
            "scenario": """A hospital is developing an AI system to prioritize emergency room patients 
based on symptoms, vital signs, and medical history.""",
            "considerations": [
                "Patient safety",
                "Medical privacy",
                "Fair treatment",
                "Professional oversight"
            ],
            "ethical_analysis": """Evaluate the ethical implications of the ER triage system:

1. Safety Protocols
   - Risk assessment
   - Override mechanisms
   - Emergency procedures
   - Backup systems

2. Privacy Standards
   - HIPAA compliance
   - Data protection
   - Information sharing
   - Consent management

3. Fairness Measures
   - Demographic analysis
   - Bias testing
   - Equal access
   - Cultural competency

4. Professional Integration
   - Staff training
   - Expert oversight
   - Decision authority
   - Accountability measures

Provide specific guidelines for ethical deployment."""
        }
    ]

    for scenario in scenarios:
        st.markdown(f"**{scenario['title']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Scenario:*")
            st.markdown(scenario["scenario"])
            
            st.markdown("**Key Considerations:**")
            for consideration in scenario["considerations"]:
                st.markdown(f"- {consideration}")
        
        with col2:
            st.markdown("*Ethical Analysis:*")
            st.code(scenario["ethical_analysis"], language="text")
            
            if st.button(f"Analyze {scenario['title']}", key=f"analyze_{scenario['title']}"):
                try:
                    with st.spinner("Conducting ethical analysis..."):
                        response = client.send_prompt(scenario["ethical_analysis"])
                        st.markdown("*Analysis Results:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how this analysis:
                        - Considers multiple stakeholders
                        - Evaluates various impacts
                        - Proposes specific safeguards
                        - Plans for implementation
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Conduct an ethical analysis of this scenario:
    
    *"A city plans to implement an AI-powered surveillance system in public spaces to reduce crime. 
    The system would use facial recognition and behavior analysis to identify potential criminal activity."*
    
    Consider these aspects:
    
    1. **Privacy Impact**
       - Public surveillance
       - Data collection
       - Information storage
       - Access controls
    
    2. **Social Implications**
       - Civil liberties
       - Public safety
       - Community trust
       - Social equity
    
    3. **Implementation Ethics**
       - System transparency
       - Accountability measures
       - Appeal processes
       - Oversight mechanisms
    
    4. **Future Considerations**
       - Long-term effects
       - Policy implications
       - Technology evolution
       - Societal impact
    
    Create a comprehensive ethical analysis and implementation plan.
    """)

    user_prompt = st.text_area(
        "Your ethical analysis:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Analyze Ethics", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on analysis
                st.info("""
                💡 **Analysis Review:**
                - How comprehensive is the evaluation?
                - Are all stakeholders considered?
                - What safeguards are proposed?
                - How are future implications addressed?
                
                Consider both immediate and long-term impacts!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_3/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_5/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_4_page1() 