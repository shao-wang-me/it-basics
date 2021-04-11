from math import inf
from os import listdir
from os.path import isfile, join

leetcode_path = 'LeetCode'

markdown = '''# LeetCode题目

| 题目 | 标签 |
| --- | --- |
'''

problems = []

for file_name in listdir(leetcode_path):
    if file_name.endswith('.py'):
        problem = file_name[:-3]
        problems.append(problem)


def get_problem_number(problem: str):
    problem_number = problem[:problem.rfind('.')]
    return int(problem_number) if problem_number.isdigit() else inf


problems.sort(key=get_problem_number)

for problem in problems:
    file_name = problem + '.py'
    path = join(leetcode_path, file_name)
    if isfile(path):
        with open(path, encoding='utf-8') as f:
            first_line = f.readline()
            tags = ''
            if first_line.startswith('# Tags: '):
                tags = first_line[8:].strip()
            markdown += f'| {problem} | {tags} |\n'

print(markdown)

with open('LeetCode题目.md', 'w', encoding='utf-8') as f:
    f.write(markdown)
