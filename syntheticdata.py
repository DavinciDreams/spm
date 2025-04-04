import json
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for synthetic data
fake = Faker()

# List of possible industries and skills for variety
industries = ["Tech", "Healthcare", "Design", "Finance", "Education"]
skills_list = {
    "Tech": ["Python", "JavaScript", "AWS", "Docker", "SQL"],
    "Healthcare": ["Patient Care", "EMR", "Medical Coding", "HIPAA Compliance"],
    "Design": ["Photoshop", "Figma", "Illustrator", "UI/UX"],
    "Finance": ["Excel", "QuickBooks", "Financial Modeling", "Risk Analysis"],
    "Education": ["Curriculum Design", "Teaching", "E-Learning", "Assessment"]
}

# Function to generate a random date within a range
def random_date(start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Function to generate a single resume (valid or with errors)
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

    # Introduce errors if with_error is True
    if with_error:
        error_type = random.choice([
            "missing_field", "invalid_date", "wrong_type", "empty_field"
        ])
        if error_type == "missing_field":
            del resume["basics"]["email"]  # Missing required field
        elif error_type == "invalid_date":
            resume["work"][0]["startDate"] = "2025-13-01"  # Invalid month
        elif error_type == "wrong_type":
            resume["basics"]["phone"] = 12345  # Should be string, not int
        elif error_type == "empty_field":
            resume["education"][0]["institution"] = ""  # Empty string

    return resume

# Generate dataset
def generate_dataset(num_entries=10):
    dataset = []
    num_errors = int(num_entries * 0.3)  # 30% of resumes will have errors
    num_valid = num_entries - num_errors

    # Generate valid resumes
    for _ in range(num_valid):
        dataset.append(generate_resume(with_error=False))

    # Generate resumes with errors
    for _ in range(num_errors):
        dataset.append(generate_resume(with_error=True))

    return dataset

# Main execution
if __name__ == "__main__":
    # Generate 10 resumes
    synthetic_resumes = generate_dataset(10)

    # Save to file
    with open("synthetic_resumes.json", "w") as f:
        json.dump(synthetic_resumes, f, indent=2)

    print(f"Generated {len(synthetic_resumes)} resumes and saved to 'synthetic_resumes.json'.")