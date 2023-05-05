from django.shortcuts import redirect
from django.contrib.auth.models import User

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnUrl=request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        user=request.session.get('user_id')
        user = User(id=user)
        # print(user)
        # print('use=',request.session.get('user_id'))
        if not request.session.get('user_id'):
            return redirect(f'/login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware

def order_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print( request.session.get('cart'))
        if not request.session.get('cart'):
            return redirect('/AllProduct')

        response = get_response(request)
        return response

    return middleware