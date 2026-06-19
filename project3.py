courses = {
    "Python Basics": ["python", "programming"],
    "Java Programming": ["java", "programming"],
    "Machine Learning Fundamentals": ["machine learning", "ai"],
    "AI with Python": ["ai", "python"],
    "Web Development": ["html", "css", "javascript"]
}

user_interests = input("Enter interests separated by commas: ").lower().split(",")

scores = {}

for course, tags in courses.items():
    score = 0
    for interest in user_interests:
        if interest.strip() in tags:
            score += 1
    scores[course] = score

recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("\nRecommended Courses:")
for course, score in recommended:
    if score > 0:
        print(course, "- Match Score:", score)