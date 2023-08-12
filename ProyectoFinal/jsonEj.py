import json


#print(x[0]["pregunta"])


class j():

    def __init__(self,pregunta,rc,ri) -> None:
        self.pregunta = pregunta
        self.rc = rc
        self.ri = ri
    def toDict(self):
        return vars(self)
    

pregunta = j("Que edad tengo",23,[29,34,23,12])
pregunta2 = j("Que edad tengo2",43,[29,34,23,12])

print(pregunta.toDict())
x = [pregunta.toDict(),pregunta2.toDict()]


with open(r"ejemplo.json", "w") as file:
        json.dump(x, file)