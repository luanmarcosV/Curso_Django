from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipe, RecipeTestBase

rtb = RecipeTestBase()

class RecipeDetailTest(TestCase):    
    
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipe', kwargs={'pk': 1})
        )
        self.assertIs(view.func.view_class, views.RecipeDetail)

    # Test para verificar se a página da receita está carregando corretamente
    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'

        # Need a recipe for this test
        rtb.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                'recipe',
                kwargs={
                    'pk': 1
                }
            )
        )
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
        reverse('recipe', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, 404)