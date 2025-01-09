from django.db import models

# Create your models here.
#  Director


class Director(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    def rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total_stars = sum(review.stars for review in reviews)
            return total_stars / reviews.count()
class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, related_name="reviews")
    GRADES = (
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *'))
    stars = models.IntegerField(choices=GRADES, default=1)
    def __str__(self):
        return f"review by : {self.movie}"
    

