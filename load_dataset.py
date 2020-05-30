import streamlit as st
import numpy as np
def select_dataset ():

    dataset = st.selectbox(
    "Select the dataset that you wish to work on ",
        ('MNIST', 'CIFAR-10', 'CIFAR-100', 'IMDB','Fashion MNIST','Boston Housing Price')
    )

    if dataset == 'MNIST':

        from keras.datasets import mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        classes = [0,1,2,3,4,5,6,7,8,9]

        top = "OD"


    elif dataset == 'Fashion MNIST':

        from keras.datasets import fashion_mnist

        (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
        classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

        top = "OD"

    elif dataset == 'CIFAR-10':

        from keras.datasets import cifar10

        (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        classes = ['airplane','automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse','ship','truck']

        top = "OD"

    elif dataset == 'CIFAR-100':

        from keras.datasets import cifar100

        (x_train, y_train), (x_test, y_test) = cifar100.load_data()
        classes = ['beaver', ' dolphin', ' otter', ' seal', ' whale', ' aquarium fish', ' flatfish', ' ray', ' shark', ' trout', ' orchids', ' poppies', ' roses', ' sunflowers', ' tulips', ' bottles', ' bowls', ' cans', ' cups', ' plates', ' apples', ' mushrooms', ' oranges', ' pears', ' sweet peppers', ' clock', ' computer keyboard', ' lamp', ' telephone', ' television', ' bed', ' chair', ' couch', ' table', ' wardrobe', ' bee', ' beetle', ' butterfly', ' caterpillar', ' cockroach', ' bear', ' leopard', ' lion', ' tiger', ' wolf', ' bridge', ' castle', ' house', ' road', ' skyscraper', ' cloud', ' forest', ' mountain', ' plain', ' sea', ' camel', ' cattle', ' chimpanzee', ' elephant', ' kangaroo', ' fox', ' porcupine', ' possum', ' raccoon', ' skunk', ' crab', ' lobster', ' snail', ' spider', ' worm', ' baby', ' boy', ' girl', ' man', ' woman', ' crocodile', ' dinosaur', ' lizard', ' snake', ' turtle', ' hamster', ' mouse', ' rabbit', ' shrew', ' squirrel', ' maple', ' oak', ' palm', ' pine', ' willow', ' bicycle', ' bus', ' motorcycle', ' pickup truck', ' train', ' lawn-mower', ' rocket', ' streetcar', ' tank', ' tractor']

        top = "OD"

    elif dataset == 'IMDB':

        st.write("If Running for the first time the application will download the the dataset.")
        from keras.datasets import imdb

        (x_train, y_train), (x_test, y_test) = imdb.load_data()

        classes = ["Negative", "Positive"]

        top = "NLP"


    elif dataset == 'Boston Housing Price':

        from keras.datasets import boston_housing

        (x_train, y_train), (x_test, y_test) = boston_housing.load_data(test_split=0.2, seed=113)

        top = "REG"

    return x_train,y_train,x_test,y_test,top,dataset,classes
