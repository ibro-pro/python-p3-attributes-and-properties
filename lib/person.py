# lib/person.py

approved_jobs = [
    "Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal",
    "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Admin"):
        self.name = name   # use the property
        self.job = job     # use the property

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
