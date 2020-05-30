import streamlit as st

def select_dataset ():

    dataset = st.selectbox(
    "Select the dataset that you wish to work on ",
        ('MNIST', 'CIFAR-10', 'CIFAR-100', 'IMDB', 'Reuters Newswire','Fashion MNIST','Boston Housing Price')
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

        data = np.concatenate((x_train, x_test), axis=0)
        target = np.concatenate((y_train, y_test), axis=0)

        x_train,y_train = data[10000:],target[10000:]
        x_test,y_test = data[:10000],target[:10000]

        classes = ["Negative", "Positive"]

        top = "NLP"

    elif dataset == 'Reuters Newswire':

        from keras.datasets import reuters

        (x_train, y_train), (x_test, y_test) = reuters.load_data(test_split=0.3)

        classes = ['cocoa','grain','veg-oil','earn','acq','wheat','copper','housing','money-supply',
        'coffee','sugar','trade','reserves','ship','cotton','carcass','crude','nat-gas',
        'cpi','money-fx','interest','gnp','meal-feed','alum','oilseed','gold','tin',
        'strategic-metal','livestock','retail','ipi','iron-steel','rubber','heat','jobs',
        'lei','bop','zinc','orange','pet-chem','dlr','gas','silver','wpi','hog','lead']

        top = "NLP"

    elif dataset == 'Boston Housing Price':

        from keras.datasets import boston_housing

        (x_train, y_train), (x_test, y_test) = boston_housing.load_data(test_split=0.2, seed=113)

        top = "Reg"

    return x_train,y_train,x_test,y_test,top,dataset,classes
