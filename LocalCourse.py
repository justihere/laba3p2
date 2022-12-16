import unittest

from src.local_course import LocalCourse
from src.teacher import Teacher


class LocalCourseTest(unittest.TestCase):
    def test_lab_validation(self):
        teacher = Teacher('Travis Scott')
        course = LocalCourse('lab name', 'course name', teacher)
        with self.assertRaises(TypeError):
            course.lab = 12345
        with self.assertRaises(ValueError):
            course.lab = ''


if __name__ == '__main__':
    unittest.main()   