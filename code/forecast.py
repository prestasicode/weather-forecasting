# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:52:48 2023

@author: ferisa.prestasi
"""

# Data manipulation
import pandas as pd # for data manipulation
print('pandas: %s' % pd.__version__) # print version
import numpy as np # for data manipulation
print('numpy: %s' % np.__version__) # print version
import math # to help with data reshaping of the data

# Visualization
import plotly 
import plotly.express as px
import plotly.graph_objects as go
print('plotly: %s' % plotly.__version__) # print version

# Tensorflow / Keras
from tensorflow import keras # for building Neural Networks
print('Tensorflow/Keras: %s' % keras.__version__) # print version
from keras.models import Sequential # for creating a linear stack of layers for our Neural Network
from keras import Input # for instantiating a keras tensor
from keras.layers import Dense, SimpleRNN # for creating regular densely-connected NN layers and RNN layers

# Sklearn
import sklearn # for model evaluation
print('sklearn: %s' % sklearn.__version__) # print version
from sklearn.model_selection import train_test_split # for splitting the data into train and test samples
from sklearn.metrics import mean_squared_error # for model evaluation metrics
from sklearn.preprocessing import MinMaxScaler # for feature scaling

import pandas as pd
data = pd.read_csv("acc_data.csv", index_col="Tanggal")
data.apply(pd.isnull).sum()/data.shape[0]

core_weather = data[["Tx", "Tx", "Tavg", "RH_avg", "RR", "ss", "ff_x", "ddd_x", "ff_avg", "ddd_car"]].copy()
core_weather.columns = ["temp_min", "temp_max", "temp_avg", "humidity", "precipitation", "sunshine", "wind_speed_max", "wind_direction", "wind_speed_avg", "wind_dir_max"]