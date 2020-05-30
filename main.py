import streamlit as st
from load_dataset import *
from visualisation import *

if __name__ == '__main__':
    st.title("Deep Learning using Streamlit")
    st.write("Use this web application to build complex deep learning with just few simple clicks")
    st.write("")

    x_train,y_train,x_test,y_test,top,dataset,classes = select_dataset()

    visualize_data(x_train,x_test,y_train,top,dataset,classes)
