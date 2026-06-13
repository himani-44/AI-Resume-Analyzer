def generate_feedback(match_percentage, missing_skills):

    feedback = []

    # Overall Assessment

    if match_percentage >= 80:
        feedback.append("Overall Assessment: Excellent Match")

    elif match_percentage >= 60:
        feedback.append("Overall Assessment: Good Match")

    else:
        feedback.append("Overall Assessment: Needs Improvement")

    # Missing Skills Section

    if missing_skills:

        feedback.append("Areas for Improvement:")

        for skill in missing_skills:
            feedback.append(f"{skill}")

    # Recommendation Section

    if len(missing_skills) == 0:

        feedback.append(
            "Recommendation: Your resume aligns well with the job description."
        )

    else:

        feedback.append(
            "Recommendation: Consider adding projects, certifications, or practical experience related to the missing skills."
        )

    return feedback