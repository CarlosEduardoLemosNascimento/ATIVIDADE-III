import unittest
from main import app, db
from models import Usuario

class TestCRUD(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/app'
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_adicionar_usuario(self):
        with self.app.app_context():
            from crud import adicionar_usuario
            adicionar_usuario("Teste", "teste@example.com")
            usuario = Usuario.query.filter_by(email="teste@example.com").first()
            self.assertIsNotNone(usuario)

    def test_excluir_usuario(self):
        with self.app.app_context():
            from crud import adicionar_usuario, excluir_usuario
            adicionar_usuario("Teste", "teste@example.com")
            usuario = Usuario.query.filter_by(email="teste@example.com").first()
            self.assertIsNotNone(usuario)
            excluir_usuario(usuario.id)
            usuario_deletado = Usuario.query.filter_by(email="teste@example.com").first()
            self.assertIsNone(usuario_deletado)

if __name__ == '__main__':
    unittest.main()
