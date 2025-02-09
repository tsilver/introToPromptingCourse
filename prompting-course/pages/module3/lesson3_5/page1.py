import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_5_page1():
    st.title("Lesson 3.5: AI Ethics Project")
    
    # Introduction
    st.markdown("""
    ### Final Project: Applying AI Ethics in Practice
    
    In this capstone project, you'll:
    - Design an ethical AI system
    - Apply comprehensive safeguards
    - Consider multiple stakeholders
    - Plan for long-term impacts
    
    Choose a challenging scenario and develop a complete ethical framework.
    """)

    # Project Options
    st.markdown("""
    ### 🎯 Choose Your Challenge
    
    Select one of these real-world scenarios:
    """)
    
    project_choice = st.radio(
        "Select your project focus:",
        [
            "Healthcare AI System",
            "Education AI Platform",
            "Autonomous Vehicle System",
            "Law Enforcement AI"
        ]
    )

    # Display project details based on selection
    project_details = {
        "Healthcare AI System": {
            "description": """Design an AI system for medical diagnosis and treatment recommendations 
            that ensures patient safety, privacy, and equitable care.""",
            "requirements": [
                "HIPAA compliance and data protection",
                "Bias prevention in diagnoses",
                "Professional oversight integration",
                "Emergency override protocols"
            ],
            "considerations": [
                "Patient privacy and consent",
                "Medical accuracy and safety",
                "Healthcare access equity",
                "Professional autonomy"
            ]
        },
        "Education AI Platform": {
            "description": """Create an AI-powered learning platform that personalizes education 
            while protecting student privacy and ensuring fair treatment.""",
            "requirements": [
                "Student data protection",
                "Equitable learning access",
                "Progress monitoring ethics",
                "Parental transparency"
            ],
            "considerations": [
                "Learning style diversity",
                "Socioeconomic factors",
                "Cultural sensitivity",
                "Development appropriateness"
            ]
        },
        "Autonomous Vehicle System": {
            "description": """Develop an ethical framework for self-driving cars that must make 
            split-second decisions affecting human safety.""",
            "requirements": [
                "Safety prioritization protocols",
                "Emergency response systems",
                "Liability frameworks",
                "Public transparency"
            ],
            "considerations": [
                "Life-value decisions",
                "Accident responsibility",
                "Public trust building",
                "Infrastructure integration"
            ]
        },
        "Law Enforcement AI": {
            "description": """Design an AI system for law enforcement that balances public safety 
            with civil rights and privacy concerns.""",
            "requirements": [
                "Civil rights protection",
                "Bias prevention measures",
                "Accountability systems",
                "Privacy safeguards"
            ],
            "considerations": [
                "Community impact",
                "Racial equity",
                "Due process rights",
                "Public oversight"
            ]
        }
    }

    if project_choice:
        project = project_details[project_choice]
        
        st.markdown("### Project Details")
        st.markdown(f"**Description:**\n{project['description']}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Requirements:**")
            for req in project["requirements"]:
                st.markdown(f"- {req}")
        
        with col2:
            st.markdown("**Key Considerations:**")
            for con in project["considerations"]:
                st.markdown(f"- {con}")

    # Framework Development
    st.markdown("""
    ### 📝 Ethical Framework Development
    
    Your framework should address:
    
    1. **System Design**
       - Core functionality
       - Safety measures
       - Privacy protections
       - Access controls
    
    2. **Stakeholder Considerations**
       - Primary users
       - Affected groups
       - Professional requirements
       - Community impact
    
    3. **Implementation Plan**
       - Development phases
       - Testing protocols
       - Deployment strategy
       - Monitoring systems
    
    4. **Risk Management**
       - Potential issues
       - Mitigation strategies
       - Emergency procedures
       - Update protocols
    """)

    # Project Workspace
    st.markdown("### 🛠️ Project Workspace")
    
    framework_sections = {
        "System Design": st.text_area(
            "Describe your system's ethical design:",
            height=200,
            key="system_design"
        ),
        "Stakeholder Analysis": st.text_area(
            "Analyze stakeholder considerations:",
            height=200,
            key="stakeholder_analysis"
        ),
        "Implementation Strategy": st.text_area(
            "Detail your implementation approach:",
            height=200,
            key="implementation"
        ),
        "Risk Management": st.text_area(
            "Outline your risk management plan:",
            height=200,
            key="risk_management"
        )
    }

    if st.button("Analyze Framework", key="analyze_framework"):
        try:
            with st.spinner("Analyzing ethical framework..."):
                # Combine all sections for analysis
                full_framework = "\n\n".join([
                    f"## {title}\n{content}"
                    for title, content in framework_sections.items()
                    if content.strip()
                ])
                
                if full_framework:
                    analysis_prompt = f"""
                    Analyze this ethical AI framework for {project_choice}:
                    
                    {full_framework}
                    
                    Provide feedback on:
                    1. Comprehensiveness of ethical considerations
                    2. Practical implementation feasibility
                    3. Stakeholder protection measures
                    4. Risk management effectiveness
                    5. Areas for improvement
                    """
                    
                    response = client.send_prompt(analysis_prompt)
                    st.markdown("### Framework Analysis")
                    st.markdown(response['response'])
                    
                    st.info("""
                    💡 **Next Steps:**
                    - Review the feedback carefully
                    - Address any gaps identified
                    - Strengthen weak areas
                    - Consider additional safeguards
                    """)
                else:
                    st.warning("Please complete at least one section of the framework.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_4/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Complete Course! →", 
                 on_click=handle_navigation,
                 args=("course_completion",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_5_page1() 