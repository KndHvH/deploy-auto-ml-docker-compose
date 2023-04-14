import streamlit as st
from cache.session_state import init_session_state
from components.st_form import single_consult_form
from model.predict import predict_consult

init_session_state()

st.title('Checkpoint1 - ComNeu')

if not st.session_state.form:
        single_consult_form()
else:
    predict_consult()

    if st.button('New Submit'):
        st.session_state.form = None
        st.session_state.posted = False
        st.experimental_rerun()



