import streamlit as st
import matplotlib.pyplot as plt
from  matplotlib.axes import Axes
import seaborn as sb
from load_dataset import *
import numpy as np
from keras.datasets import imdb
import pandas as pd

def visualize_data(x_train,x_test,y_train,top,dataset,classes):
    st.write(" ")
    st.write(" ")
    st.markdown('**Shape**')
    st.write('\nTraining dataset :',x_train.shape, "\nTesting dataset :",x_test.shape)

    if top == "OD":
        st.write(" ")
        st.write(" ")

        st.markdown("<h3 style='text-align: center;'>Sample Images</h3>", unsafe_allow_html=True)
        for i in range(9):
            plt.subplot(330 + 1 + i)
            plt.axis('off')
            plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
        st.pyplot(clear_figure=False)

    if top == "NLP":
        st.write(" ")
        index = imdb.get_word_index()
        feature = []
        for i in range(5):
            reverse_index = dict([(value, key) for (key, value) in index.items()])
            decoded = " ".join( [reverse_index.get(j - 3, "#") for j in x_train[i]])
            decoded = decoded[1:]
            feature.append(decoded)
        label = [classes[y_train[i]] for i in range(5)]

        st.markdown("<h3 style='text-align: center;'>Sample Data</h3>", unsafe_allow_html=True)
        df = pd.DataFrame(list(zip(feature,label)),columns = ['Reviews','Sentiments'])
        st.table(df)
