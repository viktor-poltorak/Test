from celery import shared_task
from faker import Faker
import random
import logging

logger = logging.getLogger(__name__)

from app.models import Question, Choice


@shared_task
def create_question():
    Faker.seed(0)
    faker = Faker()
    logger.info("Creating question")
    question = Question.objects.create(
        text=faker.text(max_nb_chars=50)
    )

    choices_number = random.randint(1, 10)

    for i in range(choices_number):
        Choice.objects.create(
            question=question,
            text=faker.text(max_nb_chars=50)
        )

    logger.info(f"Question with {choices_number} choices created successfully")

