

import streamlit as st
import pandas as pd
from pycaret.classification import *
from database.database import create_table, get_predicts_in_db, save_predict

MODEL_PKL_PATH='./model/pickle_et_pycaret'
MODEL = load_model(MODEL_PKL_PATH)

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

def predict(data):
    return predict_model(MODEL, data = data, raw_score = True)


def predict_consult():

    Xtest = pd.DataFrame(st.session_state.form, index=[0])
    ypred = predict(Xtest)

    if not st.session_state.posted:
        create_table()
        save_predict(ypred)
        st.session_state.posted = True

    with st.expander('Visualizar Form carregado:', expanded = False):
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(Xtest)

    with st.expander('Visualizar Predição:', expanded = True):
        result = ((ypred['prediction_label'].item())-32)/1.8
        color = 'red' if result > 25  else 'blue'

        st.markdown(f'# **:{color}[{result:.2f}°C]**')

        tipo_view = st.radio('', ('Completo', 'Apenas predições'))
        df_view = pd.DataFrame(ypred.iloc[:,-1].copy())
        
        if tipo_view == 'Completo': df_view = ypred.copy()

        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df_view)
        

    with st.expander('Visualizar antigos predicts'):
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(get_predicts_in_db())
