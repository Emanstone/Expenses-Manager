from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Userprofile)
class userprofile(admin.ModelAdmin):
    list_display = ('fullname', 'dob', 'address')

@admin.register(Incomecategory)
class incomecategory(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Income)
class income(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date')

# @admin.register(IncomeCategoryTab)
# class IncomeCategoryTab(admin.ModelAdmin):
#     list_display = ('name',)



# @admin.register(ExpenseCategoryTab)
# class ExpenseCategoryTab(admin.ModelAdmin):
#     list_display = ('name',)

@admin.register(Expensescategory)
class Expensescategory(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Expenses)
class Expenses(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date')


@admin.register(MonthlyBudget)
class budget(admin.ModelAdmin):
    list_display = ('name', 'amount', 'month')


# admin.site.register(IncomeReset)

# admin.site.register(ExpenseReset)