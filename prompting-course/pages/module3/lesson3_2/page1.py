import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_2_page1():
    st.title("Lesson 3.2: Spotting AI Hallucinations")
    
    # Introduction
    st.markdown("""
    ### Understanding AI Hallucinations
    
    In this lesson, you'll learn how to:
    - Identify AI-generated misinformation
    - Implement fact-checking strategies
    - Use verification techniques
    - Reduce hallucination risks
    
    AI hallucinations are instances where models generate plausible-sounding but false information.
    """)

    # Key Concepts
    st.markdown("""
    ### Types of AI Hallucinations
    
    1. **Factual Hallucinations**
       - False statistics
       - Incorrect dates
       - Made-up events
       - Nonexistent sources
    
    2. **Logical Hallucinations**
       - Invalid reasoning
       - False correlations
       - Impossible scenarios
       - Contradictory statements
    
    3. **Contextual Hallucinations**
       - Misapplied knowledge
       - Mixed-up references
       - Temporal confusion
       - Spatial inconsistencies
    """)

    # Interactive Example
    st.markdown("### 👉 Hallucination Detection Exercise")
    
    st.markdown("Analyze these AI responses for potential hallucinations:")
    
    examples = [
        {
            "title": "Historical Facts",
            "prompt": "Describe the impact of the Industrial Revolution on London.",
            "response": """The Industrial Revolution transformed London dramatically. According to Dr. James Mitchell's 1842 study "Urban Transformation in Victorian London," the city's population grew from 100,000 in 1750 to over 2 million by 1850. The famous "Green Street Factory Riots" of 1838 led to major labor reforms, and Mayor Thomas Blackwood's "City Modernization Act" of 1845 revolutionized urban planning.""",
            "hallucinations": [
                "Dr. James Mitchell's 1842 study (nonexistent source)",
                "Green Street Factory Riots (fabricated event)",
                "Mayor Thomas Blackwood and his act (fictional person/law)"
            ],
            "verification_prompt": """Describe the impact of the Industrial Revolution on London, using only widely verified historical facts. Include:

1. Population changes (from verified census data)
2. Major historical events (with dates from reputable sources)
3. Significant legislation (with proper names and dates)

For each claim, indicate the reliable historical source."""
        },
        {
            "title": "Scientific Explanation",
            "prompt": "Explain how quantum computers work.",
            "response": """Quantum computers use quantum bits or 'qubits' that operate using the Heisenberg-Schmidt principle of quantum superposition. The famous QubitFlow algorithm, developed by Dr. Sarah Chen at MIT in 2015, allows for processing speeds up to 10^12 times faster than classical computers using meta-entanglement states.""",
            "hallucinations": [
                "Heisenberg-Schmidt principle (nonexistent)",
                "QubitFlow algorithm (fictional)",
                "Dr. Sarah Chen's research (fabricated)",
                "Meta-entanglement states (made-up term)"
            ],
            "verification_prompt": """Explain how quantum computers work, using only established scientific concepts. Include:

1. Basic principles (from peer-reviewed sources)
2. Key terminology (with standard definitions)
3. Current capabilities (with verified examples)

Avoid speculative claims and cite reputable scientific sources."""
        }
    ]

    for example in examples:
        st.markdown(f"**{example['title']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Original Response:*")
            st.markdown(example["response"])
            
            st.markdown("**Identified Hallucinations:**")
            for hallucination in example["hallucinations"]:
                st.markdown(f"- {hallucination}")
        
        with col2:
            st.markdown("*Verification-Focused Prompt:*")
            st.code(example["verification_prompt"], language="text")
            
            if st.button(f"Test Verified Prompt for {example['title']}", key=f"test_{example['title']}"):
                try:
                    with st.spinner("Getting verified response..."):
                        response = client.send_prompt(example["verification_prompt"])
                        st.markdown("*Verified Response:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how this response:
                        - Sticks to verifiable facts
                        - Cites reliable sources
                        - Avoids speculative claims
                        - Maintains accuracy
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a verification-focused prompt for this topic:
    
    *"Explain the environmental impact of renewable energy technologies."*
    
    Consider these verification aspects:
    
    1. **Source Quality**
       - Peer-reviewed research
       - Official statistics
       - Verified data
       - Reputable organizations
    
    2. **Claim Verification**
       - Specific numbers
       - Named sources
       - Time periods
       - Geographic locations
    
    3. **Balanced Perspective**
       - Benefits and limitations
       - Short and long-term impacts
       - Different technologies
       - Various contexts
    
    Write a prompt that encourages accurate, verifiable information.
    """)

    user_prompt = st.text_area(
        "Your verification-focused prompt:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on verification
                st.info("""
                💡 **Verification Analysis:**
                - Are the claims specific and verifiable?
                - Are sources clearly indicated?
                - Is the information current and accurate?
                - What additional verification might be needed?
                
                Check key claims against reliable sources!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_1/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_2/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_2_page1() 