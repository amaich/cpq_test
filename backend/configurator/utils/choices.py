from django.db import models

class Operation(models.TextChoices):
    INCLUDE = "INCLUDE", "Включает"
    EXCLUDE = "EXCLUDE", "Исключает"
    RECOMMEND = "RECOMMEND", "Рекомендует"


class Operator(models.TextChoices):
    AND = "AND", "И"
    OR = "OR", "ИЛИ"