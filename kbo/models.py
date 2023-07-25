from django.db import models

# Create your models here.
class TeamList(models.Model):
    
    team = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f'{self.team}'
    
class TeamPlayer(models.Model):
    name = models.CharField(max_length=100)
    war = models.FloatField()
    hits= models.IntegerField(null=True)
    home_runs = models.IntegerField(null=True)
    batting_average = models.FloatField(null=True)  # Allow the field to be nullable
    on_base_plus_slugging = models.FloatField(null=True)
    games_played = models.IntegerField(null=True)
    position = models.CharField(max_length=10)
    team = models.ForeignKey(TeamList, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.team}  -  {self.name}'