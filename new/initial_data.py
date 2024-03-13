import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new.settings")
django.setup()

# from django.contrib.auth.models import User
from testapi.models import *

# Clear existing data
User.objects.all().delete()
Users.objects.all().delete()
Assessments.objects.all().delete()
Questions.objects.all().delete()

user1 = User.objects.create(username='john', password='password', first_name='John', last_name='Doe')
# user2 = User.objects.create(username='shoshanna', password='password', first_name='Shoshanna', last_name='Kalinke')
# user3 = User.objects.create(username='alfie', password='password', first_name='Alfie', last_name='Balazs')

# Insert data into Users table
Users.objects.bulk_create([
    Users(user=user1, age=30, gender='Male')
    # Users(user_id=2, age=28, gender='Female'),
    # Users(user_id=3, age=30, gender='Female')
])

# Insert data into Assessments table
Assessments.objects.bulk_create([
    Assessments(assessment_id=1, assessment_title='ADHD', scale=5, num_questions=8),
    Assessments(assessment_id=2, assessment_title='Generalized Anxiety Disorder', scale=4, num_questions=7),
    Assessments(assessment_id=3, assessment_title='Depression', scale=4, num_questions=9)
])

# Insert data into Questions table
Questions.objects.bulk_create([
    Questions(assessment_id=1, question_id=1, question='How often do you have difficulty getting things in order when you have to do a task that requires organization?'), 
    Questions(assessment_id=1, question_id=2, question='How often do you have problems remembering appointments or obligations?'), 
    Questions(assessment_id=1, question_id=3, question='When you have a task that requires a lot of thought, how often do you avoid or delay getting started?'), 
    Questions(assessment_id=1, question_id=4, question='How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?'), 
    Questions(assessment_id=1, question_id=5, question='How often do you feel overly active and compelled to do things, like you were driven by a motor?'), 
    Questions(assessment_id=1, question_id=6, question='How often do you make careless mistakes when you have to work on a boring or difficult project?'), 
    Questions(assessment_id=1, question_id=7, question='How often do you have difficulty keeping your attention when you are doing boring or repetitive work?'),
    Questions(assessment_id=1, question_id=8, question='How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?'), 
    Questions(assessment_id=2, question_id=9, question='Feeling nervous, anxious or on edge'), 
    Questions(assessment_id=2, question_id=10, question='Feeling down, depressed, or hopeless'), 
    Questions(assessment_id=2, question_id=11, question='Trouble falling or staying asleep, or sleeping too much'), 
    Questions(assessment_id=2, question_id=12, question='Feeling tired or having little energy'), 
    Questions(assessment_id=2, question_id=13, question='Being so restless that it is hard to sit still'),
    Questions(assessment_id=2, question_id=14, question='Becoming easily annoyed or irritable'),
    Questions(assessment_id=2, question_id=15, question='Feeling afraid as if something awful might happen '),
    Questions(assessment_id=3, question_id=16, question='Little interest or pleasure in doing things'),
    Questions(assessment_id=3, question_id=17, question='Feeling down, depressed, or hopeless'),
    Questions(assessment_id=3, question_id=18, question='Trouble falling or staying asleep, or sleeping too much'),
    Questions(assessment_id=3, question_id=19, question='Feeling tired or having little energy'),
    Questions(assessment_id=3, question_id=20, question='Poor appetite or overeating'),
    Questions(assessment_id=3, question_id=21, question='Feeling bad about yourself or that you are a failure or have let yourself or your family down'),
    Questions(assessment_id=3, question_id=22, question='Trouble concentrating on things, such as reading the newspaper or watching television'),
    Questions(assessment_id=3, question_id=23, question='Moving or speaking so slowly that other people could have noticed. Or the opposite being so fidgety or restless that you have been moving around a lot more than usual'),
    Questions(assessment_id=3, question_id=24, question='Thoughts that you would be better off dead, or of hurting yourself')
])