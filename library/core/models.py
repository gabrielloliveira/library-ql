import uuid

from django.db import models


class DefaultModel(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    uuid = models.UUIDField("UUID", unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Book(DefaultModel):
    name = models.CharField("Nome do livro", max_length=500)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.name
