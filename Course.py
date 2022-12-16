import unittest

from src.course import Course
from src.teacher import Teacher


class CourseTest(unittest.TestCase):
    __default_teacher = Teacher('Kristina Savchuk')
    __default_course = Course('Intro to python', __default_teacher)

    def test_constructor(self):
        self.assertEqual('Intro to python', self.__default_course.name)
        self.assertEqual(self.__default_teacher, self.__default_course.teacher)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            self.__default_course.name = 1234
        with self.assertRaises(ValueError):
            self.__default_course.name = ''

    def test_teacher_validation(self):
        with self.assertRaises(TypeError):
            self.__default_course.teacher = 'Kristina Savchuk but a string'

    def test_add_topic(self):
        course = Course('Intro to python', self.__default_teacher)
        self.assertEqual(0, len(course.topics))
        with self.assertRaises(TypeError):
            course.add_topic(1234)
        with self.assertRaises(ValueError):
            course.add_topic('')

        course.add_topic('What is JVM')
        course.add_topic('python')
        course.add_topic('Intro to Maven')

        self.assertEqual(3, len(course.topics))
        self.assertEqual('What is JVM', course.topics[0])
        self.assertEqual('python', course.topics[1])
        self.assertEqual('Intro to Maven', course.topics[2])

    def test_str(self):
        course = Course('Intro to python', self.__default_teacher)
        course.add_topic('What is JVM')
        self.assertEqual(
            'Course: Name=Intro to python; Teacher=Teacher: Name=Kristina Savchuk; Topics=[\'What is JVM\']',
            str(course)
        )


if __name__ == '__main__':
    unittest.main()