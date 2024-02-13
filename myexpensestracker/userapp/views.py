from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import UpdateView
from expenses.models import *
from django.contrib.auth.models import User
from expenses.models import Userprofile
from django.contrib.auth.decorators import login_required


# Create your views here.

class BaseProfileView(View):
    def get_profile_info(self, user):
        try:
            user = Userprofile.objects.get(user=user)
            # profile_complete = all(
            #     [user.username, user.email, user.dob, user.address]
            # )

            profile_info = {
                'profile_image_url': user.profile_image.url if user.profile_image else None,
                'username': user.username,
                'full_name': user.fullname,
                'address': user.address,
                'dob': user.dob,
            }

            return {'profile_info': profile_info}

            # return {'profile_info': profile_info, 'profile_complete': profile_complete}

        except User.DoesNotExist:
            return {}



# class ProfilePage(LoginRequiredMixin, BaseProfileView):
#     login_url = 'login'

#     def get(self, request):
#         if request.user.is_superuser:
#             profile_image_url = None  # Or use a default image URL for superusers
#             context = self.get_profile_info(request.user)
#             context.update({'profile_image_url': profile_image_url})  # Add image URL to context
#             return render(request, 'usertemp/profile.html', context=context)
#         else:
#             try:
#                 user_profile = Userprofile.objects.get(user=request.user)
#             except Userprofile.DoesNotExist:
#                 return redirect('editprofile')  # Redirect to create the profile

#             profile_image_url = user_profile.profile_image.url if user_profile.profile_image else None
#             context = {**self.get_profile_info(request.user), **{'profile_image_url': profile_image_url}}
#             return render(request, 'usertemp/profile.html', context=context)
        

#     def post(self, request):
#         # Process the submitted form data
#         # Redirect to the profile page
#         return redirect('usertemp/profile.html')




class ProfilePage(LoginRequiredMixin, BaseProfileView):
    login_url = 'login'

    def get(self, request):
        user_profile = Userprofile.objects.get(user=request.user)
        if user_profile.profile_image:
            profile_image_url = user_profile.profile_image.url
        else:
            profile_image_url = None  # Or a default image URL
        

        # combining 2 different dictionaries using the spread syntax : which is formed by **(multoplication operator)
        context = {**self.get_profile_info(request.user), 
                   **{'profile_image_url': profile_image_url}}

        if not context:
            return redirect('editprofile')

        return render(request, 'usertemp/profile.html', context=context)

    def post(self, request):
        # Process the submitted form data
        # Redirect to the profile page
        return redirect('usertemp/profile.html')





class EditProfilePage(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        
        # context = self.get_profile_info(request.user)
        try:
            user = Userprofile.objects.get(user=request.user)
        except Userprofile.DoesNotExist:
            return redirect('signup')

        user_profile = Userprofile.objects.get(user=request.user)
        if user_profile.profile_image:
            profile_image_url = user_profile.profile_image.url
        else:
            profile_image_url = None  # Or a default image URL

        # context = {'profile_image_url': user_profile.profile_image.url,}   


        context = {
            'profile_info': {
                'profile_image_url': user.profile_image.url if user.profile_image else None,
                'username': user.username,
                'fullname': user.fullname,
                'email': user.email,
                'address': user.address,
                'dob': user.dob,
            },

            'form_data': {
            'username': user.username,
                'fullname': user.fullname,
                'email': user.email,
                'address': user.address,
                'dob': user.dob,
            },
        }

        if not context:
            return redirect('editprofile')

        return render(request, 'usertemp/editprofile.html', context=context)


    def post(self, request):
        profile_image = request.FILES.get('postimage')
        username = request.POST.get('Username')
        fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        address = request.POST.get('Address')
        dob = request.POST.get('dob')
        

        user = Userprofile.objects.get(user=request.user)

        # Get all form fields to be validated
        fields = {
            'username': username,
            'fullname': fullname,
            'email': user.email,
            'address': address,
            'dob': dob,
        }

        # Validate each field, ignoring empty fields and preventing 'none' values
        for field_value in fields.items():
            if field_value and field_value != 'none':
                if not field_value:
                    # If the field is empty, skip validation
                    continue


        # Process the uploaded profile image (if any)
        if profile_image:
            user.profile_image = profile_image
            user.save()

        # Update author information
        user.username = username
        user.fullname = fullname
        user.email = email
        user.address = address
        user.dob = dob
        user.save()
        # messages.success(request, 'Profile Updated Successfully')
        return redirect('profilepage')