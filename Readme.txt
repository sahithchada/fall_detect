Fall Detection
This repository contains code for fall detection, capable of running on both GPU (with CUDA support) and CPU. The program analyzes input data to detect falls in real-time.

Prerequisites
For GPU execution, ensure your system has a CUDA-supported GPU and that CUDA drivers are properly installed.
For CPU execution, no special hardware requirements are needed.

Installation
Download this repository to your local machine:

Running the Fall Detection Program-

Using GPU (with CUDA support)
If your system has a GPU with CUDA support, follow these steps to run the fall detection program:

1)Open the directory in your terminal:
cd fall_detect_x64_package
2)Make the GPU executable file runnable (this needs to be done only once):
chmod +x fall_detect_gpu
3)Run the GPU version of the fall detection program:
./fall_detect_gpu

Using CPU
If you are using a CPU, follow these steps to run the fall detection program:

1)Open the directory in your terminal:
cd fall_detect_x64_package
2)Make the CPU executable file runnable (this needs to be done only once):
chmod +x fall_detect_cpu
3)Run the CPU version of the fall detection program:
./fall_detect_cpu

Additional Information
The program will output the detection results to a seperate window.

