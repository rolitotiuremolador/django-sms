from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from .views import home, element_processes, new_process
from .models import Element, Process, Kpi
from .forms import NewProcessForm

# Create your tests here.
class HomePageTests(TestCase):
    def setUp(self):
        self.element = Element.objects.create(element_name='Element 1', element_number=1, element_description='SMS Element 1')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_processes_page(self):
        element_processes_url = reverse('element_processes', kwargs={'pk': self.element.pk})
        self.assertContains(self.response, 'href="{0}"'.format(element_processes_url))

    def test_element_processes_view_contains_link_back_to_homepage(self):
        element_processes_url = reverse('element_processes', kwargs={'pk':1})
        response = self.client.get(element_processes_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

class ElementProcessesTests(TestCase):
    def setUp(self):
        Element.objects.create(element_name='Element 1', element_description='SMS Element 1', element_number=1 )
    
    def test_element_processes_view_success_status_code(self):
        url = reverse('element_processes', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_element_processes_view_not_found_status_code(self):
        url = reverse('element_processes', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_element_processes_url_resolves_element_processes_view(self):
        view = resolve('/elements/1/')
        self.assertEquals(view.func, element_processes)

    def test_element_processes_view_contains_navigation_links(self):
        element_processes_url = reverse('element_processes', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_process_url = reverse('new_process', kwargs={'pk': 1})
        response = self.client.get(element_processes_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_process_url))

class NewProcessTests(TestCase):
    def setUp(self):
        Element.objects.create(element_name='Element 1', element_description='SMS Element 1', element_number=1)
        User.objects.create_user(username='rolito', email='rolito@email.com', password='12345')

    def test_new_process_view_success_code(self):
        url = reverse('new_process', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_process_view_not_found_status_code(self):
        url = reverse('new_process', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_new_process_url_resolves_new_topic_view(self):
        view = resolve('/elements/1/new/')
        self.assertEquals(view.func, new_process)
    
    def  test_new_process_view_contains_link_back_to_element_processes_view(self):
        new_process_url = reverse('new_process', kwargs={'pk': 1})
        element_processes_url = reverse('element_processes', kwargs={'pk': 1})
        response = self.client.get(new_process_url)
        self.assertContains(response, 'href="{0}"'.format(element_processes_url))
    
    def test_csrf(self):
        url = reverse('new_process', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_process_valid_post_data(self):
        url = reverse('new_process', kwargs={'pk':1})
        data = {'process_name': 'Test title', 'kpi_name':'Lorem ipsum dolor sit amet' }
        response = self.client.post(url, data)
        self.assertTrue(Process.objects.exists())
        self.assertTrue(Kpi.objects.exists())

    def test_new_process_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is not to show the form again with validation errors
        '''
        url = reverse('new_process', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_process_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_process', kwargs={'pk':1})
        data = {'process_name': '', 'process_description': ''}
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Process.objects.exists())
        self.assertFalse(Kpi.objects.exists())

    def test_contains_form(self):
        url = reverse('new_process', kwargs={'pk':1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewProcessForm)

    def test_new_process_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validated errors
        '''
        url = reverse('new_process', kwargs={'pk':1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
           