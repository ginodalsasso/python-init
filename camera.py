import cv2 # OpenCV pip install opencv-contrib-python

cap = cv2.VideoCapture(0)
address = ""
cap.open(address)

while(True):
    ret, frame = cap.read() # Capture frame-by-frame
    cv2.imshow('frame', frame) # Afficher le frame
    if cv2.waitKey(20) & 0xFF == ord('q'): # Si on appuie sur 'q' on quitte
        break
    if cv2.waitKey(33) & 0xFF == ord('a'): # Si on appuie sur 'a' on prend une capture
        cv2.imwrite('image.jpg', frame)

cap.release() # Quand tout est fini, on relâche la capture vidéo
cv2.destroyAllWindows() # On ferme toutes les fenêtres