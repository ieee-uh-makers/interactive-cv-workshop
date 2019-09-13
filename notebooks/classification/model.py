from keras.models import Model
from keras.layers import *
from keras.applications import MobileNet
from keras.losses import binary_crossentropy
from keras.metrics import binary_accuracy
import keras.backend as K


def build_model(weights='imagenet'):

    cnn = MobileNet(include_top=False,
                    input_shape=(224, 224, 3),
                    weights=weights,
                    alpha=0.25)

    gap = GlobalAveragePooling2D(name='gap')(cnn.output)
    cls = Dense(1, activation='sigmoid', name='cls')(gap)

    model = Model(inputs=cnn.input, outputs=cls)

    metrics = {'cls': binary_accuracy}
    loss = [binary_crossentropy]

    model.summary()

    return model, metrics, loss
