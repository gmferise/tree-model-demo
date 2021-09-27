from website.shortcuts import render, redirect, redirect_back, redirect_hash

from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate as auth_getuser,
)

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from useraccount.models import UserAccount
from useraccount.forms import SignupForm, LoginForm

from filesystem.models import TreeNode
from filesystem.forms import CreateFolderForm, CreateFileForm

class FormView(View):
    """
    A generic view to render a form
    """
    Form = None
    title = None
    submit_text = None

    def get(self, request, form=None):
        return render(request, 'view/form.html', {
            'form': form or self.Form(),
            'title': self.title,
            'submit_text': self.submit_text,
        })

class Signup(FormView):
    Form = SignupForm
    title = 'Signup'
    submit_text = "Let's Bop!"

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            root = TreeNode.objects.create(
                name=f"ROOT_{data['username']}",
            )
            UserAccount.objects.create_user(
                **data,
                root=root,
            )
            return redirect('login')
        return self.get(request, form)

class Login(FormView):
    Form = LoginForm
    title = 'Login'
    submit_text = 'Show My Dox!'

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth_getuser(request, **form.cleaned_data)
            if user:
                auth_login(request, user)
                return redirect(request.GET.get('next', 'home'))
            else:
                form.add_error(None, 'Incorrect username or password')
        return self.get(request, form)

class Logout(View):
    def get(self, request):
        auth_logout(request) # will not error if no session
        return redirect_back(request)

class Home(LoginRequiredMixin, View):
    def get(self, request):    
        return render(request, 'view/home.html', {
            'nodes': TreeNode.objects.all(),
            'root': TreeNode.objects.get(id=request.user.root.id),
        })

class CreateNode(LoginRequiredMixin, View):
    Form = None
    title = None
    submit_text = 'Create'

    def get(self, request, in_id, form=None):
        return render(request, 'view/form.html', {
            'form': form or self.Form(),
            'title': self.title,
            'submit_text': self.submit_text,
        })

    def post(self, request, in_id):
        form = self.Form(request.POST)
        if form.is_valid():
            parent = TreeNode.objects.get(id=in_id or request.user.root.id)
            if parent.is_file:
                parent = TreeNode.objects.get(id=request.user.root.id)
            if parent.get_root().id != request.user.root.id:
                parent = TreeNode.objects.get(id=request.user.root.id)
            node = TreeNode.objects.create(
                **form.cleaned_data,
                parent=parent,
            )
            return redirect_hash('home', node.id)

        return self.get(request, in_id, form)

class CreateFile(CreateNode):
    Form = CreateFileForm
    title = 'New File'

class CreateFolder(CreateNode):
    Form = CreateFolderForm
    title = 'New Folder'