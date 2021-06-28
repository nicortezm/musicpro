# musicpro


## Estructura directorio y archivos
MUSICPRO/
|   db.sqlite3
|   manage.py
|   requirements.txt
|       
+---apps
|   +---accounts
|   |   |   admin.py
|   |   |   apps.py
|   |   |   forms.py
|   |   |   models.py
|   |   |   tests.py
|   |   |   urls.py
|   |   |   views.py
|   |   |   __init__.py
|   |   |   
|   +---carts
|   |   |   admin.py
|   |   |   apps.py
|   |   |   context_processors.py
|   |   |   models.py
|   |   |   tests.py
|   |   |   urls.py
|   |   |   views.py
|   |   |   __init__.py
|   |   |   
|   +---orders
|   |   |   admin.py
|   |   |   apps.py
|   |   |   forms.py
|   |   |   models.py
|   |   |   tests.py
|   |   |   urls.py
|   |   |   views.py
|   |   |   __init__.py
|   |   |   
|   \---tienda
|       |   admin.py
|       |   apps.py
|       |   context_processors.py
|       |   models.py
|       |   serializers.py
|       |   tests.py
|       |   urls.py
|       |   views.py
|       |   __init__.py
|       |   
|               
+---media
|   \---photos
|       +---categories
|       \---products
|               
+---musicpro
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   views.py
|   |   wsgi.py
|   |   __init__.py
|   |   
|   +---tests
|   |   |   test_models.py
|   |   |   test_urls.py
|   |   |   test_views.py
|   |   |   test_webpay.py
|   |   |   __init__.py
|   |   | 
+---static
|   +---admin
|   |   +---css
|   |   +---fonts
|   |   +---img
|   |   \---js 
|   +---css     
|   +---fonts
|   +---images
|   +---jet            
|   +---jet.dashboard   
|   +---js
|   +---range_filter
|   \---rest_framework
|       +---css
|       +---docs
|       +---fonts
|       +---img
|       \---js
\---templates
    |   base.html
    |   home.html
    +---accounts
    |       account_verification_email.html
    |       dashboard.html
    |       forgotPassword.html
    |       login.html
    |       register.html
    |       resetPassword.html
    |       reset_password_email.html
    +---admin
    |   |   base_site.html
    |   |   
    |   \---orders
    |       \---order
    |               change_list.html
    +---includes
    |       alerts.html
    |       footer.html
    |       navbar.html
    +---orders
    |       confirm.html
    |       payments.html
    \---store
            cart.html
            checkout.html
            product_detail.html
            store.html
            
