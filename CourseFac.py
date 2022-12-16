import unittest

from src.course_factory import CourseFactory


class CourseFactoryTest(unittest.TestCase):
    __factory = CourseFactory()

    def test_create_teacher(self):
        teacher = self.__factory.create_teacher('Travis Scott')
        self.assertEqual('Travis Scott', teacher.name)

    def test_create_local_course(self):
        teacher = self.__factory.create_teacher('Travis Scott')
        local_course = self.__factory.create_local_course('lab_name', 'course_name', teacher)
        self.assertEqual(teacher, local_course.teacher)
        self.assertEqual('lab_name', local_course.lab)
        self.assertEqual('course_name', local_course.name)

    def test_create_offsite_course(self):
        teacher = self.__factory.create_teacher('Oleksii Lozoviahin')
        offsite_course = self.__factory.create_offsite_course('Kyiv', 'How to download a GPU', teacher)
        self.assertEqual(teacher, offsite_course.teacher)
        self.assertEqual('Kyiv', offsite_course.town)
        self.assertEqual('How to download a GPU', offsite_course.name)


if __name__ == '__main__':
    unittest.main()

