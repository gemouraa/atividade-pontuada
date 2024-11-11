import pytest
from app.models.usuario_models import Usuario
from app.config.database import db
import os 

os.system("cls||clear")

@pytest.fixture 

def usuario_valido():
    usuario = Usuario("moura", "moura@gmail.com", "12345")
    return usuario

def test_nome_valido(usuario_valido):
    assert usuario_valido.nome == "moura"

def test_email_valido(usuario_valido):
    assert usuario_valido.email == "moura@gmail.com"

def test_senha_valida(usuario_valido):
    assert usuario_valido.senha == "12345"



    