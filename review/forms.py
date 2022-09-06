from django import forms
from review.models import Institution, Review

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution 
        fields = ['subject', 'content'] 
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels = {
            'content': '답변내용',
        }