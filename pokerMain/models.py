from django.db import models

# Create your models here.


class Cards(models.Model):

    def __str__(self):
        return self.card_name

    card_name = models.CharField(max_length=100)
    value = models.CharField(max_length=2)
    suit = models.CharField(max_length=1)
    image = models.ImageField(upload_to='images', default='image/none/noimg.jpg')


class SB_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class BB_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class utg_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class utg1_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class lj_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class hj_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class co_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class btn_100bb(models.Model):

    def __str__(self):
        return self.hand_name

    hand_name = models.CharField(max_length=100)
    suited = models.CharField(max_length=3)
    card1 = models.CharField(max_length=2)
    card2 = models.CharField(max_length=2)
    action = models.CharField(max_length=6)


class scoring(models.Model):
    attempts = models.IntegerField()
    correct = models.IntegerField()
    score = models.FloatField()


class report(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Bug = models.TextField(max_length=500)

