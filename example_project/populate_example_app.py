import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','example_project.settings')

import django
django.setup()

import random

from example_app.models import AccessRecord, Webpage, Topic, User

from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():

    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):

        # get the fake topic
        top = add_topic()

        # create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.free_email()

        # create the new user entry
        usr = User.objects.get_or_create(first_name = fake_first, last_name = fake_last, email = fake_email)[0]

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(N = 20)
    print('populating complete')
