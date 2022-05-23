from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=500, label="", widget=forms.TextInput(
        attrs={'placeholder':'Type the new task', 'class':'w3-border w3-round-large w3-mobile'}))