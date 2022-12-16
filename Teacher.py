import unittest

from src.teacher import Teacher


class TeacherTest(unittest.TestCase):

    def test_constructor(self):
        teacher = Teacher('Travis Scott')
        self.assertEqual('Travis Scott', teacher.name)

    def test_name_validation(self):
        teacher = Teacher('Travis Scott')
        with self.assertRaises(TypeError):
            teacher.name = 1234
        with self.assertRaises(ValueError):
            teacher.name = ''

    def test_str(self):
        teacher = Teacher('Travis Scott')
        self.assertEqual('Teacher: Name=Travis Scott', str(teacher))


if __name__ == '__main__':
    unittest.main()