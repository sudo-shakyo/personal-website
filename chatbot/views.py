from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from chatbot.models import Query, ConsumerHelpDatabase

import spacy
nlp = spacy.load('en_core_web_sm')

from chatbot.models import ConsumerHelpDatabase

data = [
    ('How do I reset my password?', 'You can reset your password by going to the account settings page.'),
    ('How do I cancel my subscription?', 'To cancel your subscription, go to the subscription page and click on the cancel button.'),
    ('What payment methods do you accept?', 'We accept credit cards, PayPal, and Apple Pay.'),
    ('How do I contact customer support?', 'You can contact customer support by emailing support@example.com or calling our toll-free number.'),
    ('What payment methods do you accept?', 'We accept various payment methods, including credit cards, PayPal, and Apple Pay. Please see our website for more details.'),
    (' How do I create an account?','You can create an account by clicking the "Sign Up" button on our website and following the prompts.'),
    (' How do I update my account information?', 'You can update your account information by logging in to your account and going to the "Account Settings" page.'),
    (' What is a syntax error?','A syntax error is a mistake in the code that violates the programming language’s syntax rules.'),
    (' What is a runtime error?','A runtime error occurs when the code is syntactically correct but causes an error during execution.'),
    ('What is a logic error?', 'A logic error is a mistake in the code’s logic that causes it to produce incorrect or unexpected results.'),
    ('How do I debug my code?', 'You can use a debugger, print statements, or logging statements to help you find and fix errors in your code.'),
    ('What is a traceback?', ' A traceback is a list of functions that were called before an error occurred, along with the line number where the error occurred.'),
    ('What is a NameError?', 'A NameError occurs when a variable or function is referenced before it has been defined.'),
    ('What is a TypeError?','A TypeError occurs when an operation or function is applied to an object of an inappropriate type.'),
    ('What is a ValueError?','A ValueError occurs when a function or operation receives an argument of the correct type but an inappropriate value.'),
    ('How do I handle exceptions?','You can use a try-except block to handle exceptions in your code.'),
    (' What is a module?','A module is a file containing Python code that can be used by other programs.'),
    ('How do I import a module?','You can import a module using the "import" statement, followed by the name of the module.'),
    ('What is a namespace?','A namespace is a mapping from names to objects, used to avoid naming conflicts and to organize code.'),
    ('What is a package?','A package is a collection of modules and other packages that can be used together.'),
    ('How do I create a package?','To create a package, create a directory with an "init.py" file and one or more Python module files.'),
    ('What is a virtual environment?','A virtual environment is an isolated Python environment that allows you to install packages and dependencies for a specific project without affecting other projects or the system Python installation.'),
    ('How do I create a virtual environment?','You can create a virtual environment using the "venv" module or a third-party tool like "conda" or "virtualenv".'),
    ('How do I activate a virtual environment?','To activate a virtual environment, run the "activate" script in the virtual environment’s "Scripts" directory.'),
    (' How do I install packages in a virtual environment?','To install packages in a virtual environment, activate the environment and use the "pip" command to install the packages.'),
    ('What is a dependency?','A dependency is a package or library that is required by another package or program to function correctly.'),
    ('How do I manage dependencies for my project?','You can manage dependencies for your project using a package manager like "pip" or "conda". You can specify the required dependencies in a "requirements.txt" file or a "environment.yml" file, which can be used to install the required packages.'),
    ('hello','hey there! welcome to CodeItWithShakyo'),
    ('hi','hey there! welcome to CodeItWithShakyo'),
    ('yo','hey there! welcome to CodeItWithShakyo'),
    ('How can your company help me improve my education?','Our company offers a range of online courses and educational resources designed to help you improve your skills and knowledge.'),
    ('Can I take courses at my own pace?','Yes, our courses are designed to be taken at your own pace, so you can study whenever and wherever it\'s convenient for you.'),
    ('What types of courses do you offer?','We offer coding courses of various languages like Python, C++, JavaScript and many more'),
    ('How do I sign up for a course?','You can sign up for a course on our website or through our YouTube Channel.'),
    ('Do you offer any support or guidance during the course?','Yes, we have a team of dedicated instructors and support staff who are available to answer any questions you may have.'),
    ('What types of assessments do you use to evaluate student progress?','We use a variety of assessments, including quizzes, exams, and assignments, to evaluate student progress.'),
    ('Can I get feedback on my performance?','Yes, our instructors provide regular feedback on student performance throughout the course.'),
    ('How do I contact customer support?','You can contact customer support through our website.'),
    ('Can I provide feedback on a course?','Yes, we welcome feedback from students on our courses.'),
    ('How do you ensure the quality of your courses?','We have a team of experienced instructors and subject matter experts who develop and review our courses to ensure their quality.'),
    ('Can I access your courses from anywhere in the world?','Yes, our courses are available to students from anywhere in the world, as long as they have an internet connection.'),
    ('How do I know if a course is right for my skill level?','Our courses are designed for students of all levels, and we provide detailed course descriptions and prerequisites to help you determine if a course is right for you. Additionally, our team can help you assess your skills and find the course that best fits your needs.'),
    ('How do I know if a course is up-to-date and relevant?','We regularly review and update our courses to ensure they are up-to-date and relevant to today\'s job market. We also work with industry experts to ensure our courses are aligned with current trends and best practices.'),
    ('Are your courses self-paced or instructor-led?','We offer both self-paced and instructor-led courses, depending on the course and subject.'),
    ('How long does it take to complete a course?','The length of time it takes to complete a course varies depending on the course and your individual pace. We provide estimated completion times for each course, but you are free to take as long as you need to complete the course.'),
    ('Are there any prerequisites for your courses?','Some of our courses have prerequisites, which are listed on the course description page. If you\'re unsure whether you meet the prerequisites for a course, our team can help you determine your eligibility.'),
    ('Are your courses interactive?','Yes, our courses are designed to be interactive and engaging, with a mix of videos, quizzes, and assignments to keep you motivated and on track.'),
    ('How do I know if I\'m ready to take an advanced course?','Our team can help you assess your readiness for an advanced course based on your skills and experience.'),
    ('What types of courses do you offer?','We offer a wide range of courses in areas such as coding, data science, design, business, and more.'),
    ('Do you offer any free courses?','Yes, we offer a variety of free courses on our website.'),
    ('Can I take multiple courses at the same time?','Yes, you can take multiple courses at the same time, but we recommend assessing your workload and availability before doing so.'),
    ('Can I get feedback on my assignments?','Yes, our instructors provide feedback on assignments to help you improve your skills.'),
    ('Can I provide feedback on a course?','Yes, we welcome feedback from students to help improve our courses and services. You can provide feedback through our website or by contacting our customer support team.'),
    
]

for query, response in data:
    ConsumerHelpDatabase.objects.create(query=query, response=response)


def chatbot(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        response = 'Sorry, I did not understand your query.'

        # use spaCy's NER to extract entities from the query
        entities = []
        doc = nlp(query)
        for ent in doc.ents:
            entities.append((ent.label_, ent.text))

        # search for a matching query using spaCy and extracted entities
        matches = []
        for row in ConsumerHelpDatabase.objects.all():
            similarity = nlp(query).similarity(nlp(row.query))
            for entity in entities:
                if entity[1] in row.query:
                    similarity += 0.1
            matches.append((row.response, similarity))

        matches.sort(key=lambda x: x[1], reverse=True)
        if matches and matches[0][1] > 0.5:
            response = matches[0][0]

        # save the query and response
        Query.objects.create(text=query, response=response)

        # return the response
        return JsonResponse({'response': response})

    return render(request, 'chatbot.html')
