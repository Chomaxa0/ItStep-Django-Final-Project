from django.db import models
from .validators import validate_alpha

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    age = models.IntegerField()
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.party})"


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=100, validators=[validate_alpha])
    voter_surname = models.CharField(max_length=100, validators=[validate_alpha])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote for {self.candidate.name} {self.candidate.surname} by {self.voter_name} {self.voter_surname} on {self.timestamp}"
