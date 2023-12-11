from django.test import TestCase

from neomodel import db, clear_neo4j_database

class YourTestClass(DjangoTestCase):
    def setUp(self):
        clear_neo4j_database(db)

    def test_something(self):
        pass
