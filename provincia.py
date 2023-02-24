class provincia:
    codigo: int
    nombre: str
    id : int
    bdname: str

    def __init__(self, id,nombre,codigo,bdname):
        self.id= id
        self.nombre = nombre
        self.codigo = codigo
        self.bdname = bdname


    def __str__(self):
        return self.nombre
    
class bdprov:
    host = "localhost"
    user = "root"
    password = ""
    db="lojurid_db"

    def __init__(self, host,user,password,db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

