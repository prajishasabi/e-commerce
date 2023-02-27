from django.test import TestCase
from django.urls import reverse, resolve 
from rest_framework.test import APIClient
from rest_framework import status


class TestSample (TestCase):

    def setup (self): 
        self.client = APIClient

    def test_index (self): #Method name should start with 'test'
        url = reverse('siteadmin:index') #get the url
        res = self.client.get(url) #Calling the url and save the response into a variable
        print (res.data)

        #The test will pass only if the status code equal to 200. Status code 200 represent the ok or success

        self.assertEquals (res.status_code, 200 )
        #The test will pass only if the response is equal to 'Congratulations, you have created an API

        self.assertEquals(res.data, 'You have created an API' )