class Degree :
    def GetDegree():
        print("I got a degree")
class Undergraduate(Degree):
    def GetDegree():
        print("I am an undergraduate")
class Postgraduate(Degree):
    def GetDegree():
        print("I am a postgraduate")
Degree.GetDegree();
Undergraduate.GetDegree();
Postgraduate.GetDegree();
