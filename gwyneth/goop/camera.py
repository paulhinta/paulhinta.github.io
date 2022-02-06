import cv2
import numpy as np
import cv2
import numpy as np
import glob
import os
import dlib

#image read
imgMustache = cv2.imread("mustache.png", -1)
orig_mask = imgMustache[:,:,3]
orig_mask_inv = cv2.bitwise_not(orig_mask)
imgMustache = imgMustache[:,:,0:3]
origMustacheHeight, origMustacheWidth = imgMustache.shape[:2]

#image read 
imgGlass = cv2.imread("glasses.png", -1)
orig_mask_g = imgGlass[:,:,3]
orig_mask_inv_g = cv2.bitwise_not(orig_mask_g)
imgGlass = imgGlass[:,:,0:3]
origGlassHeight, origGlassWidth = imgGlass.shape[:2]

# 68 point detector on face
predictor_path = "shape_predictor_68_face_landmarks.dat"
# face detection modal
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
cnn_face_detector=dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
detector=dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def __del__(self):
        self.cap.release()
    def get_frame(self):
        ret, frame = self.cap.read()
        dets = cnn_face_detector(frame, 1) 
        frame_flip = cv2.flip(frame, 1)
        ret, frame = cv2.imencode('.jpg', frame_flip)
        for k, d in enumerate(dets):  
            shape = predictor(frame, d.rect)
        return frame.tobytes()
