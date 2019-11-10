from collections import deque
from typing import List


class ACNode:
    def __init__(self, data: str):
        self.data = data
        self.children = [None] * 26  # 字符集只包含 a~z 这 26 个字符
        self.is_ending_char = False  # 结尾字符为 true
        self.length = -1  # 当 isEndingChar=true 时，记录模式串长度
        self.fail = None  # 失败指针


class ACAutomata:
    def __init__(self):
        self.root = ACNode("/")

    def insert(self, text: str) -> None:
        node = self.root
        for index, char in map(lambda x: (ord(x) - ord("a"), x), text):
            if node.children[index] is None:
                node.children[index] = ACNode(char)
            node = node.children[index]
        node.is_ending_char = True
        node.length = len(text)

    def insert_list(self, patterns: List[str]) -> None:
        for pattern in patterns:
            self.insert(pattern)
        self.build_failure_pointer()

    def build_failure_pointer(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            p: ACNode = queue.popleft()
            for pc in p.children:
                if pc is None:
                    continue
                if p == self.root:
                    pc.fail = self.root
                else:
                    q = p.fail
                    while q:
                        qc = q.children[ord(pc.data) - ord("a")]
                        if qc:
                            pc.fail = qc
                            break
                        q = q.fail
                    if q is None:
                        pc.fail = self.root
                queue.append(pc)

    def match(self, text: str) -> list:
        """返回该字符串所有匹配的起始角标和字符串长度"""
        result = []
        p = self.root
        for i, char in enumerate(text):
            idx = ord(char) - ord("a")
            while p.children[idx] is None and p != self.root:
                p = p.fail
            p = p.children[idx]
            if p is None: p = self.root
            tmp = p
            while tmp != self.root:
                if tmp.is_ending_char:
                    # print(f"匹配起始下标{i - tmp.length + 1}，长度{tmp.length}")
                    result.append((i - tmp.length + 1, tmp.length))
                tmp = tmp.fail
        return result

    def sensitive_word_filtered(self, text: str) -> str:
        filter_range_list = self.match(text)
        str_list = list(text)
        for start, length in filter_range_list:
            for i in range(start, start + length):
                str_list[i] = "*"
        return "".join(str_list)

if __name__ == "__main__":
    patterns = ["at", "art", "oars", "soar"]
    ac = ACAutomata()
    ac.insert_list(patterns)

    ac.match("soarsoarts")
