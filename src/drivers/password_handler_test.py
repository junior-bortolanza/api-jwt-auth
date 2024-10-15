from .password_handler import PasswordHandler

def test_encrypt():
    minha_senha = "123Junior"
    password_handle = PasswordHandler()

    hashed_password = password_handle.encrypt_password(minha_senha)
    password_checked = password_handle.check_password(minha_senha, hashed_password)

    assert password_checked
  