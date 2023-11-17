# encoding:utf-8

import cv2
import mediapipe as mp
import math

def cal_ang(point_1, point_2, point_3): # 計算角度
    a=math.sqrt((point_2[0]-point_3[0])*(point_2[0]-point_3[0])+(point_2[1]-point_3[1])*(point_2[1] - point_3[1]))
    b=math.sqrt((point_1[0]-point_3[0])*(point_1[0]-point_3[0])+(point_1[1]-point_3[1])*(point_1[1] - point_3[1]))
    c=math.sqrt((point_1[0]-point_2[0])*(point_1[0]-point_2[0])+(point_1[1]-point_2[1])*(point_1[1]-point_2[1]))
    A=math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
    B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
    C=math.degrees(math.acos((c*c-a*a-b*b)/(-2*a*b)))
    return B

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

input_video_path = './GX010099.mp4'
output_video_path = 'output_video.mp4'

cap = cv2.VideoCapture(input_video_path)

video_width = int(cap.get(3))
video_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter(output_video_path, fourcc, 30, (video_width, video_height))

selected_keypoints = [mp_pose.PoseLandmark.RIGHT_HIP,mp_pose.PoseLandmark.RIGHT_KNEE,mp_pose.PoseLandmark.RIGHT_ANKLE,
                      mp_pose.PoseLandmark.LEFT_HIP,mp_pose.PoseLandmark.LEFT_KNEE,mp_pose.PoseLandmark.LEFT_ANKLE,
                      mp_pose.PoseLandmark.RIGHT_SHOULDER,mp_pose.PoseLandmark.RIGHT_HIP,mp_pose.PoseLandmark.RIGHT_KNEE,
                      mp_pose.PoseLandmark.LEFT_SHOULDER,mp_pose.PoseLandmark.LEFT_HIP,mp_pose.PoseLandmark.LEFT_KNEE,
                      mp_pose.PoseLandmark.RIGHT_KNEE,mp_pose.PoseLandmark.RIGHT_ANKLE,mp_pose.PoseLandmark.RIGHT_FOOT_INDEX,
                      mp_pose.PoseLandmark.LEFT_KNEE,mp_pose.PoseLandmark.LEFT_ANKLE,mp_pose.PoseLandmark.LEFT_FOOT_INDEX
                      ]

with mp_pose.Pose(
    model_complexity=2, #  0表示 速度最快，精度最低；1表示 速度中间，精度中间；2 表示 速度最慢，精度最高；
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Cannot open video")
        exit()

    count = 0
    while True:
        ret, img = cap.read()
        if not ret:
            print("End of video")
            break
        img = cv2.resize(img, (video_width, video_height))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img_rgb)

        if results.pose_landmarks:
            selected_keypoints_coordinates = []
            for landmark in selected_keypoints:
                landmark_point = results.pose_landmarks.landmark[landmark]
                x, y = landmark_point.x, landmark_point.y

                # 將攝像機座標轉換為螢幕座標
                screen_x = int(x * video_width)
                screen_y = int(y * video_height)

                selected_keypoints_coordinates.append((screen_x, screen_y))

            mp_drawing.draw_landmarks(
                img,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS)
            
            x0 = selected_keypoints_coordinates[0]
            x1 = selected_keypoints_coordinates[1]
            x2 = selected_keypoints_coordinates[2]

            x3 = selected_keypoints_coordinates[3]
            x4 = selected_keypoints_coordinates[4]
            x5 = selected_keypoints_coordinates[5]

            x6 = selected_keypoints_coordinates[6]
            x7 = selected_keypoints_coordinates[7]
            x8 = selected_keypoints_coordinates[8]

            x9 = selected_keypoints_coordinates[9]
            x10 = selected_keypoints_coordinates[10]
            x11 = selected_keypoints_coordinates[11]

            x12 = selected_keypoints_coordinates[12]
            x13 = selected_keypoints_coordinates[13]
            x14 = selected_keypoints_coordinates[14]

            x15 = selected_keypoints_coordinates[15]
            x16 = selected_keypoints_coordinates[16]
            x17 = selected_keypoints_coordinates[17]

            righthip_angle = cal_ang(x6,x7,x8)
            cv2.putText(img, str(f'Right Hip:{round(righthip_angle)}'), org=(int(video_width*0.8),int(video_height*0.05)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,0,255), thickness=2, lineType=cv2.LINE_AA)

            rightknee_angle = cal_ang(x0,x1,x2)
            cv2.putText(img, str(f'Right Knee:{round(rightknee_angle)}'), org=(int(video_width*0.8),int(video_height*0.1)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
            
            rightankle_angle = cal_ang(x12,x13,x14)
            cv2.putText(img, str(f'Right Ankle:{round(rightankle_angle)}'), org=(int(video_width*0.8),int(video_height*0.15)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)

            lefthip_angle = cal_ang(x9,x10,x11)
            cv2.putText(img, str(f'Left Hip:{round(lefthip_angle)}'), org=(int(video_width*0.8),int(video_height*0.2)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
            
            leftknee_angle = cal_ang(x3,x4,x5)
            cv2.putText(img, str(f'Left Knee:{round(leftknee_angle)}'), org=(int(video_width*0.8),int(video_height*0.25)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)

            leftankle_angle = cal_ang(x15,x16,x17)
            cv2.putText(img, str(f'Left Ankle:{round(leftankle_angle)}'), org=(int(video_width*0.8),int(video_height*0.3)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)

            # print(selected_keypoints_coordinates)

        out.write(img)
        count += 1
        print(count)
        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
