import cv2
import numpy as np
# Read the image
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def crop_image(input_image_path,output_image_path,code = False):

    img = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edged = cv2.Canny(gray, 30, 200)

    # Find contours
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    overall_min = np.array([np.inf, np.inf])
    overall_max = np.array([-np.inf, -np.inf])

    for contour in contours:
        cnt = contour.reshape(-1,2)
        mino = np.min(cnt[:,0],axis=0)
        print(cnt[:,1])
        maxo = np.max(cnt,axis=0)
        return
        overall_min = np.minimum(overall_min,mino)
        overall_max = np.maximum(overall_max, maxo)

    print(overall_min,overall_max)


    # Sort contours by area, keeping only the largest one
    c = max(contours, key=cv2.contourArea)


    # Get the bounding box coordinates of the largest contour
    x, y, w, h = int(overall_min[0]), int(overall_min[1]), int(overall_max[0]-overall_min[0]), int(overall_max[1]-overall_min[1])



    # Crop the image using the bounding box coordinates
    if code:
        cropped_img = img[y+5:y+h-10, x+5:x+w-5]
    else:
        cropped_img = img[y+50:y+h+50, x+50:x+w+50]

    # Save the cropped image
    cv2.imwrite(output_image_path, cropped_img)

    # Display the cropped image (optional)
    # cv2.imshow('Cropped Image', cropped_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
crop_image("main.png","main2.png")
