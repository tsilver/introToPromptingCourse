import streamlit as st
from utils.teacher_client import TeacherClient
from utils.navigation import handle_navigation, scroll_to_top

def show_lesson_3_5_page2():
    # ... existing content ...

    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.button("← Previous Page", 
                 on_click=handle_navigation,
                 args=("module3/lesson3_5/page1",),
                 use_container_width=True)
    
    with col3:
        st.button("Complete Course! →", 
                 on_click=handle_navigation,
                 args=("course_completion",),
                 use_container_width=True)

    # Add scroll to top
    scroll_to_top()

if __name__ == "__main__":
    show_lesson_3_5_page2() 