from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    # mostrar tabla de usuarios
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('lista_usuarios').query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    @classmethod
    # crear un nuevo usuario para agregar a la tabla
    def save(cls, data):
        query = "INSERT INTO usuarios(nombre, apellido, edad) VALUES (%(nombre)s, %(apellido)s, %(edad)s)"
        return connectToMySQL('lista_usuarios').query_db(query, data)


    @classmethod
    # se selecciona el usuario que se quiere ver a más a detalle
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL('usuarios_crud').query_db(query, data)
        return cls(resultado[0])
    