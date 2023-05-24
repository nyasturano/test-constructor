import random

from docx.shared import Pt
import utils
from solution import solve


class Task:
    def __init__(self, t_id, solution=False):
        self.id = int(t_id)  # !!!!
        self.nodes = []
        self.img = []
        self.ans = None
        self.right = -1
        self.solution = solution

    def add_node(self, node):
        self.nodes.append(node)
        if utils.contains_table(node.getnext()):
            self.add_node(node.getnext())
        if utils.contains_picture(node):
            self.img.append(len(self.nodes) - 1)

    def compile(self, document):
        # delete empty paragraphs after answers' table and extract table from nodes
        while not utils.contains_table(self.nodes[-1]):
            self.nodes[-1].getparent().remove(self.nodes[-1])
            self.nodes.pop(-1)
        self.ans = self.nodes[-1]
        self.nodes.pop(-1)

        # if task has a solution (if it needs to be filled with random values), run this solution
        if self.solution:
            solve(self)

        # get all <w:tc> elements (all table cells) and rows count
        ans_c = []
        rows = 0
        for elem in self.ans.iter():
            if elem.tag.endswith('tr'):
                rows += 1
            if elem.tag.endswith('tc'):
                ans_c.append(elem)
                # print(elem.xml)

        # save right answer so we won't lose it
        right = ans_c[0]

        # randomly reorder cells
        random.shuffle(ans_c)

        # set custom inline numeration by columns
        for i, elem in enumerate(ans_c):
            p = document.add_paragraph()
            run = p.add_run(f'{i + 1}) ')
            run.font.name = 'Times New Roman'
            run.font.size = Pt(11)
            elem.getchildren()[1].insert(1, run._element)
            p_elem = p._element
            p_elem.getparent().remove(p_elem)
            p_elem._p = p_elem._element = None

        # find the right answer and set its index
        self.right = -1
        for i in range(0, len(ans_c)):
            if ans_c[i] == right:
                self.right = i

        cols = 4 // rows

        # append reordered cells again. as a result, cells will be moved in a new order
        for i in range(0, cols):
            for elem in self.ans.iter():
                if elem.tag.endswith('tr'):
                    elem.append(ans_c[0])
                    ans_c.pop(0)
