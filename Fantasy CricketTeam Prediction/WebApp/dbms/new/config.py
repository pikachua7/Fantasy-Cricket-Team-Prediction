from . import database

teams=[]
players=[]



class Teamcount:
    count=0

team0=Teamcount()
team1=Teamcount()

def countteam(team):
    if team==teams[0]:
        if team0.count<7:
            team0.count+=1
        else:
            return -1
    else:
        if team1.count<7:
            team1.count+=1
        else:
            return -1

def genereateMyteam():
    Myteam=[]
    keeper=database.keeper_gen()
    batsman=database.batsman_gen()
    allrounder=database.allrounder_gen()
    bowler=database.bowler_gen()

    mykeeper=keeper.mygenerate(teams)
    mybatsman=batsman.mygenerate(teams)
    mybowler=bowler.mygenerate(teams)
    myallrounder=allrounder.mygenerate(teams)
    
    #Selecting 1 best keeper
    Myteam.append(mykeeper[0]['Player'])
    countteam(mykeeper[0]['Team'])
    print(Myteam)

    #Selecting 2 best bastmen
    for i in range(2):
        Myteam.append(mybatsman[i]['Player'])
        countteam(mybatsman[i]['Team'])

    #Select 1 best allrounder
    Myteam.append(myallrounder[0]['Player'])
    countteam(myallrounder[0]['Team'])

    #Select 3 best bowlers
    for i in range(3):
        Myteam.append(mybowler[i]['Player'])
        countteam(mybowler[i]['Team'])

    #Select 1 best batsman with team constraint
    for i in range(3,len(mybatsman)):
        status=countteam(mybatsman[i]['Team'])
        if status==-1:
            continue
        else:
            Myteam.append(mybatsman[i]['Player'])
            if i<len(mybatsman)-1:
                j=i+1
                batsmanleft=sorted(mykeeper[1:]+mybatsman[j:],key=lambda j:j['Batting_Parameter'],reverse=True)
            else:
                batsmanleft=mykeeper[1:]
            break
    
    #Select 1 best keeper/batsman with team constraint
    for i in range(len(batsmanleft)):
        status=countteam(batsmanleft[i]['Team'])
        if status==-1:
            continue
        else:
            Myteam.append(batsmanleft[i]['Player'])
            break
    
    #Select 1 best allrounder with team constraints   
    for i in range(1,len(myallrounder)):
        status=countteam(myallrounder[i]['Team'])
        if status==-1:
            continue
        else:
            Myteam.append(myallrounder[i]['Player'])
            break
    
    #Select 1 best bowler with team constraint
    for i in range(3,len(mybowler)):
        status=countteam(mybowler[i]['Team'])
        if status==-1:
            continue
        else:
            Myteam.append(mybowler[i]['Player'])
            break
    return Myteam


def percentcalculate(Myteam):
    yourteam=[]
    for i in players:
        for j in i:
            yourteam.append(j)
    similar=0
    for i in yourteam:
        if i in Myteam:
            similar+=1
        else:
            continue
    percentage=round(similar*95/11)
    return percentage

