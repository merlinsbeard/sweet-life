from django.db import models

class Food_Board(models.Model):
    slug = models.SlugField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

class Food_Image(models.Model):
    board = models.ForeignKey(Food_Board, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.image
