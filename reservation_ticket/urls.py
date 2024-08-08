
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register('gst',views.viewsets_guest)
router.register('mov',views.viewset_move)
router.register('res',views.viewset_res)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1 first method
    path('django/method/',views.first_method,name='first_method'),
    # 2 method from django 
    path('secondmethod/',views.second_method,name='second_method'),
    # 3 from rest fbv function based views 
    path('rest/',views.fbv_list),
    path('edit/<int:pk>',views.fbv_pk),
    # 4 from rest api cbv class based views
    path('cbv/',views.CbvList.as_view()),
    path('cbvpk/<int:pk>/',views.CbvPk.as_view()),
    #  5 rest mixin and generics
    path('mixin',views.mixin_list.as_view()),
    path('mixin/<int:pk>',views.mixin_pk.as_view()),
    # 6 generics views 
    path('gene',views.generics_list.as_view()),
    path('gene/<int:pk>',views.generics_pk.as_view()),
    # 7 viewsets from rest
    # url of viewset must use routers and include
    path('viewsets/',include(router.urls)),
    # 8 find movie
    path('find',views.findmovie),
    # new reservation
    path('new_res',views.new_res),
    #  this used to reset urls add log out 
    path('api-auth',include('rest_framework.urls')),
    # this to add token
    path('token/', obtain_auth_token),
    # view for post models with auth
    path('post/<int:pk>',views.Post_details.as_view()),




]
# {
#     "username": "boss",
#     "password": "1234"
# }