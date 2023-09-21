from .models import Schedule, Choice


class ScheduleForm:
    question_text: str = None
    date_options: list = None

    def __init__(self, question_text, date_options):
        self.question_text = question_text
        self.date_options = date_options

    def is_valid(self):
        if self.question_text is None or self.question_text == '':
            return False

        if not isinstance(self.date_options, list) or len(self.date_options) == 0:
            return False

        return True


class ChoiceForm:
    question_id: str = None
    available_dates: dict = None
    submitter: str = None

    def __init__(self, question_id, available_dates, submitter):
        self.question_id = question_id
        self.available_dates = available_dates
        self.submitter = submitter

    def is_valid(self):
        if self.submitter is None or self.submitter == '':
            return False

        if self.question_id is None or self.question_id == '':
            return False

        schedule = Schedule.objects.get(id=self.question_id)
        if set(schedule.date_options) != set(self.available_dates.keys()):
            return False

        for key, value in self.available_dates.items():
            if not Choice.Options.is_valid(value):
                return False

        return True
