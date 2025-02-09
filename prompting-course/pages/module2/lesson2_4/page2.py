import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

# Initialize the TeacherClient
client = TeacherClient()

def show_lesson_2_4_page2():
    st.title("Lesson 2.4: Advanced Iteration Techniques")
    
    # Introduction
    st.markdown("""
    ### Mastering Advanced Iteration
    
    Let's explore sophisticated techniques for:
    - Systematic prompt improvement
    - Complex scenario handling
    - Multi-stage refinement
    - Performance optimization
    """)

    # Advanced Concepts
    st.markdown("""
    ### Advanced Iteration Strategies
    
    1. **Multi-Stage Refinement**
       - Progressive improvements
       - Targeted optimizations
       - Quality metrics
       - Success criteria
    
    2. **Performance Analysis**
       - Response evaluation
       - Consistency checking
       - Edge case handling
       - Error reduction
    """)

    # Interactive Example
    st.markdown("### 👉 Advanced Iteration Example")
    
    st.markdown("Watch how we refine a complex prompt through multiple stages:")
    
    stages = [
        {
            "stage": "Initial Analysis",
            "prompt": """Analyze the environmental impact of electric vehicles, considering:
- Manufacturing process
- Energy sources
- Battery lifecycle
- Infrastructure needs""",
            "focus": "Basic structure and coverage"
        },
        {
            "stage": "Data Integration",
            "prompt": """Analyze the environmental impact of electric vehicles with specific data:

Key Areas:
1. Manufacturing Process
   - CO2 emissions per vehicle
   - Resource consumption metrics
   - Waste generation data

2. Energy Sources
   - Grid mix percentages
   - Emissions by power source
   - Regional variations

3. Battery Lifecycle
   - Production impact numbers
   - Lifespan statistics
   - Recycling rates

4. Infrastructure
   - Charging station footprint
   - Grid upgrade requirements
   - Material needs

Include relevant statistics and cite sources.""",
            "focus": "Adding quantitative elements"
        },
        {
            "stage": "Comparative Framework",
            "prompt": """Compare environmental impacts of electric vs. traditional vehicles:

Analysis Framework:
1. Manufacturing Phase
   - EV: CO2/vehicle, resource use, waste
   - ICE: CO2/vehicle, resource use, waste
   - Comparative metrics and breakeven points

2. Operational Phase
   - EV: Grid-based emissions by region
   - ICE: Direct emissions and fuel lifecycle
   - Total lifecycle comparison

3. End-of-Life
   - Battery recycling infrastructure
   - Traditional vehicle recycling
   - Net environmental impact

4. Infrastructure Requirements
   - Charging network development
   - Power grid upgrades
   - Economic and environmental costs

Format:
- Use data tables where applicable
- Include uncertainty ranges
- Highlight key findings
- Provide regional variations""",
            "focus": "Adding comparative elements and structure"
        },
        {
            "stage": "Final Optimization",
            "prompt": """Provide a comprehensive environmental impact analysis of electric vs. traditional vehicles:

Required Format:
{
    "manufacturing_impact": {
        "ev_production": {
            "co2_emissions": {"value": number, "unit": "tons CO2e/vehicle"},
            "resource_intensity": {"value": number, "unit": "GJ/vehicle"},
            "key_materials": string[]
        },
        "ice_production": {
            "co2_emissions": {"value": number, "unit": "tons CO2e/vehicle"},
            "resource_intensity": {"value": number, "unit": "GJ/vehicle"},
            "key_materials": string[]
        },
        "comparative_analysis": {
            "breakeven_point": {"value": number, "unit": "years"},
            "key_findings": string[]
        }
    },
    "operational_impact": {
        "regional_analysis": [
            {
                "region": string,
                "grid_mix": {"renewable": number, "fossil": number},
                "ev_emissions": {"value": number, "unit": "g CO2e/km"},
                "ice_emissions": {"value": number, "unit": "g CO2e/km"}
            }
        ],
        "lifetime_comparison": {
            "assumptions": string[],
            "ev_total": {"value": number, "unit": "tons CO2e"},
            "ice_total": {"value": number, "unit": "tons CO2e"},
            "savings": {"value": number, "unit": "tons CO2e"}
        }
    },
    "infrastructure_requirements": {
        "charging_network": {
            "environmental_cost": {"value": number, "unit": "tons CO2e"},
            "resource_needs": string[]
        },
        "grid_upgrades": {
            "estimated_impact": {"value": number, "unit": "tons CO2e"},
            "key_considerations": string[]
        }
    },
    "recommendations": [
        {
            "target": string,
            "action": string,
            "impact": string,
            "timeline": string
        }
    ]
}

Use real data where available, estimate with ranges where necessary.
Provide sources for key statistics.""",
            "focus": "Structured output and comprehensive coverage"
        }
    ]

    for stage in stages:
        st.markdown(f"**{stage['stage']}:**")
        st.markdown(f"*Focus: {stage['focus']}*")
        st.code(stage['prompt'], language="text")
        st.markdown("---")

    # Practice section
    st.markdown("### 🎯 Your Turn!")
    
    st.markdown("""
    Create a multi-stage iteration process for analyzing the impact of social media on society.
    
    Start with a basic prompt and refine it through at least 3 stages, considering:
    1. **Structure Development**
       - Initial organization
       - Key areas to cover
       - Analysis framework
    
    2. **Data Integration**
       - Relevant metrics
       - Statistical requirements
       - Source citations
    
    3. **Output Format**
       - Presentation structure
       - Visual elements
       - Comparative analysis
    """)

    iterations = []
    for i in range(4):
        iteration = st.text_area(
            f"Stage {i+1}:",
            height=150,
            key=f"stage_{i}"
        )
        if iteration:
            iterations.append(iteration)

    if st.button("Test Iterations", key="test_iterations") and iterations:
        try:
            with st.spinner("Testing iterations..."):
                for i, prompt in enumerate(iterations, 1):
                    response = client.send_prompt(prompt)
                    st.markdown(f"**Stage {i} Response:**")
                    st.markdown(response['response'])
                    
                    # Provide feedback after each iteration
                    st.info(f"""
                    💡 **Stage {i} Analysis:**
                    - How has the structure improved?
                    - What new elements were added?
                    - How has the analysis deepened?
                    - What could be enhanced further?
                    """)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_4/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Continue →", 
                 on_click=handle_navigation,
                 args=("module2/lesson2_5/page1",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_2_4_page2() 