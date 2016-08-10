from django.test import TestCase
from .models import Food_Board
from food.foodie import get_urls, get_img_links, reddit_links_image

class FoodMethodTest(TestCase):

    def setup(self):
        Food_Board.objects.create(slug="monday")

    def test_food_exist(self):
        Food_Board.objects.create(slug="monday")
        desert = Food_Board.objects.get(slug="monday")

        self.assertEqual(desert.slug, 'monday')

    def test_foodie_if_it_work(self):
        subreddits = "Baking"
        links = reddit_links_image(subreddits)
        out = False
        if links != []:
            out = True
        self.assertEqual(out, True)
