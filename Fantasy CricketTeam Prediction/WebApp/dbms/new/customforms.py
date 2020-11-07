from django import forms
from . import database,views,config



teams=(('CSK','CSK'),('DC','DC'),('KKR','KKR'),('KXIP','KXIP'),('MI','MI'),('RCB','RCB'),('RR','RR'),('SRH','SRH'))
class Team(forms.Form):
    team1=forms.ChoiceField(label='',initial='None',choices=teams)
    team2=forms.ChoiceField(label='',initial='None',choices=teams)
    

class keeper(forms.Form):
    
    def __init__(self,choice=None,*args,**kwargs):
        super(keeper,self).__init__(*args,**kwargs)
        if choice:
            self.fields['keeper1'].choices=((x,x) for x in choice) 
    keeper1= forms.MultipleChoiceField(label='',widget=forms.CheckboxSelectMultiple (attrs={'class': 'special'}))


class batsman(forms.Form):
    def __init__(self,choice=None,*args,**kwargs):
        super(batsman,self).__init__(*args,**kwargs)
        if choice:
            self.fields['batsman1'].choices=((x,x) for x in choice)
    batsman1= forms.MultipleChoiceField(label='',widget=forms.CheckboxSelectMultiple (attrs={'class': 'special'}))   


class allrounder(forms.Form):
    def __init__(self,choice=None,*args,**kwargs):
        super(allrounder,self).__init__(*args,**kwargs)
        if choice:
            self.fields['allrounder1'].choices=((x,x) for x in choice)
    allrounder1= forms.MultipleChoiceField(label='',widget=forms.CheckboxSelectMultiple (attrs={'class': 'special'}))


class bowler(forms.Form):
    def __init__(self,choice=None,*args,**kwargs):
        super(bowler,self).__init__(*args,**kwargs)
        if choice:
            self.fields['bowler1'].choices=((x,x) for x in choice)
    bowler1= forms.MultipleChoiceField(label='',widget=forms.CheckboxSelectMultiple (attrs={'class': 'special'}))
