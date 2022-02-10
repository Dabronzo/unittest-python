from datetime import date, timedelta
import requests

class Student:
    """A student class for method testign"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def student_email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        self.naughty_list = True

    
    def apply_extension(self, days):
        self.end_date = self._start_date - timedelta(days=days)

    #here is a function that simulate as request of an API
    # the function may return the request or fail if the api or
    # for some other reason the request was not completed

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._first_name}/{self._last_name}")

        if response.ok:
            return response.text
        else:
            return "An error ocurred when trying to get the schedule"



if __name__ == '__main__':
    student = Student('Ayrton', 'Dabronzo')
    print(student._start_date)


