import unittest

from student import Student

class Student_Test(unittest.TestCase):
    def test_init(self):
        student = Student(4.0, 'Clarissa')
        self.assertEqual(student.gpa, 4.0, msg='The GPA should be 4.0')
        self.assertEqual(student.name, 'Clarissa')

    def test_set_mark(self):
        student = Student(4.0, 'Clarissa')
        self.assertEqual(student.marks, [])
        student.set_mark('CSCI1030U', 80.0)
        self.assertEqual(student.marks, [80.0])
        student.set_mark('CSCI1060U', 90.0)
        self.assertEqual(student.marks, [80.0, 90.0])

    def test_get_average(self):
        student = Student(4.0, 'Clarissa')
        student.set_mark('CSCI1030U', 80.0)
        student.set_mark('CSCI1060U', 90.0)
        self.assertAlmostEqual(student.get_average(), 85.0, places=2)

        self.assertRaises

unittest.main()