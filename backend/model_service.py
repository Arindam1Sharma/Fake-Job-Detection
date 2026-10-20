from pathlib import Path

import tensorflow as tf
from sentence_transformers import SentenceTransformer


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Model paths
MLP_PATH = BASE_DIR / "models" / "semantic_mlp_final.keras"
EMBEDDING_MODEL_PATH = BASE_DIR / "models" / "all-MiniLM-L6-v2"


print("Loading Sentence Transformer...")
embedding_model = SentenceTransformer(str(EMBEDDING_MODEL_PATH))

print("Loading MLP classifier...")
mlp_model = tf.keras.models.load_model(MLP_PATH)

print("Models loaded successfully.")


def predict_job_fraud(
    title="",
    company_profile="",
    description="",
    requirements="",
    benefits="",
    employment_type="",
    location="",
    salary_range="",
    industry="",
    function=""
):
    structured_text = (
        f"Title: {title} | "
        f"Company: {company_profile} | "
        f"Description: {description} | "
        f"Requirements: {requirements} | "
        f"Benefits: {benefits} | "
        f"Employment Type: {employment_type} | "
        f"Location: {location} | "
        f"Salary: {salary_range} | "
        f"Industry: {industry} | "
        f"Function: {function}"
    )

    embedding = embedding_model.encode(
        [structured_text],
        convert_to_numpy=True
    )

    fraud_probability = float(
        mlp_model.predict(embedding, verbose=0)[0][0]
    )

    prediction = int(fraud_probability >= 0.5)

    return {
        "fraud_probability": fraud_probability,
        "prediction": prediction
    }