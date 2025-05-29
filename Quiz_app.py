import tkinter as tk

# Quiz data
questions = [
    "What is the maximum number of overs allowed in an ODI?",
    "Who was the first cricketer to score 100 international centuries?",
    "Which country won the ICC Cricket World Cup in 2019?"
]

options = [
    ["50", "60", "20"],
    ["Virat", "Sachin", "Kohli"],
    ["England", "India", "Sri Lanka"]
]

answers = ["50", "Sachin", "England"]

# Quiz state
current_q = 0
score = 0

# Check answer
def check_answer(choice):
    global current_q, score
    if options[current_q][choice] == answers[current_q]:
        feedback_label.config(text="✅ Correct!", fg="green")
        score += 1
    else:
        feedback_label.config(
            text=f"❌ Wrong! Correct answer: {answers[current_q]}", fg="red"
        )
    
    next_button.config(state="normal")
    for btn in option_buttons:
        btn.config(state="disabled")

# Move to next question
def next_question():
    global current_q
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        show_result()

# Load question
def load_question():
    question_label.config(text=questions[current_q])
    feedback_label.config(text="")
    for i, btn in enumerate(option_buttons):
        btn.config(text=options[current_q][i], state="normal", command=lambda i=i: check_answer(i))
    next_button.config(state="disabled")

# Show final result
def show_result():
    question_label.config(text=f"🎉 Quiz Complete!\nYour score: {score}/{len(questions)}")
    for btn in option_buttons:
        btn.pack_forget()
    feedback_label.config(text="")
    next_button.pack_forget()

# Setup GUI
root = tk.Tk()
root.title("Cricket Quiz App")
root.geometry("500x400")

question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=450, justify="center")
question_label.pack(pady=20)

option_buttons = []
for i in range(3):
    btn = tk.Button(root, text="", font=("Helvetica", 12), width=25)
    btn.pack(pady=5)
    option_buttons.append(btn)

feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
feedback_label.pack(pady=10)

next_button = tk.Button(root, text="Next", font=("Helvetica", 12), command=next_question, state="disabled")
next_button.pack(pady=10)

load_question()
root.mainloop()