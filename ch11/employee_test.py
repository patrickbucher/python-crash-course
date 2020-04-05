import unittest

from employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('John', 'Doe', 100000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(105000, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(110000, self.employee.salary)


if __name__ == '__main__':
    unittest.main()
