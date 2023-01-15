import streamlit as st
import pandas as pd
import numpy as np

st.title('Dashboard Palmilha')

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



