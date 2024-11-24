from django.shortcuts import redirect
from django.urls import reverse

"""def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('vista_login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
"""



def login_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('vista_login')}?next={request.path}")
        return view_func(request, *args, **kwargs)
    return wrapped_view
