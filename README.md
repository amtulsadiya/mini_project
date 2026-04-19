
# Skill Gap Analyzer
A web-based application that analyzes the gap between a candidate’s resume and a job description using NLP techniques. It provides a similarity score and highlights how well a candidate matches a given role.

## Overview
The **Skill Gap Analyzer** helps job seekers understand how closely their resume aligns with a job description. By computing similarity scores and categorizing match levels, users can identify missing skills and improve their chances of selection.

## Features
*  Upload or input resume text
*  Input job description
*  Text preprocessing (cleaning, stopword removal)
*  TF-IDF vectorization
*  Cosine similarity calculation
*  Match classification:
  * High Match
  * Medium Match
  * Low Match
* Easy-to-use UI built with Streamlit

##  Tech Stack
* Python
* Scikit-learn
* NLTK 
* Streamlit

## AI / Logic Layer
->Skill Extraction (custom keyword + static skill matching)<br>
->Semantic Skill Matching ( semantic_skill_match)<br>
->Keyword Extraction (dynamic skill detection)<br>
->Text Preprocessing Pipeline<br>

## How It Works

1. The resume and job description are converted into text
2. Text is preprocessed (lowercasing, removing stopwords, etc.)
3. TF-IDF converts text into numerical vectors
4. Cosine similarity is calculated between the vectors
5. A match score is generated and categorized

##  Demo
<img width="598" height="772" alt="image" src="https://github.com/user-attachments/assets/d147bff6-b624-46fb-be29-7e5ef8577377" />

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/amtulsadiya/mini_project.git

# Navigate to the project folder
cd mini_project

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
```
## Example Output
Matched Skills:
["python","nlp"]

Missing Skills:
["tensorflow","generative ai","pytorch"]<br>
Skill Match Score: 40.0 %<br>
Overall Match Level: Low Match<br>

## Future Improvements
* Skill extraction and highlighting missing skills
* Resume improvement suggestions
* Use of advanced embeddings (BERT, Sentence Transformers)
* Support for PDF/DOCX parsing

Author
GitHub: [https://github.com/amtulsadiya](https://github.com/amtulsadiya)

