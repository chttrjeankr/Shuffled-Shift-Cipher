# def step_creator(passcode):
#     """
#
#     :param passcode: takes a string
#     :return:
#     """
#     steps = 0
#     for i in passcode:
#         steps += ord(i)
#     steps = make_one_digit(steps)
#     return len(passcode) if steps == 1 else steps
