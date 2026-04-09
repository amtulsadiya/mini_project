# import streamlit as st
# from preprocess import preprocess
# from matcher import skill_gap, match_score
# from similarity import compute_similarity
# from skill_extractor import load_skills, extract_skills, extract_keywords
# from pdf_reader import extract_text_from_pdf
# from semantic_matcher import semantic_skill_match


# # Title
# st.title("AI Skill Gap Analyzer")

# # Inputs
# st.header("Upload Resume (PDF)")
# resume_file = st.file_uploader("Upload Resume", type=["pdf"])

# st.header("Paste Job Description")
# job_text = st.text_area("Enter Job Description")

# # Load skills
# skills_list = load_skills("data/skills.txt")

# if st.button("Analyze"):
#     if resume_file and job_text:

#         # Extract resume text
#         resume_text = extract_text_from_pdf(resume_file)

#         # Preprocess
#         resume_words = preprocess(resume_text)
#         job_words = preprocess(job_text)

#         # Static skills
#         static_job_skills = extract_skills(job_words, skills_list)

#         # Dynamic keywords
#         common_useless = {'looking', 'candidate', 'experience'}
#         dynamic_job_skills = [
#             word for word in extract_keywords(job_words)
#             if word not in common_useless and len(word) > 2
#         ]

#         # Clean skills
#         def clean_skills(skills):
#             final = []
#             for skill in skills:
#                 if not any(skill != other and skill in other for other in skills):
#                     final.append(skill)
#             return final

#         job_skills = clean_skills(list(set(static_job_skills + dynamic_job_skills)))

#         # Match using text
#         resume_text_clean = " ".join(resume_words)
#         # resume_skills = [skill for skill in job_skills if skill in resume_text_clean]

#         # Analysis
#         # missing_skills = skill_gap(resume_skills, job_skills)
#         # score = match_score(resume_skills, job_skills)


# matched_skills, missing_skills = semantic_skill_match(
#         resume_skills=resume_words,
#         job_skills=job_skills
#         )

# score = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

# similarity_score = compute_similarity(resume_words, job_words)
# st.write("DEBUG Job Skills Before Filter:", static_job_skills + dynamic_job_skills)
#         st.write("DEBUG After Clean:", clean_skills(list(set(static_job_skills + dynamic_job_skills))))
#         st.write("DEBUG After Final Filter:", job_skills)
#         # Output
#         st.subheader("Results")

#         # st.write("Resume Skills:", resume_skills)
#         st.write("Job Skills:", job_skills)
#         st.write("Missing Skills:", missing_skills)

#         st.write("Skill Match Score:", round(score, 2), "%")
#         st.write("Cosine Similarity:", round(similarity_score, 3))

#     else:
#         st.warning("Please upload resume and enter job description")

import streamlit as st

from preprocess import preprocess
from similarity import compute_similarity
from skill_extractor import load_skills, extract_skills, extract_keywords
from pdf_reader import extract_text_from_pdf
from semantic_matcher import semantic_skill_match

# Title
st.title("AI Skill Gap Analyzer")

# Inputs
st.header("Upload Resume (PDF)")
resume_file = st.file_uploader("Upload Resume", type=["pdf"])

st.header("Paste Job Description")
job_text = st.text_area("Enter Job Description")

# Load skills
skills_list = load_skills("data/skills.txt")
def final_skill_filter(skills):
    blacklist = {
        'ability', 'analytical', 'analysis', 'concepts',
        'consulting', 'experience', 'knowledge',
        'understanding', 'skills', 'skill',
        'strong', 'good', 'must', 'should',
        'work', 'working', 'based'
    }

    clean = []
    for skill in skills:
        if skill not in blacklist and len(skill) > 2:
            clean.append(skill)

    return clean
if st.button("Analyze"):
    if resume_file and job_text:

        # Extract resume text
        resume_text = extract_text_from_pdf(resume_file)

        # Preprocess
        resume_words = preprocess(resume_text)
        job_words = preprocess(job_text)

        # -----------------------------
        # 🔥 STEP 1: STATIC SKILLS
        # -----------------------------
        static_job_skills = extract_skills(job_words, skills_list)

        # -----------------------------
        #  STEP 2: DYNAMIC (optional)
        # -----------------------------
        common_useless = {'looking', 'candidate', 'experience'}

        dynamic_job_skills = [
            word for word in extract_keywords(job_words)
            if word not in common_useless and len(word) > 2
        ]

        # -----------------------------
        #  STEP 3: CLEAN SKILLS
        # -----------------------------
        def clean_skills(skills):
            final = []
            for skill in skills:
                if not any(skill != other and skill in other for other in skills):
                    final.append(skill)
            return final

        # job_skills = clean_skills(static_job_skills )
        job_skills = list(set(clean_skills(static_job_skills)))
        # job_skills = clean_skills(list(set(static_job_skills + dynamic_job_skills)))
        # job_skills = final_skill_filter(job_skills)

        # -----------------------------
        #  STEP 4: SEMANTIC MATCHING
        # -----------------------------
        matched_skills, missing_skills = semantic_skill_match(
            resume_skills=resume_words,   # use full resume context
            job_skills=job_skills
        )
        matched_skills = list(set(matched_skills))
        missing_skills = list(set(missing_skills))

        # Score
        score = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

        # Similarity
        similarity_score = compute_similarity(resume_words, job_words)

        # -----------------------------
        #  DEBUG (optional)
        # -----------------------------
        st.write("DEBUG Job Skills Before Filter:", static_job_skills + dynamic_job_skills)
        st.write("DEBUG After Clean:", job_skills)

        # -----------------------------
        #  OUTPUT
        # -----------------------------
        st.subheader("Results")

        st.write("Matched Skills:", matched_skills)
        st.write("Job Skills:", job_skills)
        st.write("Missing Skills:", missing_skills)

        st.write("Skill Match Score:", round(score, 2), "%")
        st.write("Cosine Similarity:", round(similarity_score, 3))

    else:
        st.warning("Please upload resume and enter job description")
