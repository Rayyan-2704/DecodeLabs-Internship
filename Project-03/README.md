# Project 03: Tech-Stack Recommender

**DecodeLabs Internship — Project 03**
**Author:** Rayyan Aamir

## Description

A content-based recommendation system that maps a user's skill-set to their ideal tech career path. The engine uses **TF-IDF (Term Frequency–Inverse Document Frequency)** weighting to vectorize job-role skill profiles, then applies **Cosine Similarity** to mathematically score how closely a user's inputted skills align with each role, returning the top matching career paths.

## Dataset

- **Source:** `raw_skills.csv` (included in this project)
- **Structure:** Two columns — `job_role` and `skills` (a space-separated list of skills/technologies associated with that role)
- **Roles covered:** Cloud Architect, Data Scientist, DevOps Engineer, Frontend Developer, Backend Engineer, QA Automation Engineer, Data Engineer, Cybersecurity Analyst

## How It Works

1. **Data Loading** — Reads job roles and their associated skills from `raw_skills.csv`.
2. **User Input** — Prompts the user to enter 3 skills via the command line.
3. **Vectorization** — Combines the job-role skill corpus with the user's input and fits a `TfidfVectorizer` across all of them.
4. **Similarity Scoring** — Computes cosine similarity between the user's TF-IDF vector and each job role's TF-IDF vector.
5. **Ranking** — Sorts roles by similarity score and returns the top 3 matches, displayed as an alignment percentage.

## Requirements

```
pandas>=2.0.0
scikit-learn>=1.3.0
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the terminal:

```bash
python tech-stack-recommender.py
```

Or open and run the notebook version:

```
Tech-Stack-Recommender.ipynb
```

Example session:

```
==================================================
		Tech-Stack Recommender
==================================================
Enter skill 1: Python
Enter skill 2: Machine Learning
Enter skill 3: SQL


--------------- Top 3 Career Path Recommendations ---------------
Role: Data Scientist		 | Alignment Score: 61.42%
Role: Data Engineer		 | Alignment Score: 24.15%
Role: Cybersecurity Analyst	 | Alignment Score: 9.87%
```

## Project Structure

```
Project-03/
├── Tech-Stack-Recommender.ipynb
├── tech-stack-recommender.py
├── raw_skills.csv
└── requirements.txt
```

## Possible Improvements

- Expand `raw_skills.csv` with more job roles and richer skill descriptions
- Allow a variable number of user-entered skills instead of a fixed 3
- Weight skills by relevance/seniority rather than treating them uniformly
- Add fuzzy matching to handle typos or skill synonyms (e.g. "JS" vs "JavaScript")