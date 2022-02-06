import cv2
import numpy as np
import cv2
import numpy as np
import glob
import os
import dlib

#image read
imgMustache = cv2.imread("/Users/imanechafi/restoration/gwyneth/goop/mustache.png", -1)
orig_mask = imgMustache[:,:,3]
orig_mask_inv = cv2.bitwise_not(orig_mask)
imgMustache = imgMustache[:,:,0:3]
origMustacheHeight, origMustacheWidth = imgMustache.shape[:2]

#image read 
imgGlass = cv2.imread("/Users/imanechafi/restoration/gwyneth/goop/glasses.png", -1)
orig_mask_g = imgGlass[:,:,3]
orig_mask_inv_g = cv2.bitwise_not(orig_mask_g)
imgGlass = imgGlass[:,:,0:3]
origGlassHeight, origGlassWidth = imgGlass.shape[:2]

# 68 point detector on face
predictor_path = "/Users/imanechafi/restoration/gwyneth/goop/shape_predictor_68_face_landmarks.dat"
# face detection modal
face_rec_model_path = "/Users/imanechafi/restoration/gwyneth/goop/dlib_face_recognition_resnet_model_v1.dat"

cnn_face_detector=dlib.cnn_face_detection_model_v1("/Users/imanechafi/restoration/gwyneth/goop/mmod_human_face_detector.dat")
detector=dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def __del__(self):
        self.cap.release()
    def get_frame(self):
        ret, frame = self.cap.read()
        frame_flip = cv2.flip(frame, 1)
        ret, frame = cv2.imencode('.jpg', frame_flip) ##Video rect and frame 
        return frame.tobytes()

        dets = cnn_face_detector(frame, 1)
        while ret:
            dets = cnn_face_detector(frame, 1)
            for k, d in enumerate(dets):
                shape = predictor(frame, d.rect)
        
                mustacheWidth = abs(3 * (shape.part(31).x - shape.part(35).x))
                mustacheHeight = int(mustacheWidth * origMustacheHeight / origMustacheWidth) - 10
                mustache = cv2.resize(imgMustache, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
                mask = cv2.resize(orig_mask, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
                mask_inv = cv2.resize(orig_mask_inv, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
                y1 = int(shape.part(33).y - (mustacheHeight/2)) + 10
                y2 = int(y1 + mustacheHeight)
                x1 = int(shape.part(51).x - (mustacheWidth/2))
                x2 = int(x1 + mustacheWidth)
                roi = frame[y1:y2, x1:x2]
                roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
                roi_fg = cv2.bitwise_and(mustache,mustache,mask = mask)
                frame[y1:y2, x1:x2] = cv2.add(roi_bg, roi_fg)

                glassWidth = abs(shape.part(16).x - shape.part(1).x)
                glassHeight = int(glassWidth * origGlassHeight / origGlassWidth)
                glass = cv2.resize(imgGlass, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
                mask = cv2.resize(orig_mask_g, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
                mask_inv = cv2.resize(orig_mask_inv_g, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
                y1 = int(shape.part(24).y)
                y2 = int(y1 + glassHeight)
                x1 = int(shape.part(27).x - (glassWidth/2))
                x2 = int(x1 + glassWidth)
                roi1 = frame[y1:y2, x1:x2]
                roi_bg = cv2.bitwise_and(roi1,roi1,mask = mask_inv)
                roi_fg = cv2.bitwise_and(glass,glass,mask = mask)
                frame[y1:y2, x1:x2] = cv2.add(roi_bg, roi_fg)
                #'''
