# Judge Port — AI-Powered Sentiment Analysis Platform

A Flask-based web application that analyzes public sentiment around the Russia-Ukraine conflict using an LSTM deep learning model and NLP techniques.

## 🔗 Links
- **GitHub:** https://github.com/Gagana-r/judge-port

## 📌 About
Judge Port classifies user-submitted comments as **Positive**, **Neutral**, or **Negative** using a trained LSTM model. It helps researchers, journalists, and policymakers understand public perception in real time during major geopolitical events.

## 🛠️ Tech Stack
| Layer | Tool |
|---|---|
| Backend | Python, Flask |
| Deep Learning | TensorFlow, Keras (LSTM) |
| NLP | NLTK, scikit-learn |
| Database | MySQL |
| Frontend | HTML, CSS |

## ✨ Features
- User authentication (Signup, Login, Logout)
- Real-time sentiment prediction using LSTM model
- Text preprocessing with NLTK stopword removal
- Stores user queries and predictions in MySQL database
- Clean, responsive UI with red-themed design

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Gagana-r/judge-port.git
cd judge-port
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure MySQL
Update `config.py` with your MySQL credentials:
```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'your_database'
```

### 4. Set up the database
```bash
mysql -u root -p < database/schema.sql
```

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

## 📁 Project Structure
```
judge-port/
├── app.py               # Main Flask application
├── lstm_predict.py      # LSTM model prediction logic
├── preprocess.py        # Text preprocessing
├── config.py            # Database configuration
├── tokenizer.pkl        # Trained tokenizer
├── lstm_model.h5        # Trained LSTM model
├── requirements.txt     # Python dependencies
├── database/
│   └── schema.sql       # MySQL schema
├── templates/           # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── input.html
│   ├── result.html
│   ├── about.html
│   └── forget.html
└── static/
    └── styles.css
```

## 🧠 Model Details
- **Architecture:** LSTM (Long Short-Term Memory)
- **Task:** Multi-class sentiment classification (Positive / Neutral / Negative)
- **Preprocessing:** Tokenization, stopword removal, padding

## 👩‍💻 Author
**Gagana R** — [GitHub](https://github.com/Gagana-r)
