# tests/test_test_module.py

from odoo.tests.common import TransactionCase
print("TESTS LOADED!")

class TestTestModel(TransactionCase):
    
    def setUp(self, *args, **kwargs):
        ddfd
        super(TestTestModel, self).setUp(*args, **kwargs)
        print("Executed!")
        self.TestModel = self.env['test.model']

    def test_create_test_model(self):
        """Test the creation of a Test Model record."""
        record = self.TestModel.create({'name': 'Test Record'})
        print("Executed!")
        self.assertEqual(record.name, 'Test Record')

        # Check if the record is created
        self.assertEqual(record.name, 'Test Branch')
        self.assertEqual(record.code, 'TB01')
