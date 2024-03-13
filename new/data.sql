TRUNCATE TABLE Assessments CASCADE;
TRUNCATE TABLE Questions CASCADE;
TRUNCATE TABLE Responses CASCADE;
TRUNCATE TABLE UserStats CASCADE;
TRUNCATE TABLE Users CASCADE;

INSERT INTO Users(user_id, firstname, lastname, age, gender, birthdate) VALUES
  (1, 'John','Doe',30,'Male','1990-05-15'), 
  (2, 'Shoshanna','Kalinke',28,'Female','1994-3-30'), 
  (3, 'Alfie','Balazs',30,'Female','1976-07-12');

INSERT INTO Assessments(assessment_id, assessment_title, scale, num_questions) VALUES
  (1, 'ADHD', 5, 8),
  (2, 'Generalized Anxiety Disorder', 4, 7),
  (3, 'Depression', 4, 9);

INSERT INTO Questions (assessment_id, question_id, question) VALUES
  (1, 1, 'How often do you have difficulty getting things in order when you have to do a task that requires organization?'), 
  (1, 2, 'How often do you have problems remembering appointments or obligations?'), 
  (1, 3, 'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?'), 
  (1, 4, 'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?'), 
  (1, 5, 'How often do you feel overly active and compelled to do things, like you were driven by a motor?'), 
  (1, 6, 'How often do you make careless mistakes when you have to work on a boring or difficult project?'), 
  (1, 7, 'How often do you have difficulty keeping your attention when you are doing boring or repetitive work?'),
  (1, 8, 'How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?'), 
  (2, 9, 'Feeling nervous, anxious or on edge'), 
  (2, 10, 'Feeling down, depressed, or hopeless'), 
  (2, 11, ' Trouble falling or staying asleep, or sleeping too much'), 
  (2, 12, 'Feeling tired or having little energy'), 
  (2, 13, 'Being so restless that it is hard to sit still'),
  (2, 14, 'Becoming easily annoyed or irritable'),
  (2, 15, 'Feeling afraid as if something awful might happen '),
  (3, 16, 'Little interest or pleasure in doing things'),
  (3, 17, 'Feeling down, depressed, or hopeless'),
  (3, 18, 'Trouble falling or staying asleep, or sleeping too much'),
  (3, 19, 'Feeling tired or having little energy'),
  (3, 20, 'Poor appetite or overeating'),
  (3, 21, 'Feeling bad about yourself or that you are a failure or have let yourself or your family down'),
  (3, 22, 'Trouble concentrating on things, such as reading the newspaper or watching television'),
  (3, 23, 'Moving or speaking so slowly that other people could have noticed. Or the opposite being so fidgety or restless that you have been moving around a lot more than usual'),
  (3, 24, 'Thoughts that you would be better off dead, or of hurting yourself');