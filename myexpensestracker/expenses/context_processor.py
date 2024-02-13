from .models import Userprofile

def profile_info(request):
    if request.user.is_authenticated:
        try:
            profile = Userprofile.objects.get(user=request.user)
            return {'user_profile': profile}
        except Userprofile.DoesNotExist:
            pass
    return {}


# def profile_info(request):
#     context = {}
#     if request.user.is_authenticated:
#         try:
#             profile = Userprofile.objects.get(user=request.user)
#             context['user_profile'] = profile
#         except Userprofile.DoesNotExist:
#             pass
#     return context


# def profile_info(request):

    
#     if request.user.is_authenticated:
#             try:
#                 profile = Userprofile.objects.get(user=request.user)
#             except Userprofile.DoesNotExist:
#                 profile = Userprofile.objects.create(user=request.user)  # Create if it doesn't exist
#             return {'user_profile': profile}