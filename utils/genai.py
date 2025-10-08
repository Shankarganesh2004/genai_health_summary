import requests
def generate_summary(interpretation):
    prompt = "Summarize the following blood test results and provide short health advice:\n\n"
    for test, info in interpretation.items():
        prompt += f"{test}: {info['value']} ({info['status']})\n"

    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.perplexity.ai/chat/completions", headers=headers, json=payload)
    result = response.json()

    # Debug print to inspect structure
    print("API response:", result)

     # Safe access
    if 'choices' in result and result['choices']:
        return result['choices'][0]['message']['content']
    else:
        return "Sorry, the model did not return a valid summary."
