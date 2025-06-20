# 🧠 Semantic Similarity CLI Tool

A production-ready command-line tool for detecting semantic similarity between two sentences using sentence-transformers and XGBoost.

---

## 📆 Repository Link

👉 [GitHub: SIMANTIC\_SIMILARITY\_CLI](https://github.com/SasidharaSrivatchasa/SIMANTIC_SIMILARITY_CLI)

---

## 🛠️ Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SasidharaSrivatchasa/SIMANTIC_SIMILARITY_CLI.git
   cd SIMANTIC_SIMILARITY_CLI
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install CLI tool**:

   ```bash
   pip install -e .
   ```

📅 Now you can run `semantic-sim` from anywhere in your terminal.

---

## 🧠 Model and Vectorizer Used

| Component          | Method                                          |
| ------------------ | ----------------------------------------------- |
| Preprocessing      | Stopword removal, punctuation cleaning          |
| Embedding model    | `all-MiniLM-L6-v2` from `sentence-transformers` |
| Feature extraction | Cosine similarity → probability conversion      |
| Classifier model   | XGBoost Classifier (`.pkl` file)                |

All models are stored in an external Google Drive folder due to file size.

---

## 📦 Model Setup Instructions

Since model files are too large for GitHub, download them from Google Drive:

🔗 **[Download models folder](https://drive.google.com/drive/folders/11-gmsGnl9DYjJv97wCH20dFkBoxOeMf7?usp=drive_link)**

1. Download the folder from the link above
2. Place the entire folder into your project root and rename it `models/` if needed
3. Ensure the structure looks like this:

```
project-root/
├── semantic_sim_cli.py
├── setup.py
├── requirements.txt
├── models/
│   ├── semantic_similarity_model.pkl
│   └── semantic_encoder/
```

> ✅ This will make your CLI tool work correctly with local models.

---

## 🧪 Sample Inputs & Outputs

### 🔹 Command:

```bash
semantic-sim -s1 "How do I learn Python?" -s2 "What's the best way to master Python?"
```

### 🔹 Output:

```
🤝 Similar: Yes
📊 Confidence: 76.85%
```

### 🔹 Batch Mode:

```bash
semantic-sim -f data/input.csv -o data/output.csv
```

---

## 🌐 Deployment Instructions

Since this is a CLI tool, no web hosting is needed. You can:

1. Clone and run locally
2. Use it in Python pipelines
3. Extend it to a Flask/FastAPI web app (not included in this version)

---

## 📂 Project Structure

```
📚 semantic_similarity_cli/
├── semantic_sim_cli.py        # CLI logic
├── setup.py                   # CLI installation config
├── requirements.txt           # Dependencies
├── models/                    # Model and encoder
│   ├── semantic_similarity_model.pkl
│   └── semantic_encoder/
```

---

## 🤛 Author

**Sasidhara Srivatchasa**

AI Engineer | NLP Developer

[GitHub](https://github.com/SasidharaSrivatchasa)

---
