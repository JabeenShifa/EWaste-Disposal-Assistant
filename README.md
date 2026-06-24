# ♻️ E-Waste Disposal Assistant

## 🌍 AI-Powered Sustainable E-Waste Management

The **E-Waste Disposal Assistant** is an AI-powered web application that helps users identify electronic waste items from images and provides responsible disposal recommendations. The system uses **MobileNetV2 Deep Learning** for image recognition and promotes sustainable waste management practices aligned with the **United Nations Sustainable Development Goals (SDGs)**.

---

## 🚨 Problem Statement

Electronic waste (E-Waste) is one of the fastest-growing waste streams worldwide. Many people are unaware of proper disposal methods for electronic devices such as smartphones, laptops, batteries, and monitors. Improper disposal leads to environmental pollution, toxic chemical leakage, and loss of valuable recyclable materials.

This project aims to educate users and assist them in making environmentally responsible decisions regarding electronic waste disposal.

---

## 💡 Solution

Users upload an image of an electronic item, and the AI system:

* Identifies the electronic device
* Predicts confidence score
* Determines recyclability
* Classifies waste category
* Suggests disposal methods
* Provides sustainability tips
* Explains environmental impact
* Promotes SDG 12 awareness

---

## 🧠 AI Technology Used

### Deep Learning Model

* MobileNetV2 (Pretrained on ImageNet)

### Libraries

* TensorFlow
* NumPy
* Pillow
* Streamlit

### AI Features

* Image Classification
* Confidence Score Prediction
* Rule-Based Recommendation System
* Sustainability Awareness Guidance

---

## 🛠️ Technology Stack

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python      | Backend Development       |
| Streamlit   | Web Application Interface |
| TensorFlow  | Deep Learning Framework   |
| MobileNetV2 | Image Recognition Model   |
| NumPy       | Data Processing           |
| Pillow      | Image Handling            |

---

## 📂 Project Structure

```text
EWaste_Disposal_Assistant/
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── classifier.py
│   ├── recommendation.py
│   ├── utils.py
│   └── __init__.py
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/EWaste-Disposal-Assistant.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run dashboard/app.py
```

---

## 📸 Sample Output

### Input

User uploads an image of an electronic device.

### AI Prediction Example

**Detected Item:** Smartphone

**Confidence Score:** 45.98%

**Recyclable:** Yes, Highly Recyclable

**Waste Category:** Mobile Phone E-Waste

**Disposal Method:** Submit to an authorized e-waste collection center after removing personal data.

**Sustainability Tips:**

* Donate working devices
* Repair before replacing
* Recycle batteries separately

**Environmental Impact:**
Smartphones contain valuable metals such as gold, silver, and copper that can be recovered through recycling.

---

## 🌱 Sustainability Impact

The project helps:

* Promote responsible electronic waste disposal
* Increase recycling awareness
* Reduce environmental pollution
* Encourage reuse and repair of electronic devices
* Support sustainable consumption practices

---

## 🎯 Sustainable Development Goals Supported

### SDG 12 – Responsible Consumption and Production

Encourages proper recycling, reuse, and disposal of electronic products.

### SDG 13 – Climate Action

Reduces environmental damage caused by improper e-waste disposal.

### SDG 11 – Sustainable Cities and Communities

Supports cleaner and more sustainable urban environments.

---

## 📈 Future Enhancements

* Custom-trained E-Waste Dataset
* Real-time Camera Detection
* Recycling Center Locator
* QR-Based Disposal Tracking
* Multi-language Support
* Cloud Deployment

---

## 👩‍💻 Author

**Jabeen Shifa A**

1M1B AI for Sustainability Virtual Internship Project

2026

---

## 📜 License

This project is developed for educational, research, and sustainability awareness purposes.
