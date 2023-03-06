import requests;
import json;

def readJson():
    response = requests.get("https://challenge.crossmint.io/api/map/a99655c3-8472-4c84-adf7-891d8ead71e2/goal")
    if response.status_code==200:
         data=response.json()
         json_result= json.dumps(data["goal"])
         matrix=json.loads(json_result)
                
         return matrix
    else:
            return print("Matrix not found", response.status_code) 

class UniverseElement:
    def __init__(self, row, column):
        self.row=row
        self.column= column

    def create(self):
        pass
    def delete(self):
        pass


class Polyanet(UniverseElement):

    def __init__(self, row, column):
        super().__init__(row)
        super().__init__(column)

    def create(self):
        json_payload1={
          "candidateId": "a99655c3-8472-4c84-adf7-891d8ead71e2",
          "row":self.row,
          "column":self.column} 
        headers= {'Content-Type': 'application/json'}
        try:
         requests.post("https://challenge.crossmint.io/api/polyanets",json=json_payload1, headers=headers,)
        except:
         print("Error creating Polyanet")
        return
    

    def delete(self):
            json_payload1={
                "candidateId": "a99655c3-8472-4c84-adf7-891d8ead71e2",
                "row":self.row,
                "column":self.column} 
            headers= {'Content-Type': 'application/json'}
            try:
                requests.delete("https://challenge.crossmint.io/api/polyanets",json=json_payload1, headers=headers,)
            except:
                print("Error deleting Polyanet")
            return

    

class Soloon(UniverseElement):

    def __init__(self, row, column, color):
        super().__init__(row)
        super().__init__(column)
        self.color=color

    def create(self):
        json_payload1={
          "candidateId": "a99655c3-8472-4c84-adf7-891d8ead71e2",
          "row":self.row,
          "column":self.column,
          "color":self.color} 
        headers= {'Content-Type': 'application/json'}
        try:
            requests.post("https://challenge.crossmint.io/api/soloons",json=json_payload1, headers=headers,)
        except:
            print("Error creating Soloon")
        return

    def delete(self):
        json_payload1={
            "candidateId": "a99655c3-8472-4c84-adf7-891d8ead71e2",
            "row":self.row,
            "column": self.column
            } 
        headers= {'Content-Type': 'application/json'}
        try:
            requests.delete("https://challenge.crossmint.io/api/soloons",json=json_payload1, headers=headers,)
        except:
            print("Error deleting Soloon")
        return

class Cometh(UniverseElement):

 def __init__(self, row, column, direction):
        super().__init__(row)
        super().__init__(column)
        self.direction=direction

 def createCometh(self):
     json_payload1={
          "candidateId": "a99655c3-8472-4c84-adf7-891d8ead71e2",
          "row":self.row,
          "column":self.column,
          "direction":self.direction} 
     headers= {'Content-Type': 'application/json'}
     try:
         requests.post("https://challenge.crossmint.io/api/comeths",json=json_payload1, headers=headers,)
     except:
         print("Error creating Cometh")

     return

 def deleteCometh(self):
        json_payload1={
            "candidateId": "a99655c3-8472-4c84-adf7-891d8ead71e2",
            "row":self.row,
            "column":self.column
            } 
        headers= {'Content-Type': 'application/json'}
        try:
            requests.delete("https://challenge.crossmint.io/api/comeths",json=json_payload1, headers=headers,)
        except:
            print("Error deleting Cometh")
        return

class Megaverse():

 def __init__(self):
        self.createUniverse= "Hello world"


   
 def switch_case(matrixValue):
    if matrixValue == "RIGHT_COMETH":
        return 3
    elif matrixValue == "UP_COMETH":
        return 2
    elif matrixValue == "DOWN_COMETH":
        return 1
    
    elif matrixValue == "LEFT_COMETH":
        return 4
    elif matrixValue == "POLYANET":
        return 5
    elif matrixValue == "WHITE_SOLOON":
        return 6
    elif matrixValue == "PURPLE_SOLOON":
        return 7
    
    elif matrixValue == "BLUE_SOLOON":
        return 8
    elif matrixValue == "RED_SOLOON":
        return 9
    else:
        return "Invalid value"

 def createElement(universeElement):
   universeElement.create()

 def createPolyanets():
        matrix = readJson()
        n = len(matrix)
        for i in range(2,n-2):
            try:
                polyanet= Polyanet(i,j)
                Megaverse.createElement(polyanet)
                if i != n - i - 1:
                 polyanet=Polyanet(i,n-1-i)   
                 Megaverse.createElement(polyanet)
                
            except:
             print("Error in creating Polyanets")
      
        return  

 def createMegaverse():
    matrix= readJson()
    n = len(matrix)
    for i in range(n):
        m=len(matrix[i])
        
        for j in range(m):
          resultCase= Megaverse.switch_case(matrix[i][j])
          if resultCase ==1:
            cometh=Cometh(i,j,"down")
            Megaverse.createElement(cometh)
          elif resultCase==2:
            cometh=Cometh(i,j,"up")
            Megaverse.createElement(cometh)
          elif resultCase==3:
            cometh=Cometh(i,j,"right")
            Megaverse.createElement(cometh)
          elif resultCase==4:
            cometh=Cometh(i,j,"left")
            Megaverse.createElement(cometh)
          elif resultCase==5:
            polyanet= Polyanet(i,j)
            Megaverse.createElement(polyanet)
          elif resultCase==6:
            soloon= Soloon(i, j,"white" )
            Megaverse.createElement(soloon)
          elif resultCase==7:
            soloon= Soloon(i, j,"purple" )
            Megaverse.createElement(soloon)
          elif resultCase==8:
            soloon= Soloon(i, j,"blue" )
            Megaverse.createElement(soloon)
          elif resultCase==9:
            soloon= Soloon(i, j,"red" )
            Megaverse.createElement(soloon)
          else: 
            pass
        
    return

 def deleteElement(universeElement):
   universeElement.delete()

 def deleteMegaverse():
    matrix= readJson()
    n = len(matrix)
    polyanet= Polyanet(i,j)
    for i in range(n):
      m=len(matrix[i])
      for j in range(m):
        Megaverse.deleteElement(polyanet)      
    return

Megaverse.createMegaverse()
