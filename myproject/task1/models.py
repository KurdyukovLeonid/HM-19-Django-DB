from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
for buyer in Buyer.objects.all():
    print(f'Buyer: {buyer.name}, Age: {buyer.age}, Games: {[game.title for game in buyer.games.all()]}')

for game in Game.objects.all():
    print(f'Game: {game.title}, Buyers: {[buyer.name for buyer in game.buyers.all()]}')