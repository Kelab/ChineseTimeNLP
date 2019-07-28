class TimePoint:
    '''
    时间表达式单元规范化对应的内部类,对应时间表达式规范化的每个字段。\n
    六个字段分别是：年-月-日-时-分-秒 \n
    每个字段初始化为-1
    '''
    def __init__(self):
        self.tunit = [-1, -1, -1, -1, -1, -1]

    def __repr__(self):
        return str(self.tunit)
