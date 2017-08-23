from person import Person


class Student(Person):
    '''

    Student class
    '''

    # def __init__(self):
    #     print('Self', self, id(self))
    #     self.name = 'Bill'
    #     self.age = 22
    NUMBER_OF_TASKS = 37
    NUMBER_OF_TESTS = 12
    TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]

    def __init__(self, name, age=18):
        super().__init__(name, age)
        # print('Self', self, id(self)) replaced by upper line
        # self.name = name
        # self.age = age
        self.hw_results = [0]*Student.NUMBER_OF_TASKS
        self.test_results = [0]*Student.NUMBER_OF_TESTS
        self._total_rank_dirty = True
        self._total_rank = 0


    # def print_info(self):
    #     super().print_info()
    #     # print('_______________________') replaced by upper line
    #     # print('Name:', self.name)
    #     # print('Age:', self.age)
    #     print('H/w results:', self.hw_results)
    #     print('Test results:', self.test_results)
    #     print('Total rank:', self.total_rank())
    #     print('_______________________')


    def print_info_ext(self):
        print('H/w results:', self.hw_results)
        print('Test results:', self.test_results)
        print('Total rank:', self.total_rank())


    def accepted_task(self, *number_of_tasks):
        self._total_rank_dirty = True
        for task_number in number_of_tasks:
            self.hw_results[task_number-1] = 1

    def accepted_test(self, *number_of_tests):
        self._total_rank_dirty = True
        for test_number in number_of_tests:
            self.test_results[test_number-1] = 1

    def total_rank(self):
        if self._total_rank_dirty:
            total_rank = sum(self.hw_results)
            for i in range(Student.NUMBER_OF_TESTS):
                total_rank += self.test_results[i] * Student.TEST_WEIGHTS[i]
            self._total_rank = total_rank
            self._total_rank_dirty = False
        return self._total_rank

    def __str__(self):
        return  '%s: name=%s, age=%s' % \
                (self.__class__.__name__, self.name, self.age)