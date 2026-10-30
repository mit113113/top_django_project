from django.db import models


class Product(models.Model):
    name = models.CharField(
        "Название",
        max_length=120
    )

    brand = models.CharField(
        "Бренд",
        max_length=80
    )

    description = models.TextField(
        "Описание",
        blank=True
    )

    price = models.DecimalField(
        "Цена, ₽",
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        "Изображение",
        upload_to='products/',
        blank=True
    )

    created_at = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.brand} — {self.name}"