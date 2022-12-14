from django import forms
from review.models import Institution, Review

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution 
        fields = ['subject', 'content', 'text'] 
        labels = {
            'subject': '제목',
            'content': '내용',
            'text': '설명',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'age']
        labels = {
            'content': '답변내용',
            'age' : '연령대',
        }