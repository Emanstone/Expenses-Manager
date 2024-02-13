from django.urls import path
from .views import *


urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('signup/', Signup.as_view(), name='signup'),
    path('register/<str:activation_key>/', RegisterActivationView.as_view(), name='register_activation'),
    path('/register', Register.as_view(), name='register'),
    path('logout/', Logout, name='logout'),
    path('incomecreate/', IncomeCreateView.as_view(), name='incomecreate'),
    path('income/', IncomeListView.as_view(), name='income-list'),
    path('incomecategorycreate/', IncomeCategoryCreateView.as_view(), name='incomecategory-create'),
    path('incomecategorylist/', IncomeCategoryListView.as_view(), name='incomecategory-list'),
    path('expensescreate/', ExpensesCreateView.as_view(), name='expensescreate'),
    path('expenses/', ExpensesListView.as_view(), name='expenses-list'),
    path('expensecategorycreate/', ExpensesCategoryCreateView.as_view(), name='expensecategory-create'),
    path('expensecategorylist/', ExpensesCategoryListView.as_view(), name='expensescategory-list'),
    path('total-income-by-category/', TotalIncomeByCategoryView.as_view(), name='total-income-by-category'),
    path('monthly-budget/', MonthlyBudgetView.as_view(), name='monthly-budget'),
    path('monthly-budget-list/', MonthlyBudgetListView.as_view(), name='monthly-budget-list'),
    path('transaction-history/', TransactionHistoryView.as_view(), name='transaction-history'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot-password'),
    path('reset/<str:uidb64>/<str:token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
]


