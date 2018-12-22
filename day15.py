# When is a number not itself? and copy / deepcopy exercise.
# https://www.interviewcake.com/python-interview-questions
import copy

big_num_1 = 1000
big_num_2 = 1000
small_num_1 = 1
small_num_2 = 1


def singleton():
    # Python ranges start at 0 and don't include the last number
    for num in range(1001):

        # try to create a new object
        num_copy = num * 1

        if num is num_copy:
            print(num, "is a singleton")
        else:
            print(num, "is not a singleton")


def foo():
    print(big_num_1 is big_num_2)
    print(small_num_1 is small_num_2)


question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
}


def make_new_question(title, question, answer, hints=None):
    # new_q = question_template.copy()
    new_q = copy.deepcopy(question_template)

    # always require title, question, answer
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    # sometimes there aren't hints, that's fine. Otherwise, add them:
    if hints is not None:
        new_q["hints"].extend(hints)

    return new_q


if __name__ == '__main__':
    question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
    question_2 = make_new_question("title2", "question2", "answer2")
    question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])
    x = 1
