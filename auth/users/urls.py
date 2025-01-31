from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view())
]

# as_view(): used to convert a class-based view (CBV) into a callable function (like get(), post(), etc.)that Django can handle as a view.
