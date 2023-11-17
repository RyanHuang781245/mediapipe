import cv2
import numpy as np

videoLeftUp = cv2.VideoCapture('./output_video_0.mp4')
videoLeftDown = cv2.VideoCapture('./output_video_2.mp4')
videoRightUp = cv2.VideoCapture('./output_video_1.mp4')

fps = videoLeftUp.get(cv2.CAP_PROP_FPS)

width = int(videoLeftUp.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoLeftUp.get(cv2.CAP_PROP_FRAME_HEIGHT))

videoWriter = cv2.VideoWriter('./out.MP4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))

successLeftUp, frameLeftUp = videoLeftUp.read()
successLeftDown, frameLeftDown = videoLeftDown.read()
successRightUp, frameRightUp = videoRightUp.read()

while successLeftUp and successLeftDown and successRightUp:
    frameLeftUp = cv2.resize(frameLeftUp, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    frameLeftDown = cv2.resize(frameLeftDown, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    frameRightUp = cv2.resize(frameRightUp, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    frameUp = np.hstack((frameLeftUp, frameRightUp))
    frameDown = np.hstack((frameLeftDown, np.zeros_like(frameRightUp)))  # Add a black frame for the missing video
    frame = np.vstack((frameUp, frameDown))

    videoWriter.write(frame)
    successLeftUp, frameLeftUp = videoLeftUp.read()
    successLeftDown, frameLeftDown = videoLeftDown.read()
    successRightUp, frameRightUp = videoRightUp.read()

videoWriter.release()
videoLeftUp.release()
videoLeftDown.release()
videoRightUp.release()
