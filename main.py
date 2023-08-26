import cv2 as cv
import numpy as np
import mediapipe as mp
from screeninfo import get_monitors
from pynput.mouse import Button, Controller

from fingers import THUMB_TIP, INDEX_TIP, RING_TIP, PINKY_TIP

monitors = get_monitors()

if monitors:
    WIDTH = monitors[0].width
    HEIGHT = monitors[0].height
else:
    WIDTH = 1920
    HEIGHT = 1080

cap = cv.VideoCapture(0)
mouse = Controller()
state = ''

hands = mp.solutions.hands.Hands(static_image_mode=False,
                                 max_num_hands=1,
                                 min_tracking_confidence=0.5,
                                 min_detection_confidence=0.5)


def get_distance(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    distance = np.sqrt((x2-x1)**2 + (y2-y1)**2) 

    return distance


while True:
    success, frame = cap.read()

    if success is False:
        break

    frame = cv.flip(frame, 1)
    result = hands.process(frame)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            # Thumb
            xThumb, yThumb = handLms.landmark[THUMB_TIP].x * WIDTH, handLms.landmark[THUMB_TIP].y * HEIGHT

            # Index finger
            xIndex, yIndex = handLms.landmark[INDEX_TIP].x * WIDTH, handLms.landmark[INDEX_TIP].y * HEIGHT
            
            # Ring finger
            xRing, yRing = handLms.landmark[RING_TIP].x * WIDTH, handLms.landmark[RING_TIP].y * HEIGHT 

            # Pinky finger
            xPinky, yPinky = handLms.landmark[PINKY_TIP].x * WIDTH, handLms.landmark[PINKY_TIP].y * HEIGHT 

            # Left mouse button click
            if state == 'LMB':
                # Check if Thumb and middle finger far enough
                if get_distance((xThumb, yThumb), (xPinky, yPinky)) > 70:
                    state = ''
                    mouse.release(Button.left)
                
            elif state != 'LMB':
                # Check if Thumb and middle finger close enough
                if get_distance((xThumb, yThumb), (xPinky, yPinky)) < 70:
                    state = 'LMB'
                    mouse.press(Button.left)

            # Right mouse button click
            if state == 'RMB':
                # Check if Thumb and ring finger far enough
                if get_distance((xThumb, yThumb), (xRing, yRing)) > 70:
                    state = ''
                    mouse.release(Button.right)
                
            elif state != 'RMB':
                # Check if Thumb and ring finger close enough
                if get_distance((xThumb, yThumb), (xRing, yRing)) < 70:
                    state = 'RMB'
                    mouse.press(Button.right)

            # Move pointer
            alpha = 0.5
            current_x, current_y = mouse.position
            x = (1 - alpha) * current_x + alpha * xIndex
            y = (1 - alpha) * current_y + alpha * yIndex

            mouse.position = (x, y)
                
    cv.imshow('Camera', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
