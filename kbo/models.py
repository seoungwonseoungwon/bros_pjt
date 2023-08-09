from django.db import models

# Create your models here.
class TeamList(models.Model):
    
    team = models.CharField(max_length=20)
    year = models.IntegerField(default=23)
    rank = models.IntegerField(null=True)
    batting_average = models.FloatField(null=True)
    on_base_percentage = models.FloatField(null=True)
    slugging_percentage = models.FloatField(null=True)
    on_base_plus_slugging = models.FloatField(null=True)
    Fielding_Percentage = models.FloatField(null=True)
    ERA = models.FloatField(null=True)
    WHIP = models.FloatField(null=True)
    win_percentage = models.FloatField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    pre_rank = models.PositiveIntegerField(default=0)
    pre_percent = models.FloatField(default=0)


    def __str__(self):
        return f'{self.team}'
    
    def get_absolute_player(self):
        # return f'/company_info/{self.team}'
        return f'/{self.team}_player/'
    
    def get_absolute_team(self):
        return f'/{self.team}/'
    

class PreRank(models.Model):
    
    team = models.ForeignKey(TeamList, on_delete=models.CASCADE,null=True)
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()
    four = models.FloatField()
    five = models.FloatField()
    six = models.FloatField()
    seven = models.FloatField()
    eight = models.FloatField()
    nine = models.FloatField()
    ten = models.FloatField()

    def __str__(self):
        return f'{self.team}'


    
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
    

