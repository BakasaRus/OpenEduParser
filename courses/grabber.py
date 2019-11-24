import requests
import re
import json
from .models import *


class Grabber:
    courses = dict()
    organizers = dict()
    groups = dict()

    def get_texts(self):
        text = requests.get('https://openedu.ru/course/').text
        courses_text = re.search('COURSES = ({.*});', text).group(1)
        universities_text = re.search('UNIVERSITIES = ({.*});', text).group(1)
        groups_text = re.search('GROUPS = ({.*});', text).group(1)

        self.courses = json.loads(courses_text)
        self.organizers = json.loads(universities_text)
        self.groups = json.loads(groups_text)

    def save_courses(self):
        for ident, course in self.courses.items():
            course_trans = Course(
                id=ident,
                name=course['title'],
                url=course['url'],
                organizer=Organizer.objects.get(id=int(course['uni']))
            )
            course_trans.save()
            course['groups'] = [int(x) for x in course['groups']]
            course_trans.groups.set(Group.objects.filter(id__in=course['groups']))

    def save_organizers(self):
        for ident, organizer in self.organizers.items():
            organizer_trans = Organizer(
                id=ident,
                name=organizer['abbr'],
                url=organizer['url'],
                logo=organizer['icon']
            )
            organizer_trans.save()

    def save_groups(self):
        for ident, group in self.groups.items():
            group_trans = Group(
                id=ident,
                name=group['title'],
                code=group['code']
            )
            group_trans.save()
