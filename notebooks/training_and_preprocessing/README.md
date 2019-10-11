# Training

So for the past two weeks we have gone over convolutional neural networks which can classify image and identify where things are in them. But what are the ingredients to put together our own? We need a few things in order to make everything work:

- Data, more is almost always better. It's important that the data is labeled or annotated, so we know what class the image represents or where objects are within it. The quality of the annotation is also important. If we have incorrectly labeled data, it's going to interfere with the machine learning process.
- Neural Network designed for solving the problem at hand. For computer vision, this almost always means taking an off the shelf convolutional neural network and adding some application specific layers to the top (end) of the network.
- A computer powerful enough to run the training process quickly. For computer vision, this almost always means the computer needs a GPU. Currently, it's easier to work with nVidia GPU's than AMD due to software support.


## Training in Practice
So we have all of the ingredients, what else do we need to know?

### Measuring Model Performance

First of all, we need some way to establish how well our model performs at any given point on examples it has never seen before. To accomplish this, we create a train validation split, where we reserve a certain percentage of data only for testing model performance.

### Small Datasets

We don't always have a massive amount of training data. One way we can make our data go farther is data augmentation. To do this, we can do things like flip the image horizontally, rotate it, shift it, crop out sections, and more. See the augmentation.ipynb notebook for examples of this in action!

### Activations and Loss Functions

Selecting the right activations for the last layer of your network and loss functions are key for training an effective network. Heres some general guidelines:

| Task  | Activation  | Loss  |
|---|---|---|
| Binary Classifcation (Two Classes)  | Sigmoid  | Binary Crossentropy  |
| Classification  | Softmax  | Categorical Crossentropy  |
| Regression  | Linear  | Mean Squared Error  |
| Regression  | Linear  | Mean Absolute Error  |

### Batch Size

When we train a network, the optimization process (Mini Batch Stochastic Gradient Descent) provides a subset of training examples to the network for updating the model's weights. If our batch size is too high, we risk overfitting or running out of memory. If it is too low, the model may be slower to converge or converge to a less optimal solution because of noise in the gradient. A good rule for computer vision is use the highest batch size you can without running out of memory.

# Preprocessing

Often we have to do some preprocessing of data before providing it to the network in order to make training work at all, or work better. Here are some of the common strategies.

## Histogram Equalization

Histogram equalization can improve the contrast of an image, emphasizing important information more. There are several techniques that are available, but generally speaking adaptive (local / sliding window) methods work best. The one I would recommend is CLAHE, or contrast limited adaptive histogram equalization. [You can find an overview of the common methods here][histo].

## Data Scaling / Standardization

- Mean Subtraction (Caffe style): The training set mean is calculated and subtracted from each training example before putting it into the network.
- Z-Scoring: Subtract the mean, divide by standard deviation. This could be the mean and standard deviation of the entire dataset, the batch, or the individual training example.
- [-1, 1] (tf style): Divide by half of the maximum possible value, then subtract by one.

Which one is better? It depends on the task at hand, but generally for images its hard to go wrong with one of the  Z-scoring strategies.

[histo]: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
[augnb]: https://github.com/ieee-uh-makers/interactive-cv-workshop/blob/master/notebooks/training_and_preprocessing/augmentation.ipynb
