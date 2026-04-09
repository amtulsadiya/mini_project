from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_words, job_words):
    resume_text = " ".join(resume_words)
    job_text = " ".join(job_words)

    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity = cosine_similarity(vectors[0], vectors[1])

    return similarity[0][0]