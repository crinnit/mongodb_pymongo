# -*- coding: utf-8 -*-
# Aplicación de ejemplo para aprender uso de mongodb

# Importando libreria python para conectarnos a mongodb
import pymongo

# Datos de conexion para mongodb
connection_string = "mongodb://localhost"

# Estableciendo conexion con mongodb
connection = pymongo.MongoClient(connection_string)

# Estableciendo base de datos en mongodb a usar, si no existe mongo la creará
db = connection.blog

# Generando documentos a insertar
posts = [
    {
        "title":"Primer Post",
        "autor":"Admin",
        "body":"Primera entrada de nuestro blog :D",
        "votes": 10
    },
    {
        "title":"Segundo Post",
        "autor":"Admin",
        "body":"Segunda Entrada de nuestro querido blog :P",
        "tags":"dummy",
        "votes": 5
    },
    {
        "title":"Tercer Post",
        "body":"Leviossaaaa",
        "votes": 20
    },
    {
        "title":"Cuarto Post",
        "autor":"Anonimo",
        "body":"People don't forget",
        "tags":["hack","anon"],
        "votes": 1
    }
]

# Insertando documentos en collection posts, si no existe mongo la creará
db.posts.insert(posts)

print "\nVerificando que se guardaron los documentos"
for p in db.posts.find():
    print p

print "\nBuscando posts donde el autor sea Admin"
for d in db.posts.find({"autor":"Admin"}):
    print d

print "\nBuscando posts donde el autor sea Admin o Nulo"
for d in db.posts.find({"$or":[{"autor":"Admin"},{"autor":None}]}):
    print d

print "\nBuscando posts que contengan el tag dummy"
for d in db.posts.find({"tags":{"$in":["dummy"]}}):
    print d

print "\nBuscando posts que contengan el tag hack"
for d in db.posts.find({"tags":{"$in":["hack"]}}):
    print d

print "\nBuscando posts con más de 10 votos"
for d in db.posts.find({"votes":{"$gt":10}}):
    print d

print "\nBuscando posts con 10 votos o más"
for d in db.posts.find({"votes":{"$gte":10}}):
    print d

print "\nBuscando posts con menos de 10 votos"
for d in db.posts.find({"votes":{"$lt":10}}):
    print d

print "\nCreando nuevo post"
newpost = {
    "title":"Nuevo Post",
    "autor":"Anonimo",
    "body":"MongoDB es la ostia :D",
    "votes": 10,
    "tags": ["tech","anon"]
}
db.posts.insert(newpost)

print "\nVerificando que se guardaron los documentos"
for p in db.posts.find():
    print p

print "\nBuscando y editando posts sin tags"
for p in db.posts.find({"tags":None}):
    print "Agregando tags a "
    print p
    p.update({"type":["dummy"]})
    db.posts.save(p)

print "\nVerificando que se guardaron los documentos"
for p in db.posts.find():
    print p

# Limpiando collection
db.posts.drop()

# Cerrando conexion con la db y mongodb
db.logout()
connection.close()
