# 🤝 Personalized Networking Assistant

An AI-powered web application that helps users generate personalized conversation starters for professional events, conferences, seminars, and networking sessions. The application uses Natural Language Processing (NLP) to analyze event descriptions, generate context-aware conversation starters, verify information using Wikipedia, and maintain conversation history for continuous improvement.

Built using **FastAPI**, **Streamlit**, **Transformers (DistilBERT & GPT-2)**, **Wikipedia API**, and **Python**.

---

# 📌 Features

- 🤖 AI-powered personalized conversation starter generation
- 🧠 Event theme extraction using DistilBERT
- 💬 Context-aware networking conversation suggestions using GPT-2
- 🔍 Fact verification using Wikipedia API
- 📝 Conversation history management
- 👍 User feedback collection for generated suggestions
- 📄 Export conversation history as PDF
- ⚡ REST API developed using FastAPI
- 🌐 Interactive web interface using Streamlit
- 🧪 Unit testing using PyTest
- 📖 Interactive API documentation using Swagger UI

---

# 🏗️ Technical Architecture

```text
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
               FastAPI Backend
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 Event Theme Analysis        Fact Verification
 (DistilBERT)                (Wikipedia API)
        │
        ▼
 GPT-2 Conversation Generator
        │
        ▼
 Conversation History & Feedback
        │
        ▼
      JSON / Database
```

---

# 📂 Project Structure

```text
Personalized-Networking-Assistant/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── routers/
│   ├── services/
│   └── utils/
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│
├── images/
│
├── history.json
├── feedback.json
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| Streamlit | Frontend Framework |
| Hugging Face Transformers | NLP Models |
| DistilBERT | Theme Classification |
| GPT-2 | Conversation Generation |
| Wikipedia API | Fact Verification |
| ReportLab | PDF Report Generation |
| PyTest | Unit Testing |
| Git & GitHub | Version Control |

---

# 💻 System Requirements

## Hardware

- Intel Core i3 / i5 / i7 Processor
- Minimum 4 GB RAM (8 GB Recommended)
- 10 GB Free Storage
- Stable Internet Connection

## Software

- Windows / Linux / macOS
- Python 3.10+
- FastAPI
- Streamlit
- Git
- Visual Studio Code / PyCharm

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Sravanthi1757/Personalized-Networking-Assistant.git
```

Move into the project directory

```bash
cd Personalized-Networking-Assistant
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Running the Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 🧪 Running Unit Tests

```bash
pytest -v
```

---

# 📸 Application Screenshots

### Home Page

_Add screenshot here_

### Conversation Generator

_Add screenshot here_

### Fact Verification

_Add screenshot here_

### Swagger API Documentation

_Add screenshot here_

---

# 🎯 Project Scenarios

### Scenario 1 – Smart Conversation Starter Generation

A user enters an event description such as **"AI for Sustainable Cities"** along with interests like **Artificial Intelligence**, **Climate Change**, and **Urban Planning**. The application analyzes the event theme and generates personalized conversation starters relevant to the event.

---

### Scenario 2 – Fact Verification

A user searches for a topic such as **"Blockchain in Healthcare"**. The application retrieves reliable information from the Wikipedia API and displays a concise summary for quick verification.

---

### Scenario 3 – Conversation History

Users can access previous networking conversations, review generated suggestions, and revisit responses they marked as useful to continuously improve their networking skills.

---

# 🚀 Future Enhancements

- Google Gemini API Integration
- LinkedIn Profile Integration
- Voice Assistant Support
- User Authentication
- PostgreSQL Database Integration
- Cloud Deployment
- Multi-language Support
- AI-based Networking Recommendation System

---

# 👥 Team Members

**Project:** Personalized Networking Assistant

**Course:** Google Cloud Generative AI Internship

**College:** Swarnandhra College of Engineering and Technology

**Department:** B.Tech – Artificial Intelligence & Data Science (AI & DS)

| Name | Role |
|------|------|
| Ashajyothi Kusume | Team Lead |
| Polisetty Baby Nagalakshmi | Team Member |
| SatyaKalyani Donga | Team Member |
| Sravanthi Nalli | Team Member |
| Maddula Venkata Kowshik | Team Member |


---

# 📜 License

This project was developed as part of the **Google Cloud Generative AI Internship** for educational and learning purposes only.
