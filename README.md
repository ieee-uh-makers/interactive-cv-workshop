# IEEE Makers Interactive CV Workshop

Welcome to the Interactive Computer Vision Workshop! The point of these workshops are to be able to get your hands on some advanced computer vision algorithms with little prior knowledge of programming or computer vision. We will cover many different techniques, going through each individual part of the algorithm in an interactive fashion. While we will mostly stay at a high level, feel free to ask questions about specific implementation details in the code.

## Planned Workshops
- Motion Detection
- Obstacle Avoidance (Classification)
- Object Detection (Regression)
- Preprocessing Techniques
- End-to-End training of a neural network for obstacle avoidance

## General Info

- While no prior programming experience is required for most of these workshops, we do recommend having some basic familiarity with programming languages such as MATLAB or C.
- We will be using the Anaconda distribution of python for each workshop, which can be downloaded here: https://www.anaconda.com/distribution. Make sure you choose the Python 3.7 version of Anaconda.

## Installing Anaconda
### Windows

- Make sure you download the correct Anaconda installer for your operating system, by default the MacOS installer is selected.
- Once Anaconda is installed, open Conda Navigator
- Go to the environments tab, create a new Python 3.7 environment called "cv"
- Make sure the "cv" environment is selected in the environment dropdown
- On the packages dropdown menu, select "Not Installed" and search for / install: 
```
opencv
py-opencv
jupyter
ipywidgets
tensorflow
keras
```
- Go back to the "Home" tab, and start Jupyter Notebook.

### MacOS / Linux
- When installing anaconda, make sure you choose yes when it asks if you want to run conda init
- You may need to manually start Jupyter notebook like so if you get crashes:
```bash
export KMP_DUPLICATE_LIB_OK=TRUE
conda activate cv
jupyter notebook
```