import unittest
from students import Student
from datetime import date, timedelta



class TestStudent(unittest.TestCase):
    """Test class for Students"""

    # we use the setUp class to set up an instace of the student class and use for all tests

    def setUp(self):
        self.student = Student('Ayrton', 'Dabronzo')

    def test_full_name(self):
        """to test a class we need to do a instance of that class"""
        # student = Student("Ayrton", "Dabronzo")

        self.assertEqual(self.student.full_name, 'Ayrton Dabronzo')

    def test_alert_santa(self):
        """ test for the function to change the naughty list"""
        # student = Student('Ayrton', 'Dabronzo')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_student_email(self):
        """Student email test"""
        # student = Student('Ayrton', 'Dabronzo')

        self.assertEqual(self.student.student_email, 'ayrton.dabronzo@email.com')

    def test_apply_extension(self):
        """Test for the extension on the end_date"""
        self.student.apply_extension(180)
        self.assertEqual(self.student.end_date, self.student._start_date - timedelta(180))





if __name__ == '__main__':
    unittest.main()