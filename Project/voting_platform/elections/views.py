from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote
from .forms import CandidateForm, VoteForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm


def custom_login_view(request):
    form = CustomAuthenticationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('custom_username')
            password = form.cleaned_data.get('custom_password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('candidate_list')
            else:
                form.add_error(None, 'მითითებული ინფორმაცია არასწორია!')
    return render(request, 'registration/login.html', {'form': form})

@login_required
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'elections/candidate_list.html', {'candidates': candidates})


# Homepage view
def homepage(request):
    return render(request, 'elections/homepage.html')

# Admin Views (restricted)
@login_required
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'elections/candidate_list.html', {'candidates': candidates})

@login_required
def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'elections/candidate_form.html', {'form': form})

@login_required
def candidate_update(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'elections/candidate_form.html', {'form': form})

@login_required
def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidate_list')
    return render(request, 'elections/candidate_confirm_delete.html', {'candidate': candidate})

# User Views
def user_candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'elections/user_candidate_list.html', {'candidates': candidates})

def vote(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.candidate = candidate
            vote.save()
            candidate.vote_count = candidate.vote_set.count()
            candidate.save()
            return redirect('user_candidate_list')
    else:
        form = VoteForm()
    return render(request, 'elections/vote_form.html', {'form': form, 'candidate': candidate})
