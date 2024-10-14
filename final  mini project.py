#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
from fer import FER 
import matplotlib.pyplot as plt

video_capture = cv2.VideoCapture(0)

emotion_detector = FER(mtcnn=True) 
while True:

    ret, frame = video_capture.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    

    emotions = emotion_detector.detect_emotions(rgb_frame)
   
    for result in emotions:
    
        bounding_box = result["box"]
        emotion_predictions = result["emotions"]
        
        
    
        top_emotion = max(emotion_predictions, key=emotion_predictions.get)

    
        (x, y, w, h) = bounding_boxz
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
        text = f"{top_emotion}: {emotion_predictions[top_emotion]:.2f}"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

  
    cv2.imshow('Live Emotion Detection', frame)

   
    key = cv2.waitKey(1) & 0xFF
    if key == ord('z') or key == 27: 
        break


video_capture.release()
cv2.destroyAllWindows()


# In[ ]:




