# ---------------------------------------------------------------------------------
import cv2
import mediapipe as mp
import time

# ---------------------------------------------------------------------------------

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
pTime = 0
# ---------------------------------------------------------------------------------
# cap = cv2.VideoCapture('walking.mp4')  # Processing on walking.mp4
cap = cv2.VideoCapture(0)  # Reading from Camera
# ---------------------------------------------------------------------------------
if cap is None or not cap.isOpened():
    print("No Camera found")
    exit()
while True:  # Infinite loop, read image every second to make it show like a video
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # img = cv2.resize(img, (960, 540))
    img = cv2.resize(img, (600, 600))
    cv2.imshow("Coordinates", img)
    cv2.waitKey(1)

    # Close window if user press on close button
    if cv2.getWindowProperty("Coordinates", cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()
cap.release()
# ---------------------------------------------------------------------------------
