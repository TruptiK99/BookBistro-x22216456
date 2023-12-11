from django.urls import path
from . import views

urlpatterns=[
    path('',views.view_managebookings, name='view_managebookings'),
    path('history',views.view_history, name='view_history'),
    path('update_managebookings/<int:id>',views.update_managebookings, name='update_managebookings'),
    path('delete_managebookings/<int:id>',views.delete_managebookings, name='delete_managebookings'),
    # path('add_booktable/<int:id>', views.delete_booktable, name='delete_booktable'),
    # path('add_booktable/', views.booktable_form, name='add_booktable'),
    # path('update_booktable/<int:id>', views.booktable_form, name='update_booktable'),
    # path('book_booktable/<int:id>', views.book_booktable, name='book_booktable'),
    # path('create_booktable/<int:id>', views.create_booktable, name='create_booktable'),
    # path('bellsubscribe',views.bellsubscribe,name='bellsubscribe'),
]