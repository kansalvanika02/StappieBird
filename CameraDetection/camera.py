import cv2
import numpy as np

from deepgaze.color_detection import MultiBackProjectionColorDetector
from deepgaze.mask_analysis import BinaryMaskAnalyser
import keyboard

template_list=list()
template_list.append(cv2.imread('template_1.png')) #Load the image
template_list.append(cv2.imread('template_2.png')) #Load the image
template_list.append(cv2.imread('template_3.png')) #Load the image
template_list.append(cv2.imread('template_4.png')) #Load the image
template_list.append(cv2.imread('template_5.png')) #Load the image
template_list.append(cv2.imread('template_6.png')) #Load the image
# template_list.append(cv2.imread('t1.jpg'))
# template_list.append(cv2.imread('t2.jpg'))
# template_list.append(cv2.imread('t3.jpg'))
# template_list.append(cv2.imread('t4.jpg'))
# template_list.append(cv2.imread('t5.jpg'))

#Open a webcam streaming
video_capture=cv2.VideoCapture(0) #Open the webcam
#Reduce the size of the frame to 320x240
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 420)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 340)
#Get the webcam resolution
cam_w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#Declare an offset that is used to define the distance
#from the webcam center of the two red lines
offset = int(cam_h / 10)

#Declaring the binary mask analyser object
my_mask_analyser = BinaryMaskAnalyser()

#Defining the deepgaze color detector object
my_back_detector = MultiBackProjectionColorDetector()
my_back_detector.setTemplateList(template_list) #Set the template

print("Welcome! Press 'a' to start the hand tracking. Press 'q' to exit...")

while(True):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if(frame is None): break #check for empty frames
    #Return the binary mask from the backprojection algorithm
    frame_mask = my_back_detector.returnMask(frame, morph_opening=True, blur=True, kernel_size=3, iterations=2)
    if(my_mask_analyser.returnNumberOfContours(frame_mask) > 0):
        x_center, y_center = my_mask_analyser.returnMaxAreaCenter(frame_mask)
        x_rect, y_rect, w_rect, h_rect = my_mask_analyser.returnMaxAreaRectangle(frame_mask)
        area = w_rect * h_rect
        cv2.circle(frame, (x_center, y_center), 2, [0,255,0], 5)

        if(y_center > int(cam_h/2)+offset and area>1000) or (y_center < int(cam_h/2)-offset and area>1000):
            print("WAITING")

        else:
            keyboard.press_and_release('space')
            print("Jump")

    #Drawing the offsets
    cv2.line(frame, (0, int(cam_h/2)-offset), (cam_w, int(cam_h/2)-offset), [0,0,255], 1) #horizontal
    cv2.line(frame, (0, int(cam_h/2)+offset), (cam_w, int(cam_h/2)+offset), [0,0,255], 1)

    #Showing the frame and waiting for the exit command
    cv2.imshow('mpatacchiola - deepgaze', frame) #show on window
    cv2.imshow('Mask', frame_mask) #show on window
    if cv2.waitKey(1) & 0xFF == ord('q'): break #Exit when Q is pressed

video_capture.release()
