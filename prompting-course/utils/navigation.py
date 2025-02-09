import streamlit as st
from urllib.parse import urlencode
from streamlit.runtime.scriptrunner import get_script_run_ctx

def init_navigation():
    """Initialize navigation in session state"""
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "home"
    if 'current_module' not in st.session_state:
        st.session_state.current_module = None
    if 'current_lesson' not in st.session_state:
        st.session_state.current_lesson = None
    if 'module1_progress' not in st.session_state:
        st.session_state.module1_progress = 0
    if 'needs_navigation' not in st.session_state:
        st.session_state.needs_navigation = False
    if 'next_page' not in st.session_state:
        st.session_state.next_page = None

def scroll_to_top():
    """Add scroll to top functionality"""
    # Only inject scroll script if flag is set
    if 'scroll_to_top' in st.session_state and st.session_state.scroll_to_top:
        st.markdown("""
            <script>
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            </script>
        """, unsafe_allow_html=True)

def handle_navigation(page):
    """Callback function to handle navigation state updates"""
    # Set navigation flags for next rerun
    st.session_state.needs_navigation = True
    st.session_state.next_page = page

def navigate_to(page):
    """Set up navigation to a page"""
    # Update module and lesson state if needed
    if page.startswith("module1/lesson1_1"):
        st.session_state.current_module = 1
        st.session_state.current_lesson = "1.1"
        st.session_state.module1_progress = 1
    
    # Update page state and query params
    st.session_state.current_page = page
    st.query_params["page"] = page
    
    # Set scroll flag
    st.session_state.scroll_to_top = True

def get_current_page():
    """Get the current page from query parameters or session state."""
    query_params = st.query_params
    if "page" in query_params:
        return query_params["page"]  # New API returns single value directly
    return st.session_state.current_page

def check_navigation_rerun():
    """Check if we need to handle navigation"""
    ctx = get_script_run_ctx()
    if ctx is not None:
        # Clear scroll flag after page loads
        if 'scroll_to_top' in st.session_state:
            del st.session_state.scroll_to_top

    # Handle any pending navigation
    if st.session_state.needs_navigation and st.session_state.next_page:
        next_page = st.session_state.next_page
        st.session_state.needs_navigation = False
        st.session_state.next_page = None
        navigate_to(next_page)
        st.rerun() 