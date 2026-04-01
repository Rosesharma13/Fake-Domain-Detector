# 🔐 Fake Domain Detector — NLP Classifier

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-008080?style=flat)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)

## 📌 Overview

Fake Domain Detector is a Machine Learning-based cybersecurity project that detects fake and malicious domain names using NLP techniques and feature engineering. The system analyzes domain patterns to identify phishing and suspicious URLs effectively.

---

## ✨ Features

- 🔍 **Malicious Domain Detection** — Classifies domains as FAKE 🚨 or LEGIT ✅  
- 🧠 **NLP-based Analysis** — Uses character n-grams for pattern detection  
- 📊 **Feature Engineering** — Entropy, domain length, and digit patterns  
- ⚡ **Fast Predictions** — Real-time domain classification  
- 🛡️ **Cybersecurity Focus** — Helps detect phishing and fraudulent domains  
- 📈 **Scalable Model** — Can be trained on large datasets (1000+ samples)
- 🌐 **Interactive Web UI** — Built using Streamlit for real-time domain detection 

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Scikit-learn** | Machine Learning model |
| **NLP (Character N-grams)** | Feature extraction |
| **Pandas** | Data processing |
| **NumPy** | Numerical computations |
| **Streamlit** | Web interface for user interaction |

---

## 📁 Project Structure
```
fake-domain-detector/
├── data/
├── src/
├── app.py              # Streamlit UI
├── detector.py         # CLI version
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How to Run

### Step 1 — Clone the repository
```bash
git clone https://github.com/Rosesharma13/Fake-Domain-Detector
cd Fake-Domain-Detector 
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt 
```

### Step 3 — Run the detector
```bash
python detector.py
```

### Step 4 — Run Streamlit UI
```bash
streamlit run app.py
```

---

## 💬 Example Usage
| Input                          | Output  |
| ------------------------------ | ------- |
| secure-amazon-login.com        | FAKE 🚨 |
| google.com                     | LEGIT ✅|
| paytm-verification-alert.xyz   | FAKE 🚨 |

---

## 📊 Model Details
- **Algorithm**: Random Forest Classifier
- **Features Used**:
   - Character n-grams (NLP)
   - Domain length
   - Digit count
   - Lexical entropy
- **Accuracy**: ~90% (with extended dataset)

---

## 📸 Screenshots
















---

## 🔑 Key Learning Outcomes
- **NLP Feature Engineering** — Using character-level patterns for classification
- **Machine Learning Pipeline** — Data preprocessing → training → prediction
- **Cybersecurity Application** — Detecting phishing domains
- **Model Optimization** — Improving performance using engineered features

---

## 👩‍💻 Author

**Rose Sharma**

- LinkedIn: linkedin.com/in/rose-sharma13(https://www.linkedin.com/in/rose-sharma13)
- Email: rosesharmaa132003@gmail.com

---

## 📄 License

This project is licensed under the MIT License.
