def skill_gap(resume_skills, job_skills):
    return [skill for skill in job_skills if skill not in resume_skills]


def match_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0
    
    match_count = sum(1 for skill in job_skills if skill in resume_skills)
    
    return (match_count / len(job_skills)) * 100