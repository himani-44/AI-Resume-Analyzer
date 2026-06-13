skills_database = [

    # Programming
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "SQL",

    # Core CS
    "Data Structures",
    "Algorithms",
    "DBMS",
    "Database Management Systems",
    "Operating Systems",
    "OOP",
    "Object-Oriented Programming",

    # AI / ML
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "LLM",
    "RAG",
    "Embeddings",

    # Data
    "Data Analysis",
    "Pandas",
    "NumPy",
    "Power BI",
    "PostgreSQL",

    # Web
    "Flask",
    "Django",
    "FastAPI",
    "React",
    "Node.js",
    "REST API",
    "REST APIs",

    # Tools
    "Git",
    "Docker",
    "AWS",
    "Streamlit",

    # Modern AI
    "LangChain",
    "LangGraph",
    "OpenAI",
    "CrewAI",
    "Pinecone",
    "FAISS",
    "ChromaDB",
    "Vector Database",

    # Software Engineering
    "SDLC",
    "Agile",
    "Workflow Automation"
]


aliases = {

    # LLM
    "large language model": "LLM",
    "large language models": "LLM",
    "llms": "LLM",

    # NLP
    "natural language processing": "NLP",

    # RAG
    "retrieval augmented generation": "RAG",

    # PostgreSQL
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    # OOP
    "object oriented programming": "Object-Oriented Programming",

    # DBMS
    "database management system": "Database Management Systems",

    # REST
    "restful api": "REST API",
    "restful apis": "REST APIs",

    # ML
    "ml": "Machine Learning",

    # AI
    "artificial intelligence": "AI",

    # Embeddings
    "vector embeddings": "Embeddings"
}


def extract_skills(text):

    found_skills = []

    text_lower = text.lower()

    # Direct Skill Matching

    for skill in skills_database:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    # Alias Matching

    for alias, actual_skill in aliases.items():

        if alias in text_lower:
            found_skills.append(actual_skill)

    return list(set(found_skills))