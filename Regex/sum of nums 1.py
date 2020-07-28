import re
def count_nums(filename):
    text = open(filename)
    lines = text.readlines()
    lst_nums = []
    sum_nums = 0
    for line in lines:
        x = re.findall('\d+',line)
        if not x:
            continue
        lst_nums.append(x)
        for i in range(len(x)):
            number = x[i]
            convert_to_int = int(number)
            sum_nums += convert_to_int
    print(sum_nums)
count_nums('regex_sum_42.txt')
count_nums('regex_sum_735104.txt')


