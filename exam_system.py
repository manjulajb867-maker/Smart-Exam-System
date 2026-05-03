import json
import threading

EXAM_FILE = "exam.json"
STUDENT_FILE = "students.json"
RESULT_FILE = "results.json"

lock = threading.Lock()

# 1. Create Exam
def create_exam():
    exam = {
        "questions": [
            {"q": "2 + 2 = ?", "options": ["2", "4", "6"], "answer": "4"},
            {"q": "Capital of India?", "options": ["Delhi", "Mumbai", "Chennai"], "answer": "Delhi"}
        ]
    }

    with open(EXAM_FILE, "w") as f:
        json.dump(exam, f)

    print("✅ Exam created!")

# 2. Register Student
def register_student(name):
    with lock:
        try:
            with open(STUDENT_FILE, "r") as f:
                students = json.load(f)
        except:
            students = []

        seat = len(students) + 1
        students.append({"name": name, "seat": seat})

        with open(STUDENT_FILE, "w") as f:
            json.dump(students, f)

        print(f"✅ {name} got seat {seat}")

# 3. Take Exam
def take_exam(student_name):
    with open(EXAM_FILE, "r") as f:
        exam = json.load(f)

    answers = []

    print("\n📝 Exam for", student_name)

    for q in exam["questions"]:
        print("\n", q["q"])
        print("Options:", q["options"])
        ans = input("Enter answer: ")
        answers.append(ans)

    evaluate(student_name, answers)

# 4. Evaluate
def evaluate(student_name, answers):
    with open(EXAM_FILE, "r") as f:
        exam = json.load(f)

    score = 0

    for i, q in enumerate(exam["questions"]):
        if answers[i] == q["answer"]:
            score += 1

    with open(RESULT_FILE, "r") as f:
        results = json.load(f)

    results.append({"name": student_name, "score": score})

    with open(RESULT_FILE, "w") as f:
        json.dump(results, f)

    print(f"🎯 {student_name} score: {score}")

# 5. Show Results
def show_results():
    with open(RESULT_FILE, "r") as f:
        results = json.load(f)

    print("\n📊 Results:")
    for r in results:
        print(r)
