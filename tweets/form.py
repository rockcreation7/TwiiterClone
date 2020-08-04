from django import forms

from .model import Tweet

MAX_TWEET_LENGHT = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        field = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError('this tweet is too long')
        return content

