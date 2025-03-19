from django.db import models


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
    min_count = models.IntegerField(verbose_name="Минимальное количество")
    max_count = models.IntegerField(verbose_name="Максимальное количество")

    def __str__(self):
        return f"Изделие {self.name} от {self.product.name}"

# Элемент
class Element(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    value = models.BooleanField(verbose_name="Значение")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="elements",
                             verbose_name="Изделие")

    def __str__(self):
        return f"Элемент {self.name} от {self.item.name}"

# Ресурс
class Resource(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name='Изделие')

    def __str__(self):
        return f"Ресурс {self.element.name}"

# Набор признаков
class Attribute(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

    def __str__(self):
        return f"Признак {self.name} от {self.product.name}"

# Набор условий
class Condition(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="attributes",
                                  blank=True, null=True, verbose_name="Аттрибут")
    item_to_condition = models.ForeignKey(Item, on_delete=models.CASCADE,
                                          blank=True, null=True, verbose_name="Элемент условия")
    item_to_change = models.ForeignKey(Item, on_delete=models.CASCADE,
                                       blank=True, null=True, verbose_name="Изменяемый элемент")
    condition = models.CharField(max_length=255, verbose_name="Условие")

    def __str__(self):
        return f"Условие {self.name} от {self.product.name}"
