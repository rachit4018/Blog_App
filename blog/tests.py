from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email =  'test@gmail.com',
            password = 'secret',
        )
        self.post = Post.objects.create(
            title = 'A good title',
            author = self.user,
            text = 'Nice body content'
        )
    def test_string_representation(self):
        post = Post(title = 'A sample title')
        self.assertEqual(str(post), post.title)
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.text}', 'Nice body content')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
            'title' : 'new title',
            'author' : self.user,
            'text' : 'new text',
        })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'new title')

    def test_post_update_view(self):
        response =  self.client.post(reverse('post_update', args='1'),{
            'title' : 'update title',
            'text' : 'updated text',
        })
        self.assertEqual(response.status_code,302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete',args = '1'))
        self.assertEqual(response.status_code,302)


    

