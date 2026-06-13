def compare_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set  = set(jd_skills)
    matched_skills = list(resume_set.intersection(jd_set))
    missing_skills = list(jd_set - resume_set)
    if len(jd_set) > 0:
        match_percentage = ( len(matched_skills)/len(jd_set)) * 100
    else:
        match_percentage = 0
    return ( matched_skills, missing_skills, round(match_percentage, 2))
