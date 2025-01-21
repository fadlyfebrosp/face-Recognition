<p align="center">
  <img src="https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_black-2.png" alt="OpenCV Logo" width="150" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Logo" width="150" />
</p>


# Face Detection with OpenCV

This project demonstrates real-time face detection using OpenCV. The application uses a webcam to detect faces and highlights them with a blue rectangular frame. Additionally, the video feed is mirrored for a more natural interaction.

---

## Features
- **Real-time Face Detection**: Detects faces in a live webcam feed.
- **Mirrored Display**: The video feed is flipped horizontally for a mirror effect.
- **Dynamic Framing**: Adds padding to the detected face for better visibility.
- **Blue Frame Highlight**: Highlights detected faces with a blue rectangle.

---

## Prerequisites

1. Python 3.x
2. OpenCV library

To install OpenCV, run:
```bash
pip install opencv-python
```

---

## How to Run the Project

1. Clone this repository or copy the code into a Python file (e.g., `face_detection.py`).
2. Ensure your webcam is functional and accessible.
3. Run the script:
   ```bash
   python facereccognition.py
   ```

4. Press the `q` key to exit the application.

---

## Code Explanation

### Step 1: Import OpenCV
```python
import cv2
```
Import the OpenCV library for image and video processing.

### Step 2: Load the Face Detection Model
```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
```
This loads a pre-trained Haar Cascade classifier for frontal face detection.

### Step 3: Access the Webcam
```python
cap = cv2.VideoCapture(0)
```
Opens the default webcam (ID `0`). Ensure your webcam is not in use by other applications.

### Step 4: Process the Video Feed
- **Read Frames**:
  ```python
  ret, frame = cap.read()
  ```
  Captures frames from the webcam.

- **Mirror Effect**:
  ```python
  frame = cv2.flip(frame, 1)
  ```
  Flips the frame horizontally.

- **Convert to Grayscale**:
  ```python
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ```
  Prepares the frame for face detection by converting it to grayscale.

- **Detect Faces**:
  ```python
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 70))
  ```
  Detects faces with adjustable parameters for scaling and neighbor validation.

- **Draw Blue Rectangles**:
  ```python
  cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
  ```
  Highlights faces with a blue rectangle.

### Step 5: Display the Output
```python
cv2.imshow('Deteksi Wajah dengan Kotak Biru', frame)
```
Displays the processed video feed with the highlighted faces.

### Step 6: Exit on `q`
```python
if cv2.waitKey(1) == ord('q'):
    break
```
Closes the application when the `q` key is pressed.

---

## Troubleshooting
- **Webcam Not Accessible**:
  Ensure no other applications are using the webcam.
- **Face Detection Fails**:
  Check lighting conditions and ensure faces are within the camera frame.

---

## License
This project is open-source and available under the [MIT License](LICENSE).
