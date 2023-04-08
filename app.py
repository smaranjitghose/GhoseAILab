import streamlit as st
import streamlit.components.v1 as components
from utils import *


def main():
    '''
    Main function for the web application
    '''

    st.set_page_config(
        layout="centered",
        page_title="Ghose AI Lab",
        page_icon=":robot_face:",)

    disable_sidebar()
    disable_menu()
    write_title("Ghose Lab of Artificial Intelligence", color="#f5f5f5")
    write_footer()

    
    # Call the load_json function to load the JSON file
    course_data = load_json("./courses.json")

    # Check if the JSON data is loaded
    if course_data:
        
        col1, _, col2 = st.columns([1,0.25,1])
        with col1:
            # Create a select box to choose the course 
            course_options = {course["course_name"]: course for course in course_data}
            selected_course_name = st.selectbox("__Select a Course📝__", list(course_options.keys()))
            selected_course = course_options[selected_course_name]
        with col2:
            # Create a select box to choose the week number
            week_options = {f"Week {material['week number']}": material for material in selected_course["material"]}
            selected_week_name = st.selectbox("__Select a Week📅__", list(week_options.keys()))
            selected_week = week_options[selected_week_name]
        
        el_space(n=3)
        tab1,tab2,tab3 = st.tabs(["📚 Course Material", "📕 Suggested Reading","✍️ Homework"])
        with tab1:
            url = f"{selected_week['g_slide']}/embed?start=false&loop=false&delayms=5000"
            components.iframe(url, height=300)

        with tab2:
            read_list = selected_week["reading"]
            if not read_list:
                st.write("PPTs are self sufficient. No need to read anything else.")
            else:
                for i,read in enumerate(read_list):
                    st.write(f"{i+1}. {read}")
        
        with tab3:
            st.write("Will be updated soon.")

if __name__ == "__main__":
    main()