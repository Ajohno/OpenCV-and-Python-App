import cv2

# Opens the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Keeps the loop running
while True:
    # Reads the frame
    ret, frame = cap.read()

    # Flip the camera (mirror effect)
    frame = cv2.flip(frame, 1)

    if not ret:
        print("Failed to grab frame")
        break

    # Add a text overlay to show the camera is running
    cv2.putText(frame, "Camera Running",
                (20, 40),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (0, 255, 0),
                1)

    # Show the frame
    cv2.imshow("Camera Feed", frame)

    # Convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Scale", gray)

    # Quit by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup when done
cap.release()
cv2.destroyAllWindows()