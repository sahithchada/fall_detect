<<<<<<< HEAD
<h1> Fall Detection</h1>

This repository contains a model designed to predict human actions in video scenes, specifically focusing on detecting falls. The model analyzes video frames in segments of 30 frames and can be used to trigger alerts via text messages, sound signals, or other workflows when a fall is detected.

## Requirements
- Python > 3.6
- Pytorch > 1.3.1
Instruction to install pytorch can be found here- https://pytorch.org/get-started/locally/

## Pre-Trained Models
The pre-trained model can be found here- https://drive.google.com/drive/folders/1g-SsldFl8_VOpoGvFXFHJoLz2B_Gjjsg?usp=drive_link
=======
# Fall Detection

This repository contains code for fall detection, capable of running on both GPU (with CUDA support) and CPU. The program analyzes input data to detect falls in real time.

## Prerequisites

- **GPU Execution**: Ensure your system has a CUDA-supported GPU and that CUDA drivers are properly installed.
- **CPU Execution**: No special hardware requirements are needed.

## Installation

Download this repository to your local machine.

## Running the Fall Detection Program

### Using GPU (with CUDA support)

If your system has a GPU with CUDA support, follow these steps to run the fall detection program:

1. Open the directory in your terminal:
   ```bash
   cd fall_detect_x64_package
   ```
2. Make the GPU executable file runnable (this needs to be done only once):
   ```bash
   chmod +x fall_detect_gpu
   ```
3. Run the GPU version of the fall detection program:
   ```bash
   ./fall_detect_gpu
   ```
>>>>>>> a9c2ff4 (added telegram messages)

### Using CPU

<<<<<<< HEAD
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
=======
If you are using a CPU, follow these steps to run the fall detection program:

1. Open the directory in your terminal:
   ```bash
   cd fall_detect_x64_package
   ```
2. Make the CPU executable file runnable (this needs to be done only once):
   ```bash
   chmod +x fall_detect_cpu
   ```
3. Run the CPU version of the fall detection program:
   ```bash
   ./fall_detect_cpu
   ```

## Additional Information

The program will output the detection results to a separate window.
>>>>>>> a9c2ff4 (added telegram messages)
