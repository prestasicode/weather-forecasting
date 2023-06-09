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

#env-output-googlecolaboratory
#pandas: 1.5.3
#numpy: 1.22.4
#plotly: 5.13.1
#Tensorflow/Keras: 2.12.0
#sklearn: 1.2.2

data = pd.read_csv("acc_data.csv", index_col="Tanggal")
data.apply(pd.isnull).sum()/data.shape[0]

dataset = data[["Tx", "Tx", "Tavg", "RH_avg", "RR", "ss", "ff_x", "ddd_x", "ff_avg", "ddd_car"]].copy()
dataset.columns = ["temp_min", "temp_max", "temp_avg", "humidity", "precipitation", "sunshine", "wind_speed_max", "wind_direction", "wind_speed_avg", "wind_dir_max"]

#EDA
fig1 = px.line(data, x="date", 
                 y="temp_max", 
                 title='Mean Temperature in Tangerang Over the Years')
fig.show()

fig2 = px.line(data, x="date", 
                 y="humidity", 
                 title='Humidity in Tangerang Over the Years')
fig2.show()

#analyze data
data["date"] = pd.to_datetime(data["date"], format = '%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
print(data.head())

#tensorflow library
def wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=260): # 260 is used as we have approx 570 dataset for training
    return tf.estimator.inputs.pandas_input_fn(x=X,
                                               y=y,
                                               num_epochs=num_epochs,
                                               shuffle=shuffle,
                                               batch_size=batch_size)
evaluations = []
STEPS = 260
for i in range(100):
    regressor.train(input_fn=wx_input_fn(X_train, y=y_train), steps=STEPS)
    evaluation = regressor.evaluate(input_fn=wx_input_fn(X_val, y_val,
                                                         num_epochs=1,
                                                         shuffle=False),
                                    steps=1)
    evaluations.append(regressor.evaluate(input_fn=wx_input_fn(X_val,
                                                               y_val,
                                                               num_epochs=1,
                                                               shuffle=False)))

#keras library
from transformers import TrainingArguments, Trainer

epochs = 5
batch_size = 512

# Define our training job.
training_args = TrainingArguments(
    output_dir="checkpoints",
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=epochs,
    logging_strategy="epoch",
    evaluation_strategy="epoch",
)
trainer = Trainer(
    model,
    training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

# Run the training job.
trainer.train()

# Pipeline for save model
trainer.save_model("model")
!ls -lh model
