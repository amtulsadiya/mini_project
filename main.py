from preprocess import preprocess
from matcher import skill_gap, match_score
from similarity import compute_similarity
from skill_extractor import load_skills, extract_skills, extract_keywords

# Sample Inputs
resume_text = """
I am skilled in Python, Machine Learning, and Data Analysis.
I have worked with Pandas and NumPy.
"""

job_text = """
We are looking for a candidate with Python, SQL, AWS, and Machine Learning experience.
"""

# Load skills (STATIC)
skills_list = load_skills("data/skills.txt")

# Preprocess
resume_words = preprocess(resume_text)
job_words = preprocess(job_text)

# 🔥 STATIC SKILL EXTRACTION (Accurate)
static_job_skills = extract_skills(job_words, skills_list)
static_resume_skills = extract_skills(resume_words, skills_list)

# 🔥 DYNAMIC KEYWORDS (Flexible)
common_useless = {
    'looking', 'candidate', 'experience',
    'must', 'strong', 'good', 'have',
    'skills', 'ability', 'knowledge',
    'understanding', 'familiar', 'etc',
    'using', 'based', 'work', 'working',
    'fundamentals'
}

dynamic_job_skills = [
    word for word in extract_keywords(job_words)
    if word not in common_useless
    and len(word) > 2
    and word.isalpha()
]
# 🔥 HYBRID COMBINATION
# Remove words that are part of longer phrases
def clean_skills(skills):
    final_skills = []
    
    for skill in skills:
        if not any(skill != other and skill in other for other in skills):
            final_skills.append(skill)
    
    return final_skills
# 🔥 HYBRID COMBINATION

# Remove words that are part of longer phrases
def clean_skills(skills):
    final_skills = []
    
    for skill in skills:
        if not any(skill != other and skill in other for other in skills):
            final_skills.append(skill)
    
    return final_skills


def final_filter(skills):
    useless = {
        'must', 'strong', 'fundamentals',
        'looking', 'candidate', 'experience',
        'good', 'have', 'skills', 'ability',
        'knowledge', 'understanding', 'familiar',
        'etc', 'using', 'based', 'work', 'working'
    }

    return [skill for skill in skills if skill not in useless]
# job_skills = clean_skills(list(set(static_job_skills + dynamic_job_skills)))
job_skills = clean_skills(list(set(static_job_skills + dynamic_job_skills)))
job_skills = final_filter(job_skills)

job_skills = [
    skill for skill in job_skills
    if skill not in common_useless
]
# Match resume against job skills
resume_text_clean = " ".join(resume_words)

resume_skills = [
    skill for skill in job_skills
    if f" {skill} " in f" {resume_text_clean} "
]# Rule-based analysis
missing_skills = skill_gap(resume_skills, job_skills)
score = match_score(resume_skills, job_skills)

# ML-based similarity
similarity_score = compute_similarity(resume_words, job_words)

print("\n===== ANALYSIS RESULT =====")
print("\nResume Skills:", resume_skills)
print("Job Skills:", job_skills)

print("\nMissing Skills:", missing_skills)
print("\nSkill Match Score:", round(score, 2), "%")
print("Cosine Similarity Score:", round(similarity_score, 3))