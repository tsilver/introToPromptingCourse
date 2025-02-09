import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top
import plotly.graph_objects as go
import plotly.express as px

# Initialize the TeacherClient
client = TeacherClient()

def show_comprehensive_analytics():
    st.title("📊 Your Learning Journey Analytics")
    
    # Overview Section
    st.markdown("""
    ### 🎯 Performance Overview
    
    This analysis provides insights into your learning journey across all modules and lessons.
    """)

    # Module Performance
    st.markdown("### 📚 Module Performance")
    
    # Sample data - in production, this would come from a database
    module_data = {
        "Module 1: Fundamentals": 92,
        "Module 2: Advanced Techniques": 88,
        "Module 3: Ethics & Critical Thinking": 95
    }
    
    # Create module performance chart
    fig_modules = go.Figure(data=[
        go.Bar(
            x=list(module_data.keys()),
            y=list(module_data.values()),
            marker_color=['#2ecc71', '#3498db', '#9b59b6']
        )
    ])
    fig_modules.update_layout(
        title="Module Completion Scores",
        yaxis_title="Score (%)",
        yaxis_range=[0, 100]
    )
    st.plotly_chart(fig_modules, use_container_width=True)

    # Skill Development
    st.markdown("### 💡 Skill Development")
    
    # Sample skill data
    skills_data = {
        "Basic Prompting": [60, 85, 95],
        "Advanced Techniques": [30, 75, 90],
        "Critical Thinking": [40, 70, 85],
        "Ethical Awareness": [50, 80, 95]
    }
    
    # Create skill development chart
    fig_skills = go.Figure()
    stages = ["Initial", "Mid-course", "Final"]
    
    for skill, values in skills_data.items():
        fig_skills.add_trace(go.Scatter(
            x=stages,
            y=values,
            name=skill,
            mode='lines+markers'
        ))
    
    fig_skills.update_layout(
        title="Skill Progression Over Time",
        yaxis_title="Proficiency (%)",
        yaxis_range=[0, 100]
    )
    st.plotly_chart(fig_skills, use_container_width=True)

    # Detailed Analysis
    st.markdown("### 🔍 Detailed Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Strengths")
        strengths = [
            "Excellent grasp of basic prompting concepts",
            "Strong ethical consideration in AI usage",
            "Effective use of few-shot prompting",
            "Clear understanding of bias detection"
        ]
        for strength in strengths:
            st.markdown(f"✅ {strength}")
    
    with col2:
        st.markdown("#### Areas for Growth")
        growth_areas = [
            "Advanced structured output formatting",
            "Complex scenario handling",
            "Technical implementation details",
            "Edge case considerations"
        ]
        for area in growth_areas:
            st.markdown(f"📈 {area}")

    # Generate AI Analysis
    st.markdown("### 🤖 AI-Generated Learning Analysis")
    
    if st.button("Generate Detailed Analysis", key="generate_analysis"):
        try:
            with st.spinner("Analyzing your learning journey..."):
                analysis_prompt = """
                Provide a detailed analysis of the student's learning journey, considering:
                
                1. Skill Development:
                   - Basic to advanced progression
                   - Technical skill improvement
                   - Critical thinking development
                
                2. Knowledge Application:
                   - Practical implementation
                   - Problem-solving ability
                   - Creative solutions
                
                3. Future Recommendations:
                   - Suggested focus areas
                   - Advanced topics to explore
                   - Practical projects to attempt
                
                Format the response with clear sections and specific examples.
                """
                
                response = client.send_prompt(analysis_prompt)
                st.markdown(response['response'])
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practical Application Metrics
    st.markdown("### 🎯 Practical Application Metrics")
    
    metrics = {
        "Prompts Created": 157,
        "Projects Completed": 12,
        "Successful Implementations": 45,
        "Ethical Analyses": 28
    }
    
    cols = st.columns(len(metrics))
    for col, (metric, value) in zip(cols, metrics.items()):
        col.metric(metric, value)

    # Future Learning Path
    st.markdown("""
    ### 🚀 Recommended Learning Path
    
    Based on your performance and interests, consider exploring:
    
    1. **Advanced Topics**
       - Chain-of-thought prompting
       - Multi-modal AI interactions
       - System prompt design
       - Prompt optimization techniques
    
    2. **Practical Projects**
       - Build a prompt library
       - Create an AI teaching assistant
       - Develop ethical guidelines
       - Design bias detection tools
    
    3. **Community Engagement**
       - Share your knowledge
       - Collaborate on projects
       - Mentor new learners
       - Contribute to discussions
    """)

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Back to Course Completion", 
                 on_click=handle_navigation,
                 args=("course_completion",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_comprehensive_analytics() 