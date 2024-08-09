def arithmetic_arranger(problems, show_answers=False):
    check1 = check_num_problems(problems)
    check2 = check_nums(problems)
    
    firsts, operators, seconds = gen_lists(problems)
    check3 = check_num_length([firsts,seconds])
    check4 = check_ops(operators)
    spaces = calc_n_spaces(firsts,seconds)
    spaces2 = calc_n_spaces2(firsts,seconds)
    widths = calc_widths(firsts,seconds)
    spaces3 = calc_n_spaces3(problems, widths)
    answers = calc_answers(problems)

    checks = [check1, check2, check3, check4]
    messages = ['Error: Too many problems.', 'Error: Numbers must only contain digits.', 'Error: Numbers cannot be more than four digits.', "Error: Operator must be '+' or '-'."]

    result = ''.join([' '*space + num + ' '*4 for num, space in zip(firsts, spaces)]).rstrip()
    result2 = ''.join([operator + ' '*space + num + ' '*4 for operator, space, num in zip(operators, spaces2, seconds)]).rstrip()
    result3 = ''.join(['-'*width + ' '*4 for width in widths]).rstrip()
    result4 = ''.join([' '*space + ans + ' '*4 for space, ans in zip(spaces3, answers)]).rstrip()
    if True in checks:
        answer = messages[checks.index(True)]
    else:
        if show_answers == True:
            answer = f"{result}\n{result2}\n{result3}\n{result4}"
        else:
            answer = f"{result}\n{result2}\n{result3}"
    return answer


def check_num_problems(problems):
    if len(problems) > 5:
        return True
    else:
        return False


def check_nums(problems):
    has_chars = []
    for problem in problems:
        if any(char.isalpha() for char in problem):
            has_chars.append(True)
        else:
            has_chars.append(False)
    return True in has_chars


def check_num_length(num_lists):
    checks = []
    for num_list in num_lists:
        for num in num_list:
            if len(num) > 4:
                checks.append(True)
            else:
                checks.append(False)
    return True in checks


def check_ops(operators):
    for o in operators:
        if o not in ('+','-'):
            return True
        else:
            return False


def gen_lists(problems):
    firsts = [p.split(" ")[0] for p in problems]
    operators = [p.split(" ")[1] for p in problems]
    seconds = [p.split(" ")[2] for p in problems]
    return firsts, operators, seconds


def calc_first_n(firsts, seconds):
    if  len(firsts[0]) < len(seconds[0]):
        first_n = len(seconds[0]) - len(firsts[0]) + 2   
    else:
        first_n = 2
    return first_n


def calc_n_spaces(firsts, seconds):
    spaces = []
    first_n = calc_first_n(firsts, seconds)
    spaces.append(first_n)

    for i in range(1, len(firsts)):
        if len(firsts[i]) < len(seconds[i]):
            n = len(seconds[i]) - len(firsts[i]) + 2
        else:
            n = 2
        spaces.append(n)
    return spaces


def calc_first_n2(firsts, seconds):
    if  len(firsts[0]) > len(seconds[0]):
        first_n2 = len(firsts[0]) - len(seconds[0]) + 1   
    else:
        first_n2 = 1
    return first_n2


def calc_n_spaces2(firsts, seconds):
    spaces2 = []
    first_n = calc_first_n2(firsts, seconds)
    spaces2.append(first_n)

    for i in range(1, len(firsts)):
        if len(firsts[i]) > len(seconds[i]):
            n = len(firsts[i]) - len(seconds[i]) + 1
        else:
            n = 1
        spaces2.append(n)
    return spaces2


def calc_n_spaces3(problems, widths):
    spaces3 = []
    if check_nums(problems) == True:
        pass
    else:
        for i in range(len(problems)):
            space3 = widths[i] - len(str(eval(problems[i])))
            spaces3.append(space3)
    return spaces3


def calc_widths(firsts, seconds):
    widths = [max(len(firsts[i]), len(seconds[i])) + 2 for i in range(len(firsts))]
    return widths


def calc_answers(problems):
    if check_nums(problems) == True:
        answers = []
    else:
        answers = [str(eval(a)) for a in problems]  
    return answers


# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49","1 + 1", "2 + 3"], True)}')
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 4300", "123 + 49","1 + 1"], True)}')
# arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

# problems = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]
# test = check_nums(problems)
# print(test)