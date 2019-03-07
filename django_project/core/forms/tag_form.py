# coding: utf-8
__author__ = 'Alison Mukoma <mukomalison@gmail.com>'


from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TagForm(forms.Form):
    """Form to capture user tag of choice to see related cat images."""

    tag = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'search'
        self.form_method = 'post'
        self.form_action = 'submit_tag'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-3'

        self.helper.add_input(Submit('submit', 'Search Cat Tag'))

    def save(self):
        instance = super(TagForm, self).save(commit=False)
        instance.author = self.user
        instance.save()
        return instance
