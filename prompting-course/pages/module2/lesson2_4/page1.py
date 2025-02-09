import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_4_page1():
    st.title("Lesson 2.4: Iterative Prompt Refinement")
    
    # Introduction
    st.markdown("""
    ### Mastering Prompt Iteration
    
    In this lesson, you'll learn how to:
    - Systematically improve prompts
    - Identify and fix common issues
    - Test and evaluate responses
    - Optimize for specific goals
    
    Iterative refinement is key to developing effective prompts.
    """)

    # Key Concepts
    st.markdown("""
    ### The Iteration Process
    
    1. **Initial Design**
       - Base prompt creation
       - Goal definition
       - Success criteria
       - Output requirements
    
    2. **Testing & Analysis**
       - Response evaluation
       - Error identification
       - Pattern recognition
       - Edge case testing
    
    3. **Refinement Steps**
       - Targeted improvements
       - Constraint adjustments
       - Format optimization
       - Clarity enhancements
    """)

    # Interactive Example
    st.markdown("### 👉 Let's See Iteration in Action")
    
    st.markdown("Watch how a prompt evolves through multiple iterations:")
    
    iterations = [
        {
            "version": "Initial Prompt",
            "prompt": "Summarize this research paper.",
            "issues": "Too vague, no specific requirements or structure"
        },
        {
            "version": "First Iteration",
            "prompt": """Summarize this research paper with these sections:
- Main findings
- Methodology
- Conclusions""",
            "issues": "Better structure, but needs more specific guidance"
        },
        {
            "version": "Second Iteration",
            "prompt": """Analyze this research paper and provide:
1. Main findings (2-3 bullet points)
2. Methodology overview (50-75 words)
3. Key conclusions and implications
4. Limitations of the study

Keep the language technical but accessible to graduate students.""",
            "issues": "Improved, but could use validation criteria"
        },
        {
            "version": "Final Version",
            "prompt": """Analyze this research paper and provide a structured summary following these requirements:

1. Main Findings
- List 2-3 key discoveries
- Include relevant statistical significance
- Highlight practical implications

2. Methodology
- Study design and approach (50-75 words)
- Key variables measured
- Sample size and characteristics

3. Conclusions
- Primary conclusions with supporting evidence
- Real-world applications
- Future research suggestions

4. Limitations
- Methodology constraints
- Data limitations
- Generalizability considerations

Format: Use clear headers and bullet points
Language: Technical but accessible to graduate students
Length: 300-400 words total

Validation Criteria:
- All sections must be complete
- Include specific numbers and data points
- Maintain objective tone
- Link conclusions to findings"""
        }
    ]

    for i, iteration in enumerate(iterations):
        st.markdown(f"**{iteration['version']}:**")
        st.code(iteration['prompt'], language="text")
        if "issues" in iteration:
            st.info(f"🔍 **Issues to Address:** {iteration['issues']}")
        st.markdown("---")

    # Try it out section
    st.info("""
    👉 Let's compare how the different versions perform with the same research paper abstract.
    Notice how each iteration improves the response quality.
    """)

    if st.button("Compare Versions", key="compare_versions"):
        try:
            with st.spinner("Getting responses..."):
                # Test paper abstract
                abstract = """Recent studies have shown significant correlations between sleep patterns and cognitive performance in university students. This study examined 500 undergraduate students over one semester, measuring sleep duration, quality, and academic performance. Results indicated that students averaging 7-8 hours of sleep performed 23% better on exams than those sleeping less than 6 hours. Additionally, consistent sleep schedules correlated with higher GPA scores (p<0.01). However, the study was limited by self-reported data and single-semester duration."""
                
                responses = []
                for iteration in iterations:
                    response = client.send_prompt(f"{iteration['prompt']}\n\nAbstract: {abstract}")
                    responses.append(response['response'])
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Initial vs. First Iteration:**")
                    st.markdown("*Initial:*")
                    st.markdown(responses[0])
                    st.markdown("*First Iteration:*")
                    st.markdown(responses[1])
                
                with col2:
                    st.markdown("**Second vs. Final Version:**")
                    st.markdown("*Second Iteration:*")
                    st.markdown(responses[2])
                    st.markdown("*Final Version:*")
                    st.markdown(responses[3])
                
                st.success("""
                Notice how each iteration improves:
                - Structure and organization
                - Detail and specificity
                - Completeness of analysis
                - Adherence to requirements
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Take this basic prompt and improve it through at least 2 iterations:
    
    **Initial Prompt:** *"Explain quantum computing"*
    
    Consider these aspects in your iterations:
    1. **Audience and Level**
       - Who is this for?
       - What background knowledge to assume?
    
    2. **Content Structure**
       - What sections to include?
       - How to organize information?
    
    3. **Specific Requirements**
       - What details to cover?
       - What formats to use?
    
    4. **Validation Criteria**
       - How to ensure quality?
       - What standards to meet?
    """)

    iterations = []
    for i in range(3):
        iteration = st.text_area(
            f"Iteration {i+1}:",
            height=150,
            key=f"iteration_{i}"
        )
        if iteration:
            iterations.append(iteration)

    if st.button("Test Iterations", key="test_iterations") and iterations:
        try:
            with st.spinner("Testing iterations..."):
                for i, prompt in enumerate(iterations, 1):
                    response = client.send_prompt(prompt)
                    st.markdown(f"**Response to Iteration {i}:**")
                    st.markdown(response['response'])
                    
                    # Provide feedback after each iteration
                    st.info(f"""
                    💡 **Iteration {i} Analysis:**
                    - How has structure improved?
                    - Are requirements clearer?
                    - Is the guidance more specific?
                    - What could be improved further?
                    """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_3/page2",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_4/page2",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_4_page1() 