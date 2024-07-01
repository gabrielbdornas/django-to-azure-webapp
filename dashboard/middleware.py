from django.shortcuts import redirect

class RoleBasedRedirectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path == '/accounts/profile/':
                print(f"User {request.user.username} is being redirected based on role or superuser status.")
                if request.user.is_superuser:
                    return redirect('/admin/')
                elif request.user.userprofile.role.name == 'Tamil Translator':
                    return redirect('tamil_translator_dashboard')
                elif request.user.userprofile.role.name == 'Sinhala Translator':
                    return redirect('sinhala_translator_dashboard')
                elif request.user.userprofile.role.name == 'Illustrator':
                    return redirect('illustrator_dashboard')
                # Add more role-based redirections here if needed

        response = self.get_response(request)
        return response
