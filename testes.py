from main import database, app

#with app.app_context():
#    database.create_all()

#with app.app_context():
#    usuario = Usuario(username="Claudia", email="claudia@gmail.com", senha="121212")
#    usuario2 = Usuario(username="Renata", email="renata@gmail.com", senha="121212")
#    database.session.add(usuario)
#    database.session.add(usuario2)
#    database.session.commit()

#with app.app_context():
#    meus_usuarios = Usuario.query.all()
#    print(meus_usuarios)

#with app.app_context():
#    primeiro_usuario = Usuario.query.first()
#    print(primeiro_usuario)

#with app.app_context():
#    primeiro_usuario = Usuario.query.first()
#    print(primeiro_usuario.id)
#   print(primeiro_usuario.posts)

#with app.app_context():
#    meu_post = Post(id_usuario=1, titulo="Primeiro Post da Claudia", corpo="Claudia Postando")
#    database.session.add(meu_post)
#    database.session.commit()

#with app.app_context():
#    post = Post.query.first()
#    print(post.titulo)
#    print(post.autor.email)

#with app.app_context():
#    database.drop_all()
#    database.create_all()






