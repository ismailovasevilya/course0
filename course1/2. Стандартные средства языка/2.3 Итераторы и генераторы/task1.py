class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iteratable, *funcs, judge = judge_any):
        self.iteratable = iteratable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iteratable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(i):
                    pos += 1
                else:
                    neg += 1
                if self.judge(pos, neg):
                    yield i