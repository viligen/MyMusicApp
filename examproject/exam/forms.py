from django import forms

from examproject.exam.models import Profile, Item


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = '__all__'

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                })

        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ()


# Item Forms


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                })

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class DeleteItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }),
            'artist': forms.TextInput(
                attrs={
                    'readonly': True,
                }),
            'genre': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }),
            'description': forms.Textarea(
                attrs={
                    'disabled': 'disabled',
                }),
            'image_url': forms.URLInput(
                attrs={
                    'disabled': 'disabled',
                }),
            'price': forms.NumberInput(
                attrs={
                    'disabled': 'disabled',
                })

        }