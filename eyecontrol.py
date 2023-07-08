import cv2
import mediapipe as mp
import pyautogui

#detecting the first video capturing device
cam=cv2.VideoCapture(0) 
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

#dimensions of the screen
screen_w, screen_h=pyautogui.size()

#since vid is trunning cont. this loop is running forever
while True:
    #has to read ever frame so 1st var. is ignored
    _, frame=cam.read()

    #lateral inversion correction
    frame=cv2.flip(frame,1)
    #Converts the color to easier colors in order to execute
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    #processes the face
    output=face_mesh.process(rgb_frame)

    #assigns points on certain points of the face
    landmark_points=output.multi_face_landmarks

    #getting frame width and height
    frame_h,frame_w, _= frame.shape

    #print(landmark_points)
    if landmark_points:
        #detects only one face
        landmarks=landmark_points[0].landmark
        #draw points on face
        for id,landmark in enumerate(landmarks[474:478]):
            #detects only length and width of the face(x,y)
            x=int(landmark.x*(frame_w))
            y=int(landmark.y*(frame_h)) 
            cv2.circle(frame,(x,y),3,(0,255,0))

            #Enables mouse
            if id== 1:
                screen_x=(screen_w/frame_w)*x
                screen_y=(screen_h/frame_h)*y
                pyautogui.moveTo(screen_x, screen_y)

        #clicking from left eye
            left=[landmarks[145],landmarks[159]]
            for landmark in left:          
                x=int(landmark.x*(frame_w))
                y=int(landmark.y*(frame_h)) 
                cv2.circle(frame,(x,y),3,(0,255,255))
            if(left[0].y-left[1].y)<0.004:
                pyautogui.click()
                pyautogui.sleep(1)

    cv2.imshow('Eye Control Mouse',frame)
    cv2.waitKey(1)




