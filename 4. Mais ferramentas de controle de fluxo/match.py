def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404: # multiplos cases
            return "Não permitido"
        case 418:
            return "I'm a teapot"
        case _: # default
            return "Something's wrong with the internet"
        
    
ponto = (2, 3)
match ponto:
    case(0, 0):
        print("Origem")
    case(0,y):
        print(f"Y={y}")
    case(x,0):
        print(f"X={x}")
    case(x,y):
        print(f"X={x} ,Y={y}")
    case _:
        raise ValueError("Não é um ponto")
    
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def onde_esta(ponto):
    match ponto:
        case Ponto(x=0, y=0):
            print("Origem")
        case Ponto(x=0, y=y):
            print(f"Y={y}")
        case Ponto(x=x, y=0):
            print(f"X={x}")
        case Ponto():
            print("Em outro lugar")
        case _:
            print("Não é um ponto")

ponto = Ponto(0,2)
onde_esta(ponto)        
