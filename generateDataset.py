from transformers import pipeline

# List below is a list of questions that can be used to generate synthetic data

questions = ["What does this code do?"];

dataset = [];

for question in questions:
    generator = pipeline("text-generation", model="YWZBrandon/openai-gsm8k_meta-llama-Llama-3.2-3B_2e-5", device="cuda")

    messages = []

    # make a system prompt 
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    # load the codebase in maybase as an assitent role
    # import the jsonresume_repo_dump.md file from local
    with open("jsonresume_repo_dump.md", "r") as f:
        codebase = f.read()
    messages.append({"role": "system", "content": codebase})

    messages.append({"role": "user", "content": question})

    output = generator(messages, max_new_tokens=128, return_full_text=False)[0]

    dataset.append({"question": question, "answer": output["generated_text"]})

return dataset