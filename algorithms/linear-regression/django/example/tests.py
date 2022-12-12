from django.test import TestCase
from .forms import LinearRegressionForm
from .models import LinearRegressionModel


class LinearRegressionFormTest(TestCase):
    def setUp(self):
        self.form = LinearRegressionForm(data={'x': '1,2,3', 'y': '1,2,3'})

    def test_form_validation_for_blank_items(self):
        form = LinearRegressionForm(data={'x': '', 'y': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['x'],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['y'],
            ["This field is required."]
        )

    def test_form_save_handles_saving_to_a_list(self):
        new_item = self.form.save()
        self.assertEqual(new_item, LinearRegressionModel.objects.first())

    def test_form_save(self):
        new_item = self.form.save()
        self.assertEqual(new_item.x, '1,2,3')
        self.assertEqual(new_item.y, '1,2,3')

    def test_form_train(self):
        new_item = self.form.save()
        new_item.train()
        saved_item = LinearRegressionModel.objects.first()
        self.assertEqual(saved_item, new_item)

    def test_form_predict(self):
        new_item = self.form.save()
        new_item.train()
        y = new_item.predict('1,2,3')
        self.assertEqual(y.tolist(), [1.0000000000000002, 2.0, 2.9999999999999996])
