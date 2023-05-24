import math
import random
import probability
from fraction import Frac


def solve(task):
    for s in solutions:
        if s.target == task.id:
            s.solution(task)
            break


class Solution:
    def __init__(self, target_task_id, task_solution):
        self.target = target_task_id
        self.solution = task_solution


def insert_answers(task, ans):
    for elem in task.ans.iter():
        if elem.text:
            if elem.text == 'n':
                if isinstance(ans[0], Frac):
                    elem.text = f'{ans[0].n}'
                else:
                    elem.text = f'{ans[0][0]}'
            elif elem.text == 'd':
                if isinstance(ans[0], Frac):
                    elem.text = f'{ans[0].d}'
                else:
                    elem.text = f'{ans[0][1]}'
                ans.pop(0)
            elif elem.text == 'v':
                if isinstance(ans[0], Frac):
                    elem.text = f'{ans[0].decimal()}'
                else:
                    elem.text = f'{ans[0]}'
                ans.pop(0)


def problem1(task):
    r2 = random.randrange(2, 9)
    r1 = random.randrange(r2 + 1, 10)

    ans = [Frac(r2 * r2, r1 * r1),
           Frac((r2 - 1) * (r2 - 1), ((r1 - 1) * (r2 - 1))),
           Frac(r2 - 1, r1 - 1),
           Frac(r2, r1)]

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(r1=r1, r2=r2)

    insert_answers(task, ans)


def problem2(task):
    k = random.randrange(3, 19)
    n = 6 * 6 * 6
    m = 0
    for cube1 in range(1, 7):
        for cube2 in range(1, 7):
            for cube3 in range(1, 7):
                if cube1 + cube2 + cube3 == k:
                    m += 1

    ans = [Frac(m, n), Frac(m + 1, n), Frac(1, k), Frac(k, n)]

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(k=k)

    insert_answers(task, ans)


def problem3(task):
    w = random.randrange(1, 11)
    b = random.randrange(1, 11)
    k = w + b

    ans = [Frac(2 * w * b, k * (k - 1)),
           Frac(w * b, k * (k - 1)),
           Frac(w, k),
           Frac(2 * w, k * (k - 1))]

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(b=b, w=w)

    insert_answers(task, ans)


def problem4(task):
    c1 = random.randrange(3, 7)
    k1 = 10 - c1
    count1 = c1 + k1

    c2 = random.randrange(3, 6)
    k2 = 9 - c2
    count2 = c2 + k2

    p = [Frac(c1, count1),
         Frac(k1, count1)]
    p_a = [Frac((c2 + 1), (count2 + 1)),
           Frac((k2 + 1), (count2 + 1))]

    ans = [p[0] * p_a[0] + p[1] * p_a[1],
           probability.rand_prob(2),
           probability.rand_prob(2),
           probability.rand_prob(2)]

    insert_answers(task, ans)
    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(c1=c1, k1=k1, c2=c2, k2=k2)


def problem5(task):
    u = random.randrange(10, 100, 10)
    f = 100 - u

    p_a1 = Frac(u, 100)
    p_a2 = Frac(f, 100)

    p_a1_a = probability.rand_prob(2)
    p_a2_a = probability.rand_prob(2)

    p_a = p_a1 * p_a1_a + p_a2 * p_a2_a
    p = (p_a1 * p_a1_a) / p_a

    ans = [p, probability.rand_prob(3), probability.rand_prob(3), probability.rand_prob(3)]

    insert_answers(task, ans)
    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(u=u, f=f, up=p_a1_a.decimal(2), fp=p_a2_a.decimal(2))


def problem6(task):
    x = probability.rand_unique_table(4, 1, 9)
    p = probability.rand_prob_table(4, 2)[0]

    start = random.randrange(0, 2)
    stop = random.randrange(start + 2, 4)

    b1 = x[start]
    b2 = x[stop]

    ans = [p[start + 1] + p[stop],
           p[start] + p[stop],
           p[start],
           p[stop]]

    insert_answers(task, ans)

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                if elem.text == '{x}':
                    elem.text = f'{x[0]}'
                    x.pop(0)
                elif elem.text == '{p}':
                    elem.text = f'{p[0].decimal(2)}'
                    p.pop(0)
                else:
                    elem.text = elem.text.format(b1=b1, b2=b2)


def problem7(task):
    bounds = probability.rand_unique_table(4, 1, 9)
    table = probability.rand_prob_table(4, 2)
    p = table[0]
    points = table[1]

    start = random.randrange(0, 2)
    stop = random.randrange(start + 2, 4)

    b1 = bounds[start]
    b2 = bounds[stop]

    ans = [p[start + 1] + p[stop],
           p[start] + p[stop],
           points[start],
           points[stop]]

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                if '{b1}' in elem.text:
                    elem.text = elem.text.format(b1=bounds[0])
                elif '{b2}' in elem.text:
                    elem.text = elem.text.format(b2=bounds[0])
                    bounds.pop(0)
                elif '{p}' in elem.text:
                    elem.text = elem.text.format(p=points[0].decimal(2))
                    points.pop(0)
                else:
                    elem.text = elem.text.format(p1=b1, p2=b2)

    insert_answers(task, ans)


def problem8(task):
    sigma = random.randrange(1, 10)
    a = random.randrange(1, 10)
    s_p = 2 * sigma * sigma

    bounds = probability.rand_unique_table(2, 1, 10)

    f1 = str(round((bounds[1] - a) / sigma, 1)).replace('.', ',')
    f2 = str(round((bounds[0] - a) / sigma, 1)).replace('.', ',')

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(a=a, s=sigma, sp=s_p, b1=bounds[0], b2=bounds[1])

    for elem in task.ans.iter():
        if elem.text:
            elem.text = elem.text.format(b1=bounds[0], b2=bounds[1], f1=f1, f2=f2)


def problem9(task):
    k = random.randrange(2, 7)
    d_values = [6, 4, 3, 2]
    d = d_values[random.randrange(0, len(d_values))]
    while k % d == 0:
        d = d_values[random.randrange(0, len(d_values))]
    ans = [Frac(k, math.sin(k * math.pi / d)).decimal(1), 'π', d, ('π', k)]

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(k=k, d=d)

    insert_answers(task, ans)


def problem10(task):
    x = probability.rand_unique_table(3, -4, 9)
    p = probability.rand_prob_table(3, 2)[0]

    m = Frac(0)
    for i in range(0, 3):
        m += Frac(x[i]) * p[i]

    ans = [m,
           probability.rand_prob(2) + Frac(1),
           probability.rand_prob(2) + Frac(2),
           probability.rand_prob(2) + Frac(3)]

    insert_answers(task, ans)

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                if elem.text == '{x}':
                    elem.text = f'{x[0]}'
                    x.pop(0)
                elif elem.text == '{p}':
                    elem.text = f'{p[0].decimal(2)}'
                    p.pop(0)


def problem11(task):
    x = probability.rand_unique_table(2, -4, 9)
    p = probability.rand_prob_table(2, 2)[0]

    m = Frac(0)
    for i in range(0, 2):
        m += Frac(x[i]) * p[i]

    d = Frac(0)
    for i in range(0, 2):
        d += Frac(x[i]) * Frac(x[i]) * p[i]

    ans = [d - m * m,
           probability.rand_prob(2) + Frac(1),
           probability.rand_prob(2) + Frac(2),
           probability.rand_prob(2) + Frac(3)]

    insert_answers(task, ans)

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                if elem.text == '{x}':
                    elem.text = f'{x[0]}'
                    x.pop(0)
                elif elem.text == '{p}':
                    elem.text = f'{p[0].decimal(2)}'
                    p.pop(0)


def problem12(task):
    p = probability.rand_prob(2)
    q = Frac(1) - p
    n = Frac(100)
    m = p * n
    d = p * n * q
    m_w = p * p * n

    ans = [(m, d),
           (d, m),
           (m_w, d),
           (d, m_w)]

    for node in task.nodes:
        for elem in node.iter():
            if elem.text:
                elem.text = elem.text.format(p=p.decimal(2))

    for elem in task.ans.iter():
        if elem.text:
            old = elem.text
            if len(ans) > 0:
                elem.text = elem.text.format(m=ans[0][0].decimal(2), d=ans[0][1].decimal(2))
            if old != elem.text:
                ans.pop(0)


solutions = [Solution(1, problem1),
             Solution(2, problem2),
             Solution(3, problem3),
             Solution(4, problem4),
             Solution(5, problem5),
             Solution(6, problem6),
             Solution(7, problem7),
             Solution(8, problem8),
             Solution(9, problem9),
             Solution(10, problem10),
             Solution(11, problem11),
             Solution(12, problem12)]
