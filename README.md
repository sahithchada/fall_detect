# Fall Detection

This repository contains code for fall detection, capable of running on both GPU (with CUDA support) and CPU. The program analyzes input data to detect falls in real time.

## Prerequisites

- **GPU Execution**: Ensure your system has a CUDA-supported GPU and that CUDA drivers are properly installed. Refer- https://docs.nvidia.com/cuda/cuda-installation-guide-linux/
- **CPU Execution**: No special hardware requirements.

# Running Fall Detection From Source

## Installation

Clone this repository to your local machine-
   ```bash
   git clone https://github.com/sahithchada/fall_detect.git
   ```
Install all the requirements using-

   ```bash
   pip3 install -r requirements.txt
   ```
Downloading the model
   Download the weights from google drive link below and place it inside Models directory-
   ```bash
   https://drive.google.com/drive/folders/1rZit5YD-Cvx_lhvEKrE5iPIRsNzR6Lir?usp=sharing
   ```
Running Source Code
   ```bash
   python3 blur_face_and_detect.py
   ```

# Running the Fall Detection Program From Spec File

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

### Using CPU

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
