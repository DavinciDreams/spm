import json
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Industry and skills data
industries = ["Tech", "Healthcare", "Design", "Finance", "Education"]
skills_list = {
    "Tech": ["Python", "JavaScript", "AWS", "Docker", "SQL"],
    "Healthcare": ["Patient Care", "EMR", "Medical Coding", "HIPAA Compliance"],
    "Design": ["Photoshop", "Figma", "Illustrator", "UI/UX"],
    "Finance": ["Excel", "QuickBooks", "Financial Modeling", "Risk Analysis"],
    "Education": ["Curriculum Design", "Teaching", "E-Learning", "Assessment"]
}

# Random date generator
def random_date(start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Generate a single resume
def generate_resume(with_error=False):
    industry = random.choice(industries)
    resume = {
        "basics": {
            "name": fake.name(),
            "label": f"{random.choice(['Junior', 'Senior', ''])} {industry} Professional",
            "email": fake.email(),
            "phone": fake.phone_number(),
            "summary": fake.paragraph(nb_sentences=2),
            "location": {
                "city": fake.city(),
                "countryCode": fake.country_code(),
            },
            "profiles": [
                {
                    "network": random.choice(["GitHub", "LinkedIn", "Behance"]),
                    "username": fake.user_name(),
                    "url": fake.url()
                }
            ]
        },
        "work": [
            {
                "name": fake.company(),
                "position": f"{random.choice(['Analyst', 'Engineer', 'Designer', 'Manager'])}",
                "startDate": random_date(2018, 2023),
                "endDate": random_date(2023, 2025) if random.random() > 0.2 else "Present",
                "summary": fake.paragraph(nb_sentences=1),
                "highlights": [fake.sentence() for _ in range(random.randint(1, 3))]
            }
        ],
        "education": [
            {
                "institution": fake.company() + " University",
                "area": random.choice(["Computer Science", "Business", "Art", "Medicine"]),
                "studyType": random.choice(["B.S.", "M.A.", "Ph.D."]),
                "startDate": random_date(2010, 2018),
                "endDate": random_date(2018, 2022)
            }
        ],
        "skills": [
            {
                "name": industry + " Skills",
                "keywords": random.sample(skills_list[industry], random.randint(2, 4))
            }
        ]
    }

    # Introduce errors if specified
    if with_error:
        error_type = random.choice([
            "missing_field", "invalid_date", "wrong_type", "empty_field"
        ])
        if error_type == "missing_field":
            del resume["basics"]["email"]
        elif error_type == "invalid_date":
            resume["work"][0]["startDate"] = "2025-13-01"
        elif error_type == "wrong_type":
            resume["basics"]["phone"] = 12345
        elif error_type == "empty_field":
            resume["education"][0]["institution"] = ""
    return resume

# Generate prompt-response pairs
def generate_prompt_response_pairs(num_entries=10):
    dataset = []
    num_errors = int(num_entries * 0.3)  # 30% with errors
    num_valid = num_entries - num_errors

    # Valid resumes with various tasks
    for _ in range(num_valid):
        resume = generate_resume(with_error=False)
        task_type = random.choice(["add_work", "analyze"])
        if task_type == "add_work":
            new_work = {
                "name": fake.company(),
                "position": "Team Lead",
                "startDate": random_date(2022, 2024),
                "endDate": "Present",
                "summary": "Led a team to improve workflows."
            }
            updated_resume = resume.copy()
            updated_resume["work"].append(new_work)
            entry = {
                "instruction": "Add a new work experience to this resume.",
                "input": json.dumps(resume),
                "output": json.dumps(updated_resume)
            }
        else:  # analyze
            entry = {
                "instruction": "What’s wrong with this resume?",
                "input": json.dumps(resume),
                "output": "This resume appears to be valid and follows the JSON Resume schema."
            }
        dataset.append(entry)

    # Resumes with errors
    for _ in range(num_errors):
        error_resume = generate_resume(with_error=True)
        fixed_resume = error_resume.copy()
        
        # Fix the specific error
        if "email" not in error_resume["basics"]:
            fixed_resume["basics"]["email"] = fake.email()
            error_desc = "The 'email' field is missing in 'basics'."
        elif error_resume["work"][0]["startDate"] == "2025-13-01":
            fixed_resume["work"][0]["startDate"] = random_date(2018, 2023)
            error_desc = "The 'startDate' in 'work' is invalid (month 13 does not exist)."
        elif isinstance(error_resume["basics"]["phone"], int):
            fixed_resume["basics"]["phone"] = fake.phone_number()
            error_desc = "The 'phone' field in 'basics' should be a string, not an integer."
        elif error_resume["education"][0]["institution"] == "":
            fixed_resume["education"][0]["institution"] = fake.company() + " University"
            error_desc = "The 'institution' field in 'education' is empty."

        entry = {
            "instruction": "Fix this resume.",
            "input": json.dumps(error_resume),
            "output": json.dumps(fixed_resume)
        }
        dataset.append(entry)

    return dataset

# Main execution
if __name__ == "__main__":
    # Generate 10 prompt-response pairs
    prompt_response_data = generate_prompt_response_pairs(10)

    # Save to JSONL file
    with open("synthetic_resumes_prompt_response.jsonl", "w") as f:
        for entry in prompt_response_data:
            f.write(json.dumps(entry) + "\n")

    print(f"Generated {len(prompt_response_data)} prompt-response pairs and saved to 'synthetic_resumes_prompt_response.jsonl'.")