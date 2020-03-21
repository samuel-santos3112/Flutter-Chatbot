from models import Usuario
from conexao import Session



def criar(Usuario):
    try:   
        session = Session()

        session.add(Usuario)
        session.commit()
        return Usuario
    except Exception as e:
        print(e)
    finally:
        session.close()

def listar_por_nome(nome):
    try:
        session = Session()

        usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
        return usuario
    except Exception as e:
        print(e)
    finally:
        session.close()

def atualizar(id,usuario):
    try:
        session = Session()

        session.query(Usuario).filter(Usuario.id == id).update({
        Usuario.nome: usuario.nome,
        Usuario.senha: usuario.senha
        }, synchronize_session=False)
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

def deletar(id):
    try:
        session = Session()

        usuario = session.query(Usuario).get(id)
        session.delete(usuario)  
        session.commit()  
    except Exception as e:
        print(e)
    finally:
        session.close()

def listar():
    try:
        session = Session()

        usuarios = session.query(Usuario).all()
        usrs = []
        for usuario in usuarios:
            dic_usr = {
                'nome' : usuario.nome
            }
            usrs.append(dic_usr)  
        return usrs
    except Exception as e:
        print(e)
    finally:
        session.close()