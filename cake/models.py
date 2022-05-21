from django.db import models


class Category(models.Model):
    """Категория"""
    title = models.CharField("Категроия", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Sweets(models.Model):
    """Сладости"""
    title = models.CharField("Называния", max_length=50)
    price = models.PositiveSmallIntegerField("Цена", default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    img = models.ImageField(upload_to="sweets/")
    create_at = models.DateTimeField('Изготовлено', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сладости'
        verbose_name_plural = "Сладости"


class Order(models.Model):
    """ Форма Заказа """
    name = models.CharField("Имя", max_length=50)
    phone = models.CharField("Номер телефона", max_length=20)
    address = models.CharField("Адрес", max_length=50)
    messages = models.TextField("Сообщения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"


class Feedback(models.Model):
    """ Обратная связь """
    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("E-mail", max_length=50)
    messages = models.TextField("Сообщения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = "Обратная связь"


class Subscription(models.Model):
    email = models.EmailField()
    date = models.DateTimeField("Дата", auto_now_add=True)

    def __str__(self):
        return self.email
