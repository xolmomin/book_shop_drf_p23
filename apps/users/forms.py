from django.contrib.admin.forms import AdminAuthenticationForm


class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username + '@gmail.com'
