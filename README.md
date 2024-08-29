<h1> Fall Detection</h1>

Using Tiny-YOLO oneclass to detect each person in the frame and use 
[AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) to get skeleton-pose and then use
[ST-GCN](https://github.com/yysijie/st-gcn) model to predict action from every 30 frames 
of each person tracks.

- Python > 3.6
- Pytorch > 1.3.1
Instruction to install pytorch can be found here- https://pytorch.org/get-started/locally/

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
## Reference

- AlphaPose : https://github.com/Amanbhandula/AlphaPose
- ST-GCN : https://github.com/yysijie/st-gcn
