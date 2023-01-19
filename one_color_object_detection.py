# https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/
# https://www.geeksforgeeks.org/real-time-object-color-detection-using-opencv/

"""
CS180DA - Lab 0

Created by: Jillian Pantig
Description: Object Color Tracking with Bounding Box using RGB/HSV

Credits: GeeksForGeeks and OpenCV

"""

import numpy as np
import cv2

def rgb_or_hsv():
    user_input=input("Enter 'R' to use RGB or 'H' to use HSV: ")

    if user_input.upper() == 'H':
        return 0
    elif user_input.upper() == 'R':
        return 1
    
    return -1

def get_color_values(user_input):
                    # Lower     # Upper
    color_values = [[[0,95,90],[6,244,253]],       # HSV
                   [[214,6,6], [255,120,120]]]   # RGB
    return color_values[user_input]

def get_color_scale(user_input):
    color_scale = [cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2RGB]
    return color_scale[user_input]

def resize(frame):
    """
    Function for resizing the frame,
    Parameter: Image Frame
    """
    return cv2.resize(frame, (800, 600))

def draw_bounding_box(contours, imageFrame):
    """
    Function for drawing bounding box on the frame
    Parameters: Contours and Image Frame
    """
    for _, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 2000): # Make the area larger so it does not detect smaller objects
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "Red Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

def main():
    user_input = rgb_or_hsv()
    color_values = get_color_values(user_input)
    color_scale = get_color_scale(user_input)
    print(color_values)
    print(color_scale)

    # Using the webcam
    webcam = cv2.VideoCapture(0)

    ret, imageFrame = webcam.read()

    # Start a while loop until ret fails or until user terminates the program
    while ret:

        ret, imageFrame = webcam.read()
    
        # Convert the imageFrame in BGR to HSV
        hsvFrame = cv2.cvtColor(imageFrame, color_scale)
    
        l_limit=np.array(color_values[0]) # setting the color lower limit
        u_limit=np.array(color_values[1]) # setting the color upper limit

        color_mask = cv2.inRange(hsvFrame, l_limit, u_limit)
        
        # Using Dilation to reduce noise
        kernel = np.ones((5, 5), "uint8")
        
        color_mask = cv2.dilate(color_mask, kernel)
        oject_isoslate = cv2.bitwise_and(imageFrame, imageFrame, mask = color_mask)
    
        # Creating contour to put box and track red color
        contours, _ = cv2.findContours(color_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)    
        draw_bounding_box(contours, imageFrame)          

        # Show the Frame
        cv2.imshow("Color Blob Detection with Bounding Box", resize(imageFrame))
        cv2.imshow('Isolating Objects with Specified Color',resize(oject_isoslate)) # to display the blue object output

        # Terminate the program by pressing 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

if __name__=='__main__':
    main()