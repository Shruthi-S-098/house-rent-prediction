

# **🏙️ Metro House Rent Predictor**

A simple and interactive web application that helps users estimate house rent across major metro cities in India.
The app provides real-time rent predictions based on selected city, area, and home features, along with a clean and intuitive interface.

🔗 **Live App:** [https://huggingface.co/spaces/Shruthi-S-098/metro-rent-predictor](https://huggingface.co/spaces/Shruthi-S-098/metro-rent-predictor)

🔗 **GitHub Repository:** [[https://github.com/Shruthi-S-098](https://github.com/Shruthi-S-098/house-rent-prediction)](https://github.com/Shruthi-S-098)

---

## **✨ Overview**

Metro House Rent Predictor allows users to:

* Select a **city**, and automatically view all **areas** under that city.
* Enter home details such as rooms, bathrooms, parking, floor type, etc.
* Instantly get an estimated rent based on the selected features.
* Experience a friendly, interactive UI built for smooth usage.

The goal is to make rent estimation simple, accessible, and user-friendly.

---

## **🌟 Features**

### ✔️ Dynamic City–Area Linking

Once a city is selected, the area dropdown updates automatically to show only the available areas under that city.
No need for typing or guessing.

### ✔️ Clean & Modern Interface

Designed with a soft theme and intuitive layout for a seamless user experience.

### ✔️ Quick Rent Estimation

The app uses a simple calculation method based on the user’s selected house features.

### ✔️ Lightweight & Fast

Runs instantly without heavy processing or long loading times.

### ✔️ Works Anywhere

Easily accessible online through HuggingFace Spaces.

---

## **🧩 How Rent Is Estimated**

A clean, easy-to-understand formula is used:

```
Total Rent = Base Rent + (Rooms × 1200) + (Bathrooms × 800) + (Parking × 500)
```

This keeps predictions straightforward and consistent.

---

## **📁 Project Files**

```
📦 metro-rent-predictor
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 Metro_House_Rent.csv
 ┗ 📜 README.md
```

---

## **▶️ Running the Project Locally**

### **1. Clone the Repository**

```bash
git clone https://github.com/Shruthi-S-098/metro-rent-predictor.git
cd metro-rent-predictor
```

### **2. Install Required Packages**

```bash
pip install -r requirements.txt
```

### **3. Start the App**

```bash
python app.py
```

The application will open in your browser.

---

## **🌐 Deploying on HuggingFace**

1. Create a new Space.
2. Select the **Gradio** template.
3. Upload these files:

   * `app.py`
   * `requirements.txt`
   * `Metro_House_Rent.csv`
4. HuggingFace will automatically build and host the app.

---

## **👤 Developer**

**Name:** Shruthi S
🔗 GitHub: [https://github.com/Shruthi-S-098](https://github.com/Shruthi-S-098)

🔗 Live App: [https://huggingface.co/spaces/Shruthi-S-098/metro-rent-predictor](https://huggingface.co/spaces/Shruthi-S-098/metro-rent-predictor)

---


