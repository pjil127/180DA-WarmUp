# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

import numpy as np 
import cv2
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    dom_per = 0
    dom_color = []

    for (percent, color) in zip(hist, centroids):
        if percent > dom_per:
            dom_per = percent
            dom_color = color

    cv2.rectangle(bar, (int(0), 0), (int(300), 50),
                    dom_color.astype("uint8").tolist(), -1)

    # return the bar chart
    return bar

def resize(frame):
    """
    Function for resizing the frame,
    Parameter: Image Frame
    """
    return cv2.resize(frame, (800, 600))

def main():
    webcam = cv2.VideoCapture(0)

    ret, imageFrame = webcam.read()
    while(ret):
        ret, imageFrame = webcam.read()

        if ret==True:        
            x, y, w, h = 250, 150, 400, 200
            imageFrame = cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,255,0),2)
            roi = imageFrame[150:350, 250:650].copy()
            
            img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
            clt = KMeans(n_clusters=4) #cluster number
            clt.fit(img)

            hist = find_histogram(clt)
            bar = plot_colors2(hist, clt.cluster_centers_)

            bar = cv2.cvtColor(bar, cv2.COLOR_RGB2BGR)

            #Display the resulting frame
            cv2.imshow('Frame', resize(imageFrame))
            cv2.imshow('Dominant Color', bar)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    webcam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()