#carregando as bibliotecas
import pandas as pd
import streamlit as st
import joblib
import numpy as np
import pickle

# load numpy array from csv file
from numpy import loadtxt
# load array,,
rateData = np.loadtxt('probabilitiesModel.csv', delimiter=',')
trueNegative = rateData[0]
truePositive = rateData[1]
var_model = "finalized_model.joblib"
sc = pickle.load(open('scaler.pkl','rb'))

#carregando o modelo treinado.
model = joblib.load(var_model)
# model_cluster = joblib.load(var_model_cluster)

# título
st.title("Desafio")

# subtítulo
st.markdown("Este é um Data App utilizado para exibir a solução de Machine Learning para o problema do desafio na predição de fumantes.")

st.sidebar.subheader("Defina os atributos do indivíduo para predição de fumantes:")

## mapeando dados do usuário para cada atributo
Idade = st.sidebar.number_input("Idade")
IMC = st.sidebar.number_input("IMC")
Custo = st.sidebar.number_input("Custo")

#Creating a session state
if "data" not in st.session_state:
    st.session_state.data = []

# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Classificação")

# verifica se o botão foi acionado
if btn_predict:
    #imprime os dados de teste.
    st.subheader("Predição do modelo:")
    #realiza a predição.
    # result = predict_model(model, data=data_teste)
    result = model.predict(sc.transform([[Idade, IMC, Custo]]))
    #recupera os resultados.
    # pred = result["Fumante"][0]
    # prob = result["Score"][0]*100

    if result == 1:
       st.write("A predição do modelo KNN para o indivíduo inserido é: Fumante, com probabilidade de acerto de {0:.2f}%".format(truePositive * 100))
    else:
       st.write("A predição do modelo KNN para o indivíduo inserido é: Não Fumante, com probabilidade de acerto de {0:.2f}%".format(trueNegative * 100))

    if result == 1:
        result = 'yes'
    else:
        result = 'no'
    st.session_state.data.append([Idade, IMC, Custo, result])
# data_teste.append(data_teste, ignore_index=True)
    df = pd.DataFrame(st.session_state.data, columns = ['Idade','IMC','Custo','Fumante'])
    st.download_button(label = 'Download CSV', data = df.to_csv(), mime='text/csv')
    st.write(df)
