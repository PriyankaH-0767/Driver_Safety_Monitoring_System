import cv2
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps

# Load model
model = load_model("keras_model.h5", compile=False)

# Load labels
class_names = open("labels.txt", "r").readlines()

# Open webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Resize and prepare image
    image = cv2.resize(frame, (224, 224))
    image = Image.fromarray(image)
    image = ImageOps.fit(image, (224, 224))
    image_array = np.asarray(image)

    normalized_image = (image_array.astype(np.float32) / 127.5) - 1

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image

    # Predict
    prediction = model.predict(data, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence = prediction[0][index]

    # Display result
    text = f"{class_name} ({confidence*100:.2f}%)"
    cv2.putText(frame, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Driver Safety Monitoring", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()