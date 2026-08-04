# DecodeLabs Internship — Machine Learning Projects

**Author:** Rayyan Aamir\
**Program:** DecodeLabs Machine Learning Internship

This repository contains the hands-on projects completed during the DecodeLabs Machine Learning Internship. Each project lives in its own folder with a dedicated `README.md`, source code, and (where applicable) a Jupyter notebook version.

## Projects

| # | Project | Description | Key Tech | Type |
|---|---|---|---|---|
| 01 | [Rule-Based Chatbot](./Project-01) | A command-line chatbot (**RayBot**) that matches keywords in user input against a predefined knowledge base and responds accordingly, with graceful fallback handling and multiple exit commands. | Python (standard library only) | Rule-based system |
| 02 | [Wine Quality Prediction](./Project-02) | A classification pipeline that predicts red wine quality (Good/Bad) from physicochemical properties, training and comparing Logistic Regression, KNN, and Decision Tree models. | pandas, scikit-learn, matplotlib, seaborn | Supervised classification |
| 03 | [Tech-Stack Recommender](./Project-03) | A content-based recommendation system that maps a user's skills to the closest-matching tech career paths using TF-IDF vectorization and cosine similarity. | pandas, scikit-learn (TF-IDF, cosine similarity) | Recommendation system |
| 04 | [OCR Text Recognition](./Project-04) | An end-to-end OCR pipeline that preprocesses images, extracts text with Tesseract, benchmarks detections against an 80% confidence threshold, and visualizes labeled bounding boxes. | OpenCV, pytesseract, NumPy, Pillow | Computer vision / OCR |

## Repository Structure

```
DecodeLabs-Internship/
├── Project-01/          # Rule-Based Chatbot
│   ├── ray-chatbot.py
│   └── README.md
├── Project-02/          # Wine Quality Prediction
│   ├── Wine-Quality-Prediction.ipynb
│   ├── wine-quality-prediction.py
│   ├── requirements.txt
│   └── README.md
├── Project-03/          # Tech-Stack Recommender
│   ├── Tech-Stack-Recommender.ipynb
│   ├── tech-stack-recommender.py
│   ├── raw_skills.csv
│   ├── requirements.txt
│   └── README.md
├── Project-04/          # OCR Text Recognition
│   ├── OCR-Text-Recognition.ipynb
│   ├── OCR-text-recognition.py
│   ├── sample.jpg
│   ├── requirements.txt
│   └── README.md
└── .gitignore
```

## Getting Started

Each project is self-contained. To run one:

```bash
cd Project-0X
pip install -r requirements.txt   # if the project has one
python <script-name>.py
```

Project-01 has no external dependencies (pure Python standard library). Projects 02–04 include a `requirements.txt` for their Python package dependencies; Project-04 additionally requires the [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract#installing-tesseract) installed as a system binary.

See each project's own `README.md` for full details — dataset info, usage examples, sample output, and possible improvements.

## Note

This repository documents projects completed as part of the **DecodeLabs Machine Learning Internship**, covering rule-based systems, supervised machine learning, recommendation systems, and computer vision/OCR.