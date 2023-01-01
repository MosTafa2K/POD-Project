# Welcome to POD Project

For full documentation visit [POD Project Docs](https://mostafa2k.github.io/podprojectdocs/).

## Overview

**POD (Synonymous for Python Object Detection)** project usefull to determin and detect objects in **Images**, **Videos** and also **WebCam** like cat, dog, car and etc!

Basically, this project is used as an api for projects used to detect objects. POD Project have two part :

- UserInterface
- Core

**Core** can be used without **UI** in your project. The **UI** is used to make it look more beautiful and have a better feeling when working in this project!

In **UI** we used [flet](https://github.com/flet-dev/flet) framework to have a fantasy UI!

POD used **ONNX Models** and **YOLOv7 algorithm** for train, object localization and object detection

## What is ONNX Models ?

ONNX is an intermediary machine learning framework used to convert between different machine learning frameworks. So let's say you're in TensorFlow, and you want to get to TensorRT, or you're in PyTorch, and you want to get to TFLite, or some other machine learning framework. ONNX is a good intermediary to use to convert your model as you're going through these different machine learning frameworks.
ONNX has worked really hard to basically implement all kinds of different neural network functions and different functionalities in these machine learning models, so we can support this cross functionality to have baseline, common framework to convert into.
There are several ways in which you can obtain a model in the ONNX format, including: ONNX Model Zoo: Contains several pre-trained ONNX models for different types of tasks. [Read More](https://onnx.ai/)

## What is YOLOv7 algorithm ?

YOLO (“You Only Look Once”) is an effective real-time object recognition algorithm, first described in the seminal 2015 paper by Joseph Redmon et al.
Since the release of YOLOv1 in 2015, the algorithm has gained immense popularity among the computer vision community. Furthermore, the updated version of the model YOLOv2, YOLOv3, YOLOv4, YOLOv5, YOLOv6, and very much recently, YOLOv7 has been released so far. Note that YOLOv5 has been one of the most successful and commonly used versions of the YOLO series. So the same team creating the updated version is a reason to consider learning it. Yolov7 is a real-time object detector currently revolutionizing the computer vision industry with its incredible features. The official YOLOv7 provides unbelievable speed and accuracy compared to its previous versions. Yolov7 weights are trained using Microsoft’s COCO dataset, and no pre-trained weights are used. [Read More](https://learnopencv.com/yolov7-object-detection-paper-explanation-and-inference/)


## Most commonly frameworks and other tools that used in this project is :

* Numpy: 1.23.5
* opencv-python: 4.6.0.66
* Sympy: 1.11.1
* Onnxruntime: 1.13.1
* Pillow: 9.3.0
* flet: 0.2.4

> Note: For using this project you will need **Python 3.8** or later!

