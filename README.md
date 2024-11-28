# Webcam game controller
## Contents
1. [Introduction](#introduction)
2. [Run the aplication](#run-the-application)
3. [Usage](#usage)
4. [Threads structure](#threads-structure)
5. [Author](#author)

## Introduction
A multi-threaded, webcam-based game controller that utilizes body and hand gestures to seamlessly emulate keyboard and mouse functionality.

[![Demo](https://i.ytimg.com/vi/IIvClNtovDs/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZCg1MA8=&rs=AOn4CLCT_Ceme8Qy61T_AvFiOXoRj0IlPQ&quot)](https://www.youtube.com/watch?v=IIvClNtovDs)
<div align="center">
    Video: A demo of the application.
</div>


### Used technology:
- Python,
- MediaPipe,
- Numpy,
- Pynput.

## Run the application
Run the `python3 main.py` command in the `Webcam-game-controller` directory:

## Usage
1. Click "Start Program" in the menu. Optionally, adjust the keybinds or mouse settings.
2. Stand far enough from the webcam so that your entire body is visible in the preview.
3. To quit the application, click the "X" on the window.

## Threads structure

<div align="center">
    <img src="https://i.imgur.com/SwFb62s.png" alt="Threads diagram">
    Image: Application threads diagram.
</div>

### Threads:
- `Pose detection thread`:  The application's main thread. It predicts body landmarks and passes them to the __Body landmarks__ and __Right hand Landmarks Queue__. This thread also starts other threads.
- `Keyboard emulation thread`: Calculates body and left hand gestures and emulates keyboard functionality.
- `Mouse action calculation thread`:
Calculates right hand gestures and pointer movement based on right wrist coordinates, then passes this information to the __Pointer emulation thread__  through the __Pointer queue__.
- `Pointer emulation thread`: Emulates pointer movement and mouse functionality based on screen refresh rate.

## Author
* ### Mateusz Domino: [LinkedIn](https://www.linkedin.com/in/mateusz-domino)
* ### Email: [matdomino@outlook.com](mailto:matdomino@outlook.com)