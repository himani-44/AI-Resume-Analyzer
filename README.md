# AI Resume Analyzer

An AI-powered Resume Analyzer that compares resumes against job descriptions using NLP, embeddings, semantic similarity, and ATS scoring.

## Live Demo

Deployed Application:

https://ai-resume-analyzer-kmqqsvs26m3cyqlnd53wxx.streamlit.app/

## Features

* Resume PDF Parsing
* Skill Extraction
* Alias Mapping
* Skill Matching
* Missing Skill Detection
* Semantic Similarity using Sentence Transformers
* ATS Score Calculation
* Multi Resume Comparison
* Resume Ranking
* Resume Recommendation
* ATS Feedback Generation
* Interactive Streamlit Interface

## Tech Stack

* Python
* Streamlit
* Sentence Transformers
* Scikit-Learn
* spaCy
* PyMuPDF
* NLP
* Embeddings
* Cosine Similarity

## How It Works

1. Upload one or more resumes.
2. Enter a job description.
3. Extract skills from resumes and job description.
4. Calculate skill match percentage.
5. Calculate semantic similarity using embeddings.
6. Compute ATS Score.
7. Rank resumes and recommend the best resume.

## ATS Score Formula

ATS Score = (Skill Match Percentage × 0.6) + (Semantic Similarity × 0.4)

## Project Architecture

* parser.py → Extracts text from PDF resumes
* skills.py → Skill extraction and alias mapping
* similarity.py → Skill matching logic
* semantic_similarity.py → Embeddings and cosine similarity
* feedback.py → ATS feedback generation
* app.py → Streamlit user interface

## Future Improvements

* LLM-based feedback generation
* Resume improvement suggestions
* Vector database integration
* Advanced NLP skill extraction
* Cloud-scale deployment

## Author

Himani Agrawal
