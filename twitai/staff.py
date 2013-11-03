from django.contrib.auth.decorators import user_passes_test, login_required
from django.http.response import HttpResponse
from django.shortcuts import render


def staff_limit(user):
    return user.is_staff


@login_required()
@user_passes_test(staff_limit)
def staff_main(request):
    return render(request, 'staff.html')


