import streamlit as st


def single_consult_form():
    with st.form("Consult"):

        form_data = {}
        
        col1,col2,col3 =  st.columns(3)
        with col1:
            form_data['Wind Direction'] = st.number_input("Wind Direction",step=1, min_value=0, max_value=100)
        with col2:
            form_data['Wind Speed'] = st.number_input("Wind Speed",step=0.01)
        with col3:
            form_data['Humidity'] = st.number_input("Humidity",step=1, min_value=0, max_value=100)
        
        col1,col2,col3 =  st.columns(3)
        with col1:
            form_data['Pressure'] = st.number_input("Pressure",step=0.01, min_value=0.0, max_value=100.0)
        with col2:
            form_data['Power Level'] = st.number_input("Power Level",step=0.01)
        with col3:
            form_data['Light Intensity'] = st.number_input("Light Intensity",step=1, min_value=0, max_value=5)
        
        

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.form = form_data
            st.experimental_rerun()
