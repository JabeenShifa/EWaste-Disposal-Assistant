import numpy as np

try:
    from tensorflow.keras.applications.mobilenet_v2 import (
        MobileNetV2,
        preprocess_input,
        decode_predictions
    )

    from tensorflow.keras.preprocessing import image

    TF_AVAILABLE = True

except Exception:
    TF_AVAILABLE = False


# ==========================================
# Load Model
# ==========================================

if TF_AVAILABLE:
    model = MobileNetV2(weights="imagenet")


# ==========================================
# Label Mapping
# ==========================================

LABEL_MAPPING = {

    "cellular_telephone": "smartphone",
    "hand-held_computer": "smartphone",

    "notebook": "laptop",

    "desktop_computer": "computer",

    "computer_keyboard": "keyboard",
    "keyboard": "keyboard",

    "monitor": "monitor",
    "television": "monitor",

    "battery": "battery",

    "mouse": "mouse"
}


# ==========================================
# Prediction Function
# ==========================================

def predict_image(img_path):

    if not TF_AVAILABLE:
        raise Exception(
            "TensorFlow is not installed.\n\nRun:\npip install tensorflow"
        )

    img = image.load_img(
        img_path,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    img_array = preprocess_input(
        img_array
    )

    predictions = model.predict(
        img_array,
        verbose=0
    )

    decoded = decode_predictions(
        predictions,
        top=1
    )[0]

    raw_label = decoded[0][1]

    confidence = float(
        decoded[0][2]
    )

    final_label = LABEL_MAPPING.get(
        raw_label,
        raw_label
    )

    return final_label, confidence