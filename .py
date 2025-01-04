import cv2
import numpy as np
import os
import tempfile
from inference_sdk import InferenceHTTPClient

# Initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="XCjCnsDvWNwavem9Gk50"
)

# Start video capture (0 for the default webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Create a temporary file to save the image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file_path = temp_file.name

    # Save the current frame to the temporary file
    cv2.imwrite(temp_file_path, frame)

    # Perform inference on the captured frame using the file path
    result = CLIENT.infer(temp_file_path, model_id="grains-detection-ykdtf/2")

    # Print the result
    print(result)

    # Show the frame in a window
    cv2.imshow("Webcam Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Optionally, remove the temporary file after inference
    os.remove(temp_file_path)

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
