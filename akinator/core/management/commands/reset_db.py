import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Entity, Question, AnswersDistribution


BOOKS_FILE = os.path.join(settings.PROJECT_ROOT, 'core', 'fixtures', 'Books.csv')
QUESTIONS_FILE = os.path.join(settings.PROJECT_ROOT, 'core', 'fixtures', 'Questions.csv')
DISTRIBUTION_FILE = os.path.join(settings.PROJECT_ROOT, 'core', 'fixtures', 'Distribution.csv')


class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'Reset db started.'

        Entity.objects.all().delete()
        Question.objects.all().delete()
        print 'db clear done.'

        print 'Loading books...'
        books_list = {}
        with open(BOOKS_FILE, 'r') as f:
            b_reader = csv.DictReader(f, delimiter=',')
            for book in b_reader:
                pk = int(book['id_b'])
                name = book['name'].decode('utf8')
                description = ''

                db_book = Entity(name=name, description=description)
                db_book.save()

                books_list[pk] = db_book

        print 'Done.'

        print 'Loading questions...'
        questions_list = {}
        with open(QUESTIONS_FILE, 'rb') as f:
            q_reader = csv.DictReader(f, delimiter=',')
            for question in q_reader:
                pk = int(question['id_q'])
                text = question['question'].decode('utf8')

                db_question = Question(text=text)
                db_question.save()

                questions_list[pk] = db_question

        print 'Done.'

        print 'Loading distributions...'
        with open(DISTRIBUTION_FILE, 'rb') as f:
            d_reader = csv.DictReader(f, delimiter=',')
            for distribution in d_reader:
                book_id = int(distribution['id_b'])
                question_id = int(distribution['id_q'])

                yes_count = int(float(distribution['yes'].replace(',', '.')) * 100)
                no_count = int(float(distribution['no'].replace(',', '.')) * 100)
                dm_count = int(float(distribution['does not matter'].replace(',', '.')) * 100)

                book = books_list[book_id]
                question = questions_list[question_id]

                db_distribution = AnswersDistribution(entity=book, question=question, yes_count=yes_count, no_count=no_count, dm_count=dm_count)
                db_distribution.save()

        print 'Done.'
