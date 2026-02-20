# Exercise 2: Student Grade Analyzer

student_records = []

# Collect student data with for and create 3 variables
for i in range(1, 7):
    name = input(f"Student {i} name: ")
    score = int(input(f"Student {i} score: "))
    student_records.append((name, score))

# Extract scores
scores = [score for name, score in student_records]

# Calculate statistics with highest lowest and average
stats = {}
stats['highest'] = max(scores)
stats['lowest'] = min(scores)
stats['average'] = sum(scores) / len(scores)

# Find unique scores
unique_scores = set(scores)

# Count grade distribution
grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

# Display results
print("\n=== STUDENT RECORDS ===")
for i, (name, score) in enumerate(student_records, 1):
    print(f"{i}. {name}: {score}")

print("\n=== CLASS STATISTICS ===")
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")

print("\n=== UNIQUE SCORES ===")
print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")

print("\n=== GRADE DISTRIBUTION ===")
for score, count in grade_distribution.items():
    if count == 1:
        print(f"Score {score}: {count} student")
    else:
        print(f"Score {score}: {count} students")
