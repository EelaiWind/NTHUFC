# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Field, Div
from crispy_forms.bootstrap import  FormActions, InlineRadios
from users.models import Account
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from  django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    #username = forms.CharField()
    email = forms.EmailField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput,max_length=10)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # important!!!!! self.helper.form_tag = False
        self.helper.form_tag = False

        self.fields['email'].label = u'信箱'
        self.fields['password'].label = u'密碼'
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    u'登入',
                    Field('email'),
                    Field('password'),
                    HTML('<br>')
                ),
                FormActions(
                    Submit('submit', u'登入', css_class='btn btn-primary'),
                    css_class="submit-btn"
                ),
                css_class="login-form",
            ),
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = Account.objects.get(email=email)
            if not check_password(password, user.password):
                raise forms.ValidationError("登入失敗")
        except Account.DoesNotExist:
            raise forms.ValidationError("登入失敗")

        return cleaned_data

class ForgetPasswordForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(ForgetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # important!!!!! self.helper.form_tag = False
        self.helper.form_tag = False
        self.fields['username'].label = u'姓名'
        self.fields['email'].label = u'信箱'

        self.helper.layout = Layout(
            Div(
                Fieldset(
                    u'忘記密碼',
                    Field('username'),
                    Field('email'),
                    HTML('<br>')
                ),
                FormActions(
                    Submit('submit', u'提交', css_class='btn btn-primary'),
                    css_class="submit-btn"
                ),
                css_class="forget-password-form",
            ),
        )    
    
    def clean(self):
        cleaned_data = self.cleaned_data
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        try:
            user = Account.objects.get(username=username, email=email)            
        except Account.DoesNotExist:
            raise forms.ValidationError("提交失敗")

        return cleaned_data