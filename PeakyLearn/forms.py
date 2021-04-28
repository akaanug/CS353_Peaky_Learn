from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(max_length=254)
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    uname = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    pw = forms.CharField(widget=forms.PasswordInput())

    def get_fields(self):
        return { 'email': self.email, 'fname': self.fname, 'lname': self.lname,
                'uname': self.uname, 'phone': self.phone, 'pw': self.pw }
