import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_3_2_page2():
    st.title("Lesson 3.2: Advanced Hallucination Prevention")
    
    # Introduction
    st.markdown("""
    ### Preventing and Mitigating Hallucinations
    
    Now let's explore advanced techniques for:
    - Designing hallucination-resistant prompts
    - Implementing verification strategies
    - Cross-referencing information
    - Building fact-checking workflows
    """)

    # Advanced Concepts
    st.markdown("""
    ### Prevention Strategies
    
    1. **Prompt Design**
       - Explicit fact requirements
       - Source verification requests
       - Confidence indicators
       - Uncertainty acknowledgment
    
    2. **Verification Frameworks**
       - Multi-source validation
       - Cross-reference checks
       - Temporal consistency
       - Logical coherence tests
    
    3. **Response Analysis**
       - Claim extraction
       - Source verification
       - Consistency checking
       - Plausibility assessment
    """)

    # Interactive Example
    st.markdown("### 👉 Advanced Prevention Exercise")
    
    st.markdown("Analyze these prompting strategies for hallucination prevention:")
    
    strategies = [
        {
            "title": "Research Summary",
            "basic_prompt": "Summarize recent research on climate change mitigation.",
            "issues": [
                "No date range specified",
                "No source requirements",
                "No verification mechanism",
                "Vague scope"
            ],
            "enhanced_prompt": """Provide a summary of climate change mitigation research from 2020-2023, with these requirements:

1. Source Requirements:
   - Only peer-reviewed papers from recognized journals
   - Include DOI or full citation for each claim
   - Specify publication dates

2. Content Structure:
   - Key findings with confidence levels
   - Methodology overview
   - Data sources and sample sizes
   - Study limitations

3. Verification Framework:
   - Indicate consensus vs. emerging findings
   - Note any conflicting results
   - Highlight areas of uncertainty
   - Specify geographic scope

For any claim where you're uncertain, explicitly state "This requires verification" rather than making assumptions."""
        },
        {
            "title": "Technical Documentation",
            "basic_prompt": "Explain the new features in Python 3.11.",
            "issues": [
                "No version verification",
                "No documentation links",
                "No feature categorization",
                "Missing release context"
            ],
            "enhanced_prompt": """Describe the new features in Python 3.11, following these guidelines:

1. Documentation Sources:
   - Official Python documentation only
   - PEP references for each feature
   - Release notes citations
   - Core developer announcements

2. Feature Verification:
   - Link to source code implementations
   - Include example code that works in 3.11
   - Note backward compatibility
   - Specify deprecation notices

3. Information Structure:
   - Category (Performance/Syntax/Library)
   - Implementation status
   - Version requirements
   - Breaking changes

If any feature's status is unclear, mark it as "Needs verification" and provide the relevant issue tracker link."""
        }
    ]

    for strategy in strategies:
        st.markdown(f"**{strategy['title']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("*Basic Prompt:*")
            st.code(strategy["basic_prompt"], language="text")
            
            st.markdown("**Potential Issues:**")
            for issue in strategy["issues"]:
                st.markdown(f"- {issue}")
        
        with col2:
            st.markdown("*Enhanced Prompt:*")
            st.code(strategy["enhanced_prompt"], language="text")
            
            if st.button(f"Test Enhanced Prompt for {strategy['title']}", key=f"test_{strategy['title']}"):
                try:
                    with st.spinner("Getting verified response..."):
                        response = client.send_prompt(strategy["enhanced_prompt"])
                        st.markdown("*Enhanced Response:*")
                        st.markdown(response['response'])
                        
                        st.success("""
                        Notice how this response:
                        - Includes clear sources
                        - Acknowledges uncertainties
                        - Provides verification paths
                        - Maintains precision
                        """)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Design a hallucination-resistant prompt for this topic:
    
    *"Explain the impact of artificial intelligence on job markets."*
    
    Include these prevention mechanisms:
    
    1. **Source Requirements**
       - Specific time periods
       - Credible organizations
       - Industry reports
       - Academic studies
    
    2. **Data Validation**
       - Statistical significance
       - Sample sizes
       - Methodology notes
       - Replication status
    
    3. **Uncertainty Handling**
       - Confidence levels
       - Conflicting findings
       - Knowledge gaps
       - Future uncertainties
    
    Create a prompt that maximizes factual accuracy and minimizes speculation.
    """)

    user_prompt = st.text_area(
        "Your hallucination-resistant prompt:",
        height=300,
        key="practice_prompt"
    )

    if st.button("Test Your Prompt", key="test_prompt") and user_prompt:
        try:
            with st.spinner("Getting AI response..."):
                response = client.send_prompt(user_prompt)
                st.markdown("**AI Response:**")
                st.markdown(response['response'])
                
                # Provide feedback on prevention
                st.info("""
                💡 **Prevention Analysis:**
                - How well are sources specified?
                - Are uncertainties acknowledged?
                - Is speculation minimized?
                - What verification paths exist?
                
                Review the response for verifiable claims!
                """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_2/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_3/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_2_page2() 