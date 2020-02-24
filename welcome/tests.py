#import os
from .models import PageView
#from .database import info
#from django.test import TestCase

# These basic tests are to be used as an example for running tests in S2I
# and OpenShift when building an application image.

#class PageViewTest(TestCase):
#    def test_index(self):
#        resp = self.client.get('/')
#        self.assertEqual(resp.status_code, 200)

#class DbEngine(TestCase):
#    def setUp(self):
#        os.environ['ENGINE'] = 'SQLite'

#    def test_engine_setup(self):
#        settings = info()
#        self.assertEqual(settings['engine'], 'SQLite')
#        self.assertEqual(settings['is_sqlite'], True)
