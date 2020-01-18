from django import forms
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from jet.templatetags.jet_tags import (
    jet_select2_lookups,
    jet_next_object,
    jet_previous_object,
)
from jet.tests.models import TestModel, SearchableTestModel


class TagsTestCase(TestCase):
    def setUp(self):
        self.models = []
        self.searchable_models = []

        self.models.append(TestModel.objects.create(field1="first", field2=1))
        self.models.append(TestModel.objects.create(field1="second", field2=2))
        self.searchable_models.append(
            SearchableTestModel.objects.create(field1="first", field2=1)
        )
        self.searchable_models.append(
            SearchableTestModel.objects.create(field1="second", field2=2)
        )

    def test_select2_lookups(self):
        class TestForm(forms.Form):
            form_field = forms.ModelChoiceField(SearchableTestModel.objects)

        value = self.searchable_models[0]

        form = TestForm(initial={"form_field": value.pk})
        field = form["form_field"]
        field = jet_select2_lookups(field)
        choices = [choice for choice in field.field.choices]

        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0][0], value.pk)

    def test_select2_lookups_posted(self):
        class TestForm(forms.Form):
            form_field = forms.ModelChoiceField(SearchableTestModel.objects)

        value = self.searchable_models[0]

        form = TestForm(data={"form_field": value.pk})
        field = form["form_field"]
        field = jet_select2_lookups(field)
        choices = [choice for choice in field.field.choices]

        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0][0], value.pk)

    def test_non_select2_lookups(self):
        class TestForm(forms.Form):
            form_field = forms.ModelChoiceField(TestModel.objects)

        value = self.searchable_models[0]

        form = TestForm(initial={"form_field": value.pk})
        field = form["form_field"]
        field = jet_select2_lookups(field)
        choices = [choice for choice in field.field.choices]

        self.assertEqual(len(choices), len(self.models) + 1)
