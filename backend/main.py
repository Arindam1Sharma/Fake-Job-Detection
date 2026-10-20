from fastapi import FastAPI
from pydantic import BaseModel

from model_service import predict_job_fraud


app = FastAPI(
    title="Fake Job Detection API",
    description="AI-powered API for detecting potentially fraudulent job postings.",
    version="1.0.0"
)


class JobPosting(BaseModel):
    title: str = ""
    company_profile: str = ""
    description: str = ""
    requirements: str = ""
    benefits: str = ""
    employment_type: str = ""
    location: str = ""
    salary_range: str = ""
    industry: str = ""
    function: str = ""


@app.get("/")
def root():
    return {
        "message": "Fake Job Detection API is running",
        "status": "online"
    }


@app.post("/predict")
def predict(job: JobPosting):

    result = predict_job_fraud(
        title=job.title,
        company_profile=job.company_profile,
        description=job.description,
        requirements=job.requirements,
        benefits=job.benefits,
        employment_type=job.employment_type,
        location=job.location,
        salary_range=job.salary_range,
        industry=job.industry,
        function=job.function
    )

    probability = result["fraud_probability"]

    if probability >= 0.5:
        prediction = "Potentially Fraudulent"
        risk_level = "High"
    else:
        prediction = "Likely Legitimate"
        risk_level = "Low"

    return {
        "prediction": prediction,
        "fraud_probability": probability,
        "risk_level": risk_level
    }