import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.skills import extract_skills
from utils.similarity import compare_skills
from utils.feedback import generate_feedback
from utils.semantic_similarity import calculate_semantic_similarity


st.title("AI RESUME ANALYZER")
st.write("Welcome to the AI Resume Analyzer!")

job_description = st.text_area("Paste Job Description Here")


# single file is being uploaded we changed to multiple resume files
# can be uploaded and processed in one go.

uploaded_files = st.file_uploader(
    "Upload Your Resumes (PDF only)",
    type=["pdf"],
    accept_multiple_files=True
)


# uploaded_files now stores a list of PDF files
# example:
# [resume1.pdf, resume2.pdf, resume3.pdf]

if uploaded_files:

    
    results = []

    # extracting jd skills once because job description remains same
    jd_skills = extract_skills(job_description)

    # loop through every uploaded resume
    for file in uploaded_files:

        # extract text from current resume
        resume_text = extract_text_from_pdf(file)

        # extract skills from resume
        found_skills = extract_skills(resume_text)

        # compare resume skills with jd skills
        matched_skills, missing_skills, match_percentage = compare_skills(
            found_skills,
            jd_skills
        )

        # semantic similarity using embeddings
        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_description
        )

        # ATS Score
        # 60% skill matching
        # 40% semantic similarity

        ats_score = (
            match_percentage * 0.6
            + semantic_score * 0.4
        )
        ats_score =round(ats_score, 2)

        # store everything for this resume
        results.append({

            "resume_name": file.name,

            "resume_text": resume_text,

            "detected_skills": found_skills,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "match_percentage": round(match_percentage, 2),

            "semantic_score": round(semantic_score, 2),

            "ats_score": round(ats_score, 2)

        })

    # sorting resumes based on ATS score
    # highest score comes first

    results.sort(
        key=lambda x: x["ats_score"],
        reverse=True
    ) # basically taking in a dictionary sorting using ats score and reverse true means highest score first 

    st.subheader("Resume Ranking")

    for result in results:

        st.write(
            f"{result['resume_name']} : {result['ats_score']}%"
        )
    # highest scoring resume after sorting 
    best_resume = results[0]
    st.success(
        f"Recommended Resume: {results[0]['resume_name']}"
    )

    # st.subheader("Detailed Analysis")

    # # show complete analysis for every resume

    # for result in results:

    #     st.markdown("---")

    #     st.subheader(result["resume_name"])

    #     st.subheader("Detected Skills")
    #     st.write(result["detected_skills"])

    #     st.subheader("JD Skills")
    #     st.write(jd_skills)

    #     st.subheader("Matched Skills")
    #     st.write(result["matched_skills"])

    #     st.subheader("Missing Skills")
    #     st.write(result["missing_skills"])

    #     st.subheader("Match Percentage")
    #     st.write(f"{result['match_percentage']}%")

    #     st.subheader("Semantic Similarity Score")
    #     st.write(f"{result['semantic_score']}%")

    #     st.subheader("ATS Score")
    #     st.write(f"{result['ats_score']}%")

    #     feedback = generate_feedback(
    #         result["match_percentage"],
    #         result["missing_skills"]
    #     )

    #     st.subheader("ATS Feedback")

    #     for item in feedback:
    #         st.write(item)


    st.subheader("Recommended Resume Analysis")

    st.subheader("Resume Name")
    st.write(best_resume["resume_name"])

    st.subheader("Detected Skills")
    st.write(best_resume["detected_skills"])

    st.subheader("JD Skills")
    st.write(jd_skills)

    st.subheader("Matched Skills")
    st.write(best_resume["matched_skills"])

    st.subheader("Missing Skills")
    st.write(best_resume["missing_skills"])

    st.subheader("Match Percentage")
    st.write(f"{best_resume['match_percentage']}%")

    st.subheader("Semantic Similarity Score")
    st.write(f"{round(best_resume['semantic_score'], 2)}%")

    st.subheader("ATS Score")
    st.write(f"{round(best_resume['ats_score'], 2)}%")

    st.subheader("Why This Resume Was Recommended")

    st.write(
    f"""
    This resume achieved the highest ATS Score of
    {best_resume['ats_score']}%.

    
    It matched {len(best_resume['matched_skills'])}
    skills from the job description.

    Missing Skills:
    {', '.join(best_resume['missing_skills'])}
    """
    

    )

    feedback = generate_feedback(
    best_resume["match_percentage"],
    best_resume["missing_skills"]
    )

    st.subheader("ATS Feedback")

    for item in feedback:
        st.write(item)
