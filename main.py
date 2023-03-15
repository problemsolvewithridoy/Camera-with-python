# Please Subscribe our YouTube channel @problemsolvewithridoy
import cv2
import winsound

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

counter = 0

while True:
  _, img  = cap.read()
  cv2.imshow("My own Camera",img)
  if cv2.waitKey(1) == ord("c"):
    counter += 1
    cv2.imwrite(f"myimage{counter}.jpg",img)
    winsound.Beep(500, 100)
  if cv2.waitKey(1) == ord("q"):
    break



