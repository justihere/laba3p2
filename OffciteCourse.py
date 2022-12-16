import unittest

from src.offsite_course import OffsiteCourse
from src.teacher import Teacher


class OffsiteCourseTest(unittest.TestCase):
    def test_town_validation(self):
        teacher = Teacher('Travis Scott')
        course = OffsiteCourse('town name', 'course name', teacher)
        with self.assertRaises(TypeError):
            course.town = 12345
        with self.assertRaises(ValueError):
            course.town = ''


if __name__ == '__main__':
    unittest.main()