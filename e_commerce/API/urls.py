from django.urls import path
from . import views
urlpatterns = [
    path('add_student',views.add_student),
    path('view_student',views.view_student),
    path('delete_student/<int:id>',views.delete_student),
    path('update_student/<int:id>',views.update_student)


]
