import streamlit as st
import pandas as pd
import numpy as np

st.title('Dashboard Palmilha')

def loadData():
    df = pd.read_csv('./dataset.csv', sep=',')
    df['acc_x'] = df['acc_x'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['acc_y'] = df['acc_y'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['acc_z'] = df['acc_z'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['gyro_x'] = df['gyro_x'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['gyro_y'] = df['gyro_y'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['gyro_z'] = df['gyro_z'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['mag_x'] = df['mag_x'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['mag_y'] = df['mag_y'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['mag_z'] = df['mag_z'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['hallux'] = df['hallux'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['toes'] = df['toes'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['met1'] = df['met1'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['met3'] = df['met3'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['met5'] = df['met5'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['arch'] = df['arch'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['heelL'] = df['heelL'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    df['heelR'] = df['heelR'].apply(lambda x : str(x).replace('[','').replace(']', '')).astype('float')
    return df


df = loadData()


sole = df[['hallux', 'toes','met1', 'met3', 'met5','arch', 'heelL', 'heelR']]
acc = df[['acc_x', 'acc_y', 'acc_z']]
gyro = df[['gyro_x', 'gyro_y', 'gyro_z']]
mag = df[['mag_x', 'mag_y', 'mag_z']]
st.header('Gráfico Variação Pressão')
st.line_chart(sole)
st.header('Gráfico Variação Acelerômetro')
st.line_chart(acc)
st.header('Gráfico Variação Giroscópio')
st.line_chart(gyro)
st.header('Gráfico Variação Magnetômetro')
st.line_chart(mag)

st.markdown(
    """
        <div class="parent">
            <style>
                .parent {       
                    position: relative;
                    height: 500px;
                }
                .section {
                    height: 120px;
                    width: 70px;
                    background: linear-gradient(to right, green, red);
                    background-size: 100% 100%;
                    border-radius:10px 10px 10px 10px;
                    position: absolute;
                }
                .hallux{
                    top: 10px;
                    left: 0px;
                }
                .toes {
                    top: 10px;
                    left: 120px;
                    transform: rotate(-45deg);
                }
                .met1 {
                    top: 150px;
                    left: 0px;
                }
                .met3{
                    top: 150px;
                    left: 100px;
                }
                .met5{
                    top: 150px;
                    left: 200px;
                }
                .arch{
                    top: 300px;
                    left: 200px;
                }
                .heelL{
                    top: 450px;
                    left: 100px;
                }
                .heelR{
                    top: 450px;
                    left: 200px;
                }
            </style>
            <div class="section hallux">
                1
            </div>
            <div class="section toes">
                2
            </div>
            <div class="section met1">
                3
            </div>
            <div class="section met3">
                4
            </div>
            <div class="section met5">
                5
            </div>
            <div class="section arch">
                6
            </div>
            <div class="section heelL">
                7
            </div>
            <div class="section heelR">
                8
            </div>
        </div>
    """
, unsafe_allow_html=True)



