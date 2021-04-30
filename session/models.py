from django.db import models
from django.contrib.auth.models import User

from student.models import Student

SESSION_TYPES = [('intro', "Intro"), ('inception', "Project inception"),
                 ('middle', "Middle of project"), ('end', "End of project"),
                 ('prep', "Interview preparation and career advice"),
                 ('postponed', "Postponed (Valid Reason)"), ('other', "Other"),
                 ('no-show', "**No-show**")]

SESSION_FEELINGS = [('excellent', "Excellent - It's going great."),
                    ('average',
                     "Average - The student is moving at an acceptable pace."),
                    ('poor', "I'm worried about this student's progress.")]

PROJECTS = [('intro', 'Intro/Interview'),
            ('userCentric', 'User Centric Front End Development (MS1)'),
            ('interactive', 'Interactive Front End Development (MS2)'),
            ('dataCentric', 'Data Centric Development (MS3)'),
            ('fullStack', 'Full Stack Frameworks with Django (MS4)'),
            ('pp1', 'HTML/CSS Essentials (PP1)'),
            ('pp2', 'JavaScript Essentials (PP2)'),
            ('pp3', 'Python Essentials (PP3)'),
            ('pp4', 'Full Stack Toolkit (PP4)'),
            ('eCommerce', 'eCommerce (PP5)')]


class SessionLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    mentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, default="")
    concern = models.TextField(max_length=500, default="", null=True)
    date = models.DateField(blank=False)
    types = models.CharField(max_length=255,
                             blank=False,
                             choices=SESSION_TYPES)
    projects = models.CharField(max_length=255,
                                blank=False,
                                default='["other"]')
    duration = models.CharField(max_length=255, blank=False)
    feeling = models.TextField(blank=False, choices=SESSION_FEELINGS)

    @property
    def duration_in_mins(self):
        hours, mins, seconds = map(int, self.duration.split('-'))
        return round(hours * 60 + mins + seconds / 60, 2)

    def __str__(self):
        return "Log: {} -> {}".format(self.id, self.date)
