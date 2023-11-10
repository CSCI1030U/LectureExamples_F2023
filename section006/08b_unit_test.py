import unittest
from student import Student


class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(4.0, 'Clarissa')
        self.assertEqual(clarissa.gpa, 4.0, msg='GPA should be 4.0')
        self.assertEqual(clarissa.name, 'Clarissa', msg='name should be Clarissa')
        self.assertEqual(clarissa.marks, [], 'Marks should be an empty list')

    def test_set_mark(self):
        clarissa = Student(4.0, 'Clarissa')
        self.assertEqual(clarissa.marks, [])
        clarissa.set_mark('CSCI1030U', 92.5)
        self.assertEqual(clarissa.marks, [92.5])
        clarissa.set_mark('CSCI1060U', 87.0)
        self.assertEqual(clarissa.marks, [92.5, 87.0])

    def test_get_average(self):
        clarissa = Student(4.0, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 90.0)
        clarissa.set_mark('CSCI1060U', 80.0)
        self.assertAlmostEquals(clarissa.get_average(), 85.0, places=2)
        

unittest.main()