import numpy as np # pip install numpy
from PIL import Image # pip install pillow
import cv2 # pip install opencv-python

# TensorFlow and tf.keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2

# pip install tensorflow

# Modèle ImageNet
model = MobileNetV2(weights='imagenet')
img = Image.open("image.jpg")

# Fonction de prédiction
def model_predict(img, model):
   img = img.resize((224, 224))
   x = image.img_to_array(img)
   x = np.expand_dims(x, axis=0)
   x = preprocess_input(x, mode='tf')
   preds = model.predict(x)
   return preds


# prediction
preds = model_predict(img, model)
pred_proba = "{:.3f}".format(np.amax(preds))
pred_class = decode_predictions(preds, top=1)

result = str(pred_class[0][0][1])
result = result.replace('_', ' ').capitalize()
print({"result":result, "probability":pred_proba})