from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_skill_match(resume_skills, job_skills, threshold=0.6):
    matched = []
    missing = []

    # Convert to embeddings
    job_embeddings = model.encode(job_skills, convert_to_tensor=True)
    resume_embeddings = model.encode(resume_skills, convert_to_tensor=True)

    for i, job_skill in enumerate(job_skills):
        similarities = util.cos_sim(job_embeddings[i], resume_embeddings)

        max_score = similarities.max().item()

        if max_score >= threshold:
            matched.append(job_skill)
        else:
            missing.append(job_skill)

    return matched, missing