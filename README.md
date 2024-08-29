<h1> Fall Detection</h1>

This repository contains a model designed to predict human actions in video scenes, specifically focusing on detecting falls. The model analyzes video frames in segments of 30 frames and can be used to trigger alerts via text messages, sound signals, or other workflows when a fall is detected.

## Requirements
- Python > 3.6
- Pytorch > 1.3.1
Instruction to install pytorch can be found here- https://pytorch.org/get-started/locally/

## Pre-Trained Models
The pre-trained model can be found here- https://drive.google.com/drive/folders/1g-SsldFl8_VOpoGvFXFHJoLz2B_Gjjsg?usp=drive_link

## Basic Use

1. Download all pre-trained models into ./Models folder.
2. Run main.py
```
    python main.py ${video file or camera source}
```
## With face blur
```
    python blur_face_and_detect.py ${video file or camera source}
```
## To Package the Model
1. Install pyinstaller
```
    pip install pyinstaller
```
2. run main.spec
```
    pyinstaller main.spec
```
