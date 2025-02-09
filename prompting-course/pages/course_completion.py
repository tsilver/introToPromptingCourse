import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_course_completion():
    st.title("🎓 Course Completion: AI Prompting Mastery")
    
    # Celebration and Congratulations
    st.balloons()
    st.markdown("""
    ### 🎉 Congratulations on Completing the Course!
    
    You've successfully completed all modules of the AI Prompting Mastery course. 
    Let's review your learning journey and achievements.
    """)

    # Course Journey Summary
    st.markdown("""
    ### 📚 Your Learning Journey
    
    **Module 1: Fundamentals of Prompting**
    - Mastered basic prompt components
    - Learned context and constraint usage
    - Developed explanation techniques
    - Practiced conversation management
    
    **Module 2: Advanced Techniques**
    - Applied few-shot prompting
    - Utilized role-based approaches
    - Created structured outputs
    - Refined prompts iteratively
    
    **Module 3: Critical Thinking & Ethics**
    - Identified AI biases
    - Detected hallucinations
    - Applied ethical principles
    - Developed ethical frameworks
    """)

    # Skills Assessment
    st.markdown("### 🎯 Core Skills Acquired")
    
    skills = {
        "Prompt Engineering": ["Basic prompting", "Advanced techniques", "Iterative refinement"],
        "Critical Thinking": ["Bias detection", "Hallucination spotting", "Quality assessment"],
        "Ethical Considerations": ["Privacy awareness", "Fairness principles", "Responsible AI usage"],
        "Practical Application": ["Real-world scenarios", "Project implementation", "Problem-solving"]
    }
    
    for category, skill_list in skills.items():
        with st.expander(f"**{category}**"):
            for skill in skill_list:
                st.markdown(f"- {skill}")

    # Progress Analysis
    st.markdown("### 📊 Learning Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Generate Quick Analysis", key="analyze_progress"):
            try:
                with st.spinner("Analyzing your course journey..."):
                    analysis_prompt = """
                    Provide a brief analysis of the student's journey through the AI Prompting course.
                    Focus on key achievements and main areas of growth.
                    """
                    
                    response = client.send_prompt(analysis_prompt)
                    st.markdown("#### Quick Analysis")
                    st.markdown(response['response'])
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    
    with col2:
        st.button("View Comprehensive Analytics 📊", 
                 on_click=handle_navigation,
                 args=("comprehensive_analytics",),
                 use_container_width=True)

    # Next Steps
    st.markdown("""
    ### 🚀 Next Steps
    
    Now that you've completed the course, consider:
    
    1. **Practical Application**
       - Apply these skills to your projects
       - Start with simple implementations
       - Gradually tackle more complex challenges
    
    2. **Continued Learning**
       - Stay updated with AI developments
       - Join AI prompting communities
       - Share your knowledge with others
    
    3. **Project Development**
       - Start your own AI projects
       - Document your prompting strategies
       - Build on your course foundation
    """)

    # Certificate Section
    st.markdown("### 🏆 Course Certificate")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        Your official AIxponential certificate verifies your:
        - Course completion
        - Acquired skills
        - Professional development
        - Technical proficiency
        """)
    
    with col2:
        st.button("View Official Certificate 🎓", 
                 on_click=handle_navigation,
                 args=("course_certificate",),
                 use_container_width=True)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Return to Final Project", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_5/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_course_completion() 