from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    # path('signin/', views.signin_user, name='signin'),
    # path('forgottenPassford/', views.forgotten_password, name='forgottenPassword'),
    path('logout/', views.logout_user, name='logout'),
    path('subject/', views.subjects, name='subject'),
    path('subject/<str:pk>/delete', views.deleteSubject, name='deleteSubject'),
    path('subject/detail/<str:pk>/', views.classes, name='subject_detail'),
    path('subject/detail/<str:pk>/delete', views.deleteClass, name='deleteClass'),
    path('class/detail/<str:pk>/', views.class_detail, name='class_detail'),
    path('class/detail/<str:pk>/delete', views.deleteNote, name='deleteNote'),
    path('notes/', views.notes, name='notes'),
    path('note/detail/<str:pk>/', views.note_detail, name='note_detail'),
    path('note/detail/<str:pk>/question/delete', views.deleteQuestion, name='deleteQuestion'),
    path('tests/', views.tests, name='tests'),
    path('tests/<str:test_type>/create', views.test_create, name='create_test'),
    path('tests/<str:test_type>', views.test, name='test'),
]
