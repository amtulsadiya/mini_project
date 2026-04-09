from collections import Counter

# 🔹 Load skills from file
def load_skills(file_path):
    with open(file_path, 'r') as file:
        skills = [line.strip().lower() for line in file.readlines()]
    return skills


# 🔹 Extract skills using static list
def extract_skills(words, skills_list):
    text = " ".join(words)
    
    found_skills = []
    
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    
    return found_skills


# 🔹 Extract dynamic keywords
def extract_keywords(words, top_n=10):
    word_freq = Counter(words)
    common_words = word_freq.most_common(top_n)
    
    keywords = [word for word, freq in common_words]
    
    return keywords