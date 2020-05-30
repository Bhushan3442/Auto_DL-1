import streamlit as st
import matplotlib.pyplot as plt
from  matplotlib.axes import Axes
import seaborn as sb
from load_dataset import *

def visualize_data(x_train,x_test,y_train,top,dataset,classes):
    st.write(" ")
    st.write(" ")
    st.markdown('**Shape**')
    st.write('\nTraining dataset :',x_train.shape, "\nTesting dataset :",x_test.shape)

    if top == "OD":
        st.write(" ")
        st.write(" ")
        st.write("**Sample Images**".format(dataset))

        for i in range(9):
            plt.subplot(330 + 1 + i)
            plt.axis('off')
            plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
        st.pyplot(clear_figure=False)
