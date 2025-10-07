from transformers import pipeline

# Load FLAN-T5 base model (fast + free)
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_summary(interpretation):
    prompt = "What is a short health summary and advice based on these blood test results?\n"
    for test, info in interpretation.items():
        prompt += f"{test}: {info['value']} ({info['status']})\n"

    response = generator(prompt, max_new_tokens=150)
    return response[0]['generated_text']