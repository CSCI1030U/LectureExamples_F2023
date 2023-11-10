import unittest
from student import Student

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(4.0, 'Clarissa')
        self.assertEqual(clarissa.gpa, 4.0, msg='The GPA should be 4.0')
        self.assertEqual(clarissa.name, 'Clarissa')
        self.assertEqual(clarissa.marks, [])

    def test_set_mark(self):
        clarissa = Student(4.0, 'Clarissa')
        self.assertEqual(clarissa.marks, [])
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertEqual(clarissa.marks, [70.0])
        clarissa.set_mark('CSCI1060U', 80.0)
        self.assertEqual(clarissa.marks, [70.0, 80.0])

    def test_get_average(self):
        clarissa = Student(4.0, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 70.0)
        clarissa.set_mark('CSCI1060U', 80.0)
        self.assertAlmostEqual(clarissa.get_average(), 75.0, places=2)

unittest.main()
