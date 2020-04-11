from django import forms
from .models import Order


class RegisterForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
        max_length=64,
        label='수량'
    )

    # 사용자 정보는 세션이 들고 있기 때문에 따로 만들지 않음

    # id 값을 받기 때문에 interger 필드로 만듦
    product = forms.IntegerField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        },
        label='상품설명', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
