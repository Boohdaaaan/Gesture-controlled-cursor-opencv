# Gesture-controlled pointer | OpenCV, Mediapipe

Introducing my pet project! This program enables real-time webcam-based hand gesture recognition. It smoothly controls cursor movement via finger tracking and ingeniously simulates mouse clicks using finger touches. The project brilliantly demonstrates human-computer interaction possibilities.

## Usage

### Requirements
* Python 3

### Setup
* Clone repository
```bash
  git clone https://github.com/Boohdaaaan/Gesture-controlled-pointer-opencv.git
```

* Move to project folder
```bash
  cd Gesture-controlled-pointer-opencv
```

* Install dependencies
```bash
  pip install -r requirements.txt
```

* Run the main file
```bash
  python main.py
```

### How to Interact with the Project

The program allows you to interact with the cursor and perform mouse clicks using specific hand gestures.  After launching the main file, the video from your webcam will appear on your screen.  

1. **Pointer Movement:** Move your index finger to control the cursor's movement on the screen.  
   
   ![Pointer Movement](gifs/Pointer_movement_1.gif)
   ![Pointer Movement](gifs/Pointer_movement_2.gif)  
   
2. **Left Mouse Click:** Touch your thumb and pinky finger together to simulate a left mouse button click. 
    
   ![Left Mouse Click](gifs/Left_mouse_button_1.gif)
   ![Left Mouse Click](gifs/Left_mouse_button_2.gif)

3. **Right Mouse Click:** Touch your thumb and ring finger together to simulate a right mouse button click.  
   
   ![Right Mouse Click](gifs/Right_mouse_button.gif)

4. **Hold left or right mouse button:** Touch your thumb and small finger together and don't let go.  
   
   ![Hold left mouse button](gifs/Drag_file.gif)
   ![Hold left mouse button](gifs/Select_files.gif)  


