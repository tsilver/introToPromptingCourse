import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_2_page1():
    st.title("Lesson 2.2: Persona and Role-Based Prompting")
    
    # Introduction
    st.markdown("""
    ### Mastering Role-Based Prompts
    
    In this lesson, you'll learn how to use personas and roles to:
    - Control the AI's writing style and tone
    - Get expertise-specific responses
    - Maintain consistent character voice
    - Achieve specific communication goals
    
    Role-based prompting helps you get responses tailored to specific contexts and audiences.
    """)

    # Key Concepts
    st.markdown("""
    ### Understanding Persona Prompting
    
    A persona prompt includes:
    1. **Role Definition**: Who the AI should act as
    2. **Expertise Level**: Required knowledge depth
    3. **Communication Style**: Tone and language approach
    4. **Target Audience**: Who the response is for
    
    This helps shape both the content and delivery of the AI's response.
    """)

    # Interactive Example
    st.markdown("### 👉 Let's See Persona Prompting in Action")
    
    st.markdown("Here's how different personas explain the same concept:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Prompt:**")
        st.code("Explain how a smartphone works.", language="text")
        
    with col2:
        st.markdown("**Persona-Based Prompt:**")
        st.code("""Act as a friendly tech educator explaining to a group of seniors.
Your goal is to build confidence with technology.
Use simple analogies and avoid technical jargon.
Break down concepts into manageable parts.

Explain how a smartphone works, focusing on:
1. Basic components
2. Daily usage
3. Common features
4. Safety and privacy""", language="text")

    # Try it out section
    st.info("""
    👉 Let's compare responses with different personas. Notice how each role shapes 
    the explanation style and content focus.
    """)

    if st.button("Compare Responses", key="compare_responses"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt("Explain how a smartphone works.")
                
                tech_educator = client.send_prompt("""Act as a friendly tech educator explaining to a group of seniors.
Your goal is to build confidence with technology.
Use simple analogies and avoid technical jargon.
Break down concepts into manageable parts.

Explain how a smartphone works, focusing on:
1. Basic components
2. Daily usage
3. Common features
4. Safety and privacy""")
                
                engineer = client.send_prompt("""Act as a software engineer explaining to a technical audience.
Focus on system architecture and technical specifications.
Use precise terminology and include technical details.
Address performance considerations.

Explain how a smartphone works, focusing on:
1. Hardware components
2. Operating system
3. Application framework
4. Network connectivity""")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("**Basic Response:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**Tech Educator Response:**")
                    st.markdown(tech_educator['response'])
                
                with col3:
                    st.markdown("**Engineer Response:**")
                    st.markdown(engineer['response'])
                
                st.success("""
                Notice how each persona results in:
                - Different language complexity
                - Varying technical depth
                - Appropriate analogies
                - Audience-specific focus
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a persona-based prompt to explain climate change. Choose a specific role and audience.
    
    Consider these elements:
    - Who is explaining? (Teacher, Scientist, Journalist, etc.)
    - Who is the audience? (Kids, Adults, Experts, etc.)
    - What's the communication goal? (Inform, Persuade, Guide, etc.)
    - What tone is appropriate? (Formal, Friendly, Professional, etc.)
    
    Include specific instructions about:
    - Language level
    - Use of analogies
    - Technical depth
    - Key points to cover
    """)

    user_prompt = st.text_area(
        "Your persona-based prompt:",
        height=200,
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
                💡 **Persona Analysis:**
                - Is the role clearly defined?
                - Is the audience considered?
                - Is the tone appropriate?
                - Are the instructions specific?
                
                Compare how the response matches your intended style!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_1/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_2/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_2_page1() 