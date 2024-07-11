empty_dict = {}

assert len(empty_dict) == 0

capitls = {"russia": "Moscow", "Germany": "Berlin", "France": "Paris"}

assert len(capitls) == 3
assert capitls["russia"] == "Moscow"
assert capitls.get("France") == "Paris"

capitls["Great Britain"] = "London"
assert capitls.get("Great Britain") == "London"

capitls["russia"] = "SPB"
assert capitls.get("russia") == "SPB"

print(capitls)

qa_skills = {
    "python": ["pytest", "requests", "allure", "selenium"],
    "databases": ["SQL", "SQLAlchme"],
    "theory": {
        "test design": ["tehnics", "test case"],
        "bug tracking": ["reporting", "lifecycle", "jira"],
    },
}

for skill in qa_skills.get("python"):
    print("python +", skill)

for db in qa_skills.get("databases"):
    print("Database +", db)

my_key = "theory"
assert qa_skills.get(my_key).get("bug tracking")[2] == "jira"

# добавление в qa_skills
qa_skills.get("theory")["tools"] = ["postman", "charles", "pair wise generator"]
