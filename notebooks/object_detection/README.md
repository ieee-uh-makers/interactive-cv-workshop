# Object Detection with Neural Networks

Todays workshop will cover the basics of object detection with neural networks. What is object detection you ask?

![Object Detection](squirrel.png)

Simply put, object detection is the localization of an object within an image. How object detect works with neural networks is very similar to object classication. We take an input image, put it into a neural network, and make a prediction. Remember how information flows through a classification network, starting with an image:

## Classification Network
|   | Input  | Output |
|---|---|---|
| Convolutional Neural Network  | 224x224x3 Image | 7x7x256 Feature Map  |
| Classification Layer (Top)  | 7x7x256 Feature Map  | Probability of Class Present in Image  |

Our detection network has two different outputs.

### Neural Network Terminology: Top

Top essentially means the end of the network, where the network outputs its prediction, and there are no additional layers after. It is common practice to take a convolutional neural network trained for a certain task, remove the top layers and replace them with something else and run training on the new task using the weights from a different task as a starting point. This is called "transfer learning", and often results in training taking far less time / require less data than starting from scratch.

## Detection Network
|   | Input  | Output |
|---|---|---|
| Convolutional Neural Network  | 224x224x3 Image | 7x7x256 Feature Map  |
| Classification Layer (Top)  | 7x7x256 Feature Map  | 7x7 Probability Grid |
| Detection Layer (Top) | 7x7x256 Feature Map | 7x7x4 Bounding Boxes (X, Y, Width, Height) |

### Object Detection in Action

Here we can see the two layers in action. The colored squares are the class probabilities overlayed on the original image, and the green rectangle is the bounding box predicted by the network.

![Object Detection](example.jpg)
