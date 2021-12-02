from django.urls import path
from employee import views
urlpatterns = [
     path('', views.index, name="Homepage"),
     path('login', views.loginpage, name="LoginPage"),
     path('register', views.signuppage, name="RegisterPage"),
     path('logout', views.userlogout, name="LogoutPage"),
     path('addemployee', views.empadd, name="AddEmployeeForm"),
     path('updateemployee', views.empedit, name="UpdateEmployeeForm"),
     path('editemployee', views.empupdate, name="EditEmployee"),
     path('allemployeedetail', views.empview, name="AllEmployeeDetails"),
     path('removeemployee', views.removeemp, name="RemoveEmployee"),
     path('userdetail', views.userview, name="AllUserDetails"),
     path('searchdetails', views.search, name="Searchpage"),
     path('exportcsv', views.export_csv, name="export_csv"),
]