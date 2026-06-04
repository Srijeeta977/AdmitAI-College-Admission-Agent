from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Credentials
API_KEY = "qO2Od-_wFbqYk-z-rHUsjx2n9bfkrIPBuD--nIZJCcv5"
PROJECT_ID = "f5320c3b-1459-4518-80fb-5ddec4e556f2"
URL = "https://au-syd.ml.cloud.ibm.com"

# Model Parameters
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
    "temperature": 0.7
}

# Granite Model
model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    params=parameters,
    credentials={
        "apikey": API_KEY,
        "url": URL
    },
    project_id=PROJECT_ID
)

print("\n🎓 AdmitAI College Admission Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("Student: ")

    if question.lower() == "exit":
        break

    prompt = f"""
You are AdmitAI, an intelligent college admission assistant.

Answer clearly and professionally.

Student Question:
{question}
"""

    response = model.generate_text(prompt=prompt)

    print("\nAdmitAI:", response)
    print("\n")