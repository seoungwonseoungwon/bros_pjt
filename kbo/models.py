from django.db import models

# Create your models here.
class TeamList(models.Model):
    
    team = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f'{self.team}'
    
    def get_absolute_url(self):
        # return f'/company_info/{self.team}'
        return f'/{self.pk}/'
    
class Hitting(models.Model):
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
    

    
class Pitcher(models.Model):
    team = models.ForeignKey(TeamList, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    war = models.FloatField()
    games_played = models.IntegerField()
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    era = models.FloatField(default=0.0)
    saves =  models.IntegerField(default=0)
    holds = models.IntegerField(default=0)
    innings_pitched = models.FloatField(default=0.0)
    # Add other pitcher fields as necessary
    position = models.CharField(max_length=10, default='투수')

    def __str__(self):
        return f'{self.team}  -  {self.name}'