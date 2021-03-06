class Questionnaire:
    def __init__(self):
        self.questions = []

        with open("CovApp.txt") as f:
            questions = []

            current_question = None
            current_alternatives = []

            for line in f.readlines():
                if line.startswith("\t\t "):  # answer
                    current_alternatives.append(line[3:-1])
                elif line.startswith("\t\t"):  # question
                    if current_question:
                        # clear old question
                        questions.append(
                            {
                                "question": current_question,
                                "alternatives": current_alternatives,
                            }
                        )

                    current_question = line[2:-1]
                    current_alternatives = []

            self.questions = questions

    def __call__(self, update, context):
        update.message.reply_text(":wave:")


def get_score(questions):
    score = 0.0

    for index, question in enumerate(questions):
        print(question["question"])
        print(question["alternatives"])

        number = int(input())
        answer = question["alternatives"][number]

        print(f"Your answer is {answer}")

        if index > 2:
            if number == 0:
                score += 1.0
            if number == 1:
                pass
            if number == 2:
                score += 0.5

    return score
