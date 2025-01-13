def scored(answers, true_answers):
    score = 0
    for i in range(len(answers)):
        if answers[i] == true_answers[i]:
            score += 1
        else:
            score = score
    return score


def percentage_scored(score, number_of_questions):
    return (score / number_of_questions) * 100
