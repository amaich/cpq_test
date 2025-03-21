from django.db import models
from .utils.choices import Operator, Operation

# Товар
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name='Бренд')
    manufacturer = models.CharField(max_length=255, blank=True, null=True, verbose_name='Производитель')
    is_custom = models.BooleanField(verbose_name="На пошив", default=True)

    def __str__(self):
        return f"Товар {self.name}"

# Изделие
class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='items',
                               blank=True, null=True, verbose_name='Родительская группа')
    uniq = models.BooleanField(default=False, verbose_name="Уникальная группа")
    required = models.BooleanField(default=False, verbose_name="Обязательно")
    min_count = models.IntegerField(default=1, verbose_name="Минимальное количество")
    max_count = models.IntegerField(default=1, verbose_name="Максимальное количество")

    def __str__(self):
        return f"Изделие {self.name} от {self.product.name}"


# Ресурс
class Resource(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="resources",
                             verbose_name='Изделие')

    def __str__(self):
        return f"Ресурс {self.item.name}"

# Набор признаков
class Attribute(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes",
                                verbose_name="Товар")
    attribute_for = models.ManyToManyField(Item, related_name='attributes',
                                           verbose_name="Признак для")
    operation = models.CharField(max_length=100, choices=Operation.choices, verbose_name="Операция")

    def __str__(self):
        return f"Признак {self.name} от {self.product.name}"

# Набор условий
class Condition(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="conditions",
                                verbose_name="Товар")
    condition_for = models.ManyToManyField(Item, related_name='conditions',
                                           verbose_name="Условие для")
    operation = models.CharField(max_length=100, choices=Operation.choices, verbose_name="Операция")
    operator = models.CharField(max_length=100, choices=Operator.choices, verbose_name="Оператор")

    def __str__(self):
        return f"Условие {self.name} от {self.product.name}"

class ConditionItem(models.Model):
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name="condition_items",
                                  verbose_name="Условие")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="condition_items",
                             verbose_name="Элемент")
    value = models.BooleanField(verbose_name="Значение")

    def __str__(self):
        return f"Элемент условия для {self.item}"
