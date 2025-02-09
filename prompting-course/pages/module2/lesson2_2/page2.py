import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_2_page2():
    st.title("Lesson 2.2: Advanced Role-Based Techniques")
    
    # Introduction
    st.markdown("""
    ### Combining Roles and Expertise
    
    Now let's explore advanced role-based techniques:
    - Multiple persona combinations
    - Expert role specifications
    - Dynamic role adaptation
    - Complex audience targeting
    """)

    # Advanced Concepts
    st.markdown("""
    ### Advanced Role Techniques
    
    1. **Expert Role Definition**
       - Professional background
       - Experience level
       - Specialization areas
       - Teaching/communication style
    
    2. **Audience Layering**
       - Primary audience
       - Secondary audiences
       - Mixed expertise levels
       - Cultural considerations
    """)

    # Interactive Example
    st.markdown("### 👉 Complex Role-Based Example")
    
    st.markdown("Let's see how combining roles affects explanations:")
    
    st.code("""Act as an experienced environmental scientist with a background in public communication.
You're giving a TED talk to a mixed audience of:
- Primary: Concerned citizens (general knowledge)
- Secondary: Policy makers (need actionable points)
- Also present: Industry representatives (technical background)

Your goal is to explain the impact of microplastics on ocean ecosystems.
Balance these requirements:
- Use compelling data and visuals
- Provide actionable solutions
- Address economic considerations
- Maintain scientific accuracy

Structure your talk with:
1. Problem definition
2. Current research
3. Impact analysis
4. Solution framework
5. Call to action""", language="text")

    # Try it out section
    st.info("""
    👉 Let's see how this complex role handles the multi-layered communication challenge.
    Compare it with simpler approaches.
    """)

    if st.button("Compare Approaches", key="compare_approaches"):
        try:
            with st.spinner("Getting responses from AI..."):
                basic_response = client.send_prompt(
                    "Explain the impact of microplastics on ocean ecosystems."
                )
                
                expert_response = client.send_prompt("""Act as an experienced environmental scientist with a background in public communication.
You're giving a TED talk to a mixed audience of:
- Primary: Concerned citizens (general knowledge)
- Secondary: Policy makers (need actionable points)
- Also present: Industry representatives (technical background)

Your goal is to explain the impact of microplastics on ocean ecosystems.
Balance these requirements:
- Use compelling data and visuals
- Provide actionable solutions
- Address economic considerations
- Maintain scientific accuracy

Structure your talk with:
1. Problem definition
2. Current research
3. Impact analysis
4. Solution framework
5. Call to action""")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Basic Response:**")
                    st.markdown(basic_response['response'])
                
                with col2:
                    st.markdown("**Expert Multi-Audience Response:**")
                    st.markdown(expert_response['response'])
                
                st.success("""
                Notice how the complex role-based approach:
                - Balances technical and accessible language
                - Addresses multiple stakeholder concerns
                - Maintains professional credibility
                - Drives toward actionable outcomes
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a complex role-based prompt for explaining artificial intelligence ethics. 
    Your prompt should:
    
    1. **Define the Expert Role**
       - Professional background
       - Areas of expertise
       - Communication style
    
    2. **Specify Multiple Audiences**
       - Primary audience
       - Secondary audiences
       - Their different needs
    
    3. **Set Communication Goals**
       - Key messages
       - Desired outcomes
       - Balance of perspectives
    
    4. **Structure Requirements**
       - Organization of content
       - Supporting elements
       - Engagement approach
    """)

    user_prompt = st.text_area(
        "Your complex role-based prompt:",
        height=300,
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
                💡 **Complex Role Analysis:**
                - How well are the expert credentials defined?
                - Are multiple audiences addressed effectively?
                - Is the communication properly layered?
                - Does it achieve all communication goals?
                
                Compare how different audience needs are balanced!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_2/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_3/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_2_page2() 