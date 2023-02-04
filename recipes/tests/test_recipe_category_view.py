from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipe, RecipeTestBase

rtb = RecipeTestBase()

class RecipeCategoryTest(TestCase):    
    
    # Test se a página de Categoria carrega corretamente
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)
        
    # Test para verificar se as receitas aparecem na página de Categorias
    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        rtb.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)