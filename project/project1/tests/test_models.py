from django.test import TestCase
from . .models import *
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print(" SetUpTestData")
        pass

    def setUp(self):
        print("SetUp ")
        pass

    '''def test_false_is_false(self):
         post=Pikir()
         self.assertFalse(post.get_number())'''

    def test_false_is_true(self):
        post=Pikir()
        self.assertTrue(post.get_number())
        
        
    '''def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two")
        post= Makal()
        self.assertEqual(1+1,2)'''
        
    
    '''def test_compare_numbers(self):
        post=Pikir()
        self.assertTrue(post.get_number(),9)'''
        
        
    