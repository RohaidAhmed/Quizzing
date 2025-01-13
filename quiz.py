import random
import numpy as np


def quiz_questions(number_of_questions, test_num_range):
    ans = []
    true_ans = []
    low_limit, high_limit = test_num_range
    num = np.array(random.sample(range(low_limit, high_limit), number_of_questions))
    num2 = np.array(random.sample(range(low_limit, high_limit), number_of_questions))

    for i in range(number_of_questions):
        true_ans = num * num2
        ans.append(int(input("{} * {} = ".format(num[i], num2[i]))))
    return ans, true_ans
