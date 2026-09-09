from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data["edad"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    # mostrar tabla de usuarios
    def get_all(cls):
        query = "SELECT * FROM usuarios"
        resultados = connectToMySQL('lista_usuarios').query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    @classmethod
    # crear un nuevo usuario para agregar a la tabla
    def save(cls, data):
        query = "INSERT INTO usuarios(nombre, apellido, edad, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW())"
        return connectToMySQL('lista_usuarios').query_db(query, data)
    