import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_5_page1():
    st.title("Lesson 2.5: Prompt Engineering Project")
    
    # Introduction
    st.markdown("""
    ### Final Project: Applying Advanced Prompting Techniques
    
    It's time to put everything you've learned into practice! In this final project, 
    you'll apply all the advanced prompting techniques you've learned to create 
    sophisticated and effective prompts for real-world scenarios.
    """)

    # Project Options
    st.markdown("""
    ### Choose Your Challenge
    
    Select one of the following scenarios for your project:
    
    1. **Travel Brochure**
       - Create an engaging travel brochure for a fictional island
       - Include sections for attractions, accommodations, cuisine
       - Make it persuasive and informative
       - End with a compelling call to action
    
    2. **Historical Speech**
       - Generate a speech from a historical figure
       - Ensure historical accuracy and appropriate persona
       - Match the style to the time period and occasion
       - Maintain authentic voice and tone
    
    3. **Coding Assistant**
       - Develop prompts for generating code
       - Specify language and functionality requirements
       - Include error handling and best practices
       - Ensure clean, efficient code output
    
    4. **Creative Story**
       - Craft a short story with specific requirements
       - Control genre, plot, and character elements
       - Maintain consistent style and tone
       - Create engaging narrative flow
    
    5. **AI Teaching Assistant**
       - Design prompts for explaining academic concepts
       - Create different types of educational content
       - Include assessment and feedback mechanisms
       - Ensure clear and accurate explanations
    """)

    # Project Requirements
    st.markdown("""
    ### Project Requirements
    
    Your submission should include:
    
    1. **Documentation of Process**
       - Initial prompt attempts
       - Iterations and improvements
       - Reasoning for changes
       - Final refined prompt
    
    2. **Implementation of Techniques**
       - Few-shot prompting examples
       - Role/persona definitions
       - Structured output formats
       - Iterative refinements
    
    3. **Analysis and Evaluation**
       - Quality of AI responses
       - Accuracy and bias assessment
       - Ethical considerations
       - Areas for improvement
    """)

    # Interactive Workspace
    st.markdown("### 🎯 Project Workspace")
    
    scenario = st.selectbox(
        "Choose your project scenario:",
        ["Travel Brochure", "Historical Speech", "Coding Assistant", "Creative Story", "AI Teaching Assistant"]
    )
    
    st.markdown("#### Document Your Process")
    
    # Initial Prompt
    st.markdown("**Step 1: Initial Prompt**")
    initial_prompt = st.text_area(
        "Write your initial prompt:",
        height=150,
        key="initial_prompt"
    )

    if st.button("Test Initial Prompt", key="test_initial"):
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(initial_prompt)
                st.markdown("**Initial Response:**")
                st.markdown(response['response'])
                
                st.info("""
                💡 **Analysis Questions:**
                - What worked well in this response?
                - What needs improvement?
                - Which techniques could enhance it?
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Iterations
    st.markdown("**Step 2: Iterations**")
    for i in range(3):
        st.markdown(f"**Iteration {i+1}**")
        iteration = st.text_area(
            f"Refined prompt {i+1}:",
            height=150,
            key=f"iteration_{i}"
        )
        
        if st.button(f"Test Iteration {i+1}", key=f"test_iter_{i}"):
            try:
                with st.spinner("Getting AI response..."):
                    response = client.send_prompt(iteration)
                    st.markdown(f"**Response to Iteration {i+1}:**")
                    st.markdown(response['response'])
                    
                    st.info("""
                    💡 **Improvement Analysis:**
                    - How has the response improved?
                    - What techniques were most effective?
                    - What could be refined further?
                    """)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    # Final Evaluation
    st.markdown("**Step 3: Final Evaluation**")
    st.text_area(
        "Document your evaluation of the final result:",
        height=200,
        placeholder="""Consider:
- Quality of the final output
- Effectiveness of different techniques
- Accuracy and potential bias
- Ethical considerations
- Lessons learned""",
        key="evaluation"
    )

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_4/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3_intro",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_5_page1() 