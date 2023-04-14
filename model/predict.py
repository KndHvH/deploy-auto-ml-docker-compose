

import streamlit as st
import pandas as pd
from pycaret.classification import *
from database.database import create_table, get_predicts_in_db, save_predict

MODEL_PKL_PATH='./model/pickle_et_pycaret'
MODEL = load_model(MODEL_PKL_PATH)


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
        st.dataframe(Xtest)

    with st.expander('Visualizar Predição:', expanded = True):
        result = ((ypred['prediction_label'].item())-32)/1.8
        color = 'red' if result > 25  else 'blue'

        st.markdown(f'# **:{color}[{result:.2f}°C]**')

        tipo_view = st.radio('', ('Completo', 'Apenas predições'))
        df_view = pd.DataFrame(ypred.iloc[:,-1].copy())
        
        if tipo_view == 'Completo': df_view = ypred.copy()

        st.dataframe(df_view)

    with st.expander('Visualizar antigos predicts'):

        st.dataframe(get_predicts_in_db())
