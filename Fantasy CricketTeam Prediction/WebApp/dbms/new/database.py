import pymongo
# from new.views import team

# teams=team

myc=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myc['ipl']

class batsman_gen:
    batsman=mydb['batsman']

    def generate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.batsman.find({'$or':[query1,query2]},{'_id':0,'Player':1}).sort('Player')
            for x in selected:
                array.append(x.get('Player'))
            return array
        else:
            array.append('0000')
        return array

    def mygenerate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.batsman.find({'$or':[query1,query2]},{'_id':0,'Player':1,'Batting_Parameter':1,'Team':1}).sort('Batting_Parameter',-1)
            for x in selected:
                array.append(x)
            return array
        else:
            array.append('0000')
        return array


class bowler_gen:
    bowler=mydb['bowler']

    def generate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.bowler.find({'$or':[query1,query2]},{'_id':0,'Player':1}).sort('Player')
            for x in selected:
                array.append(x.get('Player'))
            return array
        else:
            array.append('0000')
        return array

    def mygenerate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.bowler.find({'$or':[query1,query2]},{'_id':0,'Player':1,'Batting_Parameter':1,'Team':1}).sort('Bowling_Parameter')
            for x in selected:
                array.append(x)
            return array
        else:
            array.append('0000')
        return array


class allrounder_gen:
    allrounder=mydb['allrounder']

    def generate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.allrounder.find({'$or':[query1,query2]},{'_id':0,'Player':1}).sort('Player')
            for x in selected:
                array.append(x.get('Player'))
            return array
        else:
            array.append('0000')
        return array

    def mygenerate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.allrounder.find({'$or':[query1,query2]},{'_id':0,'Player':1,'Batting_Parameter':1,'Team':1}).sort('Allrounder_Parameter',-1)
            for x in selected:
                array.append(x)
            return array
        else:
            array.append('0000')
        return array 


class keeper_gen:
    keeper=mydb['keeper']
    
    def generate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.keeper.find({'$or':[query1,query2]},{'_id':0,'Player':1,'Batting_Parameter':1,'Team':1}).sort('Player')
            for x in selected:
                array.append(x['Player'])
            return array
        else:
            array.append('0000')
        return array

    def mygenerate(self,teams):
        array=[]
        if len(teams)>=2:
            query1={'Team':teams[0]}
            query2={'Team':teams[1]}
            selected=self.keeper.find({'$or':[query1,query2]},{'_id':0,'Player':1,'Batting_Parameter':1,'Team':1}).sort('Batting_Parameter',-1)
            for x in selected:
                array.append(x)
            return array
        else:
            array.append('0000')
        return array

   