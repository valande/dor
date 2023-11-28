DEBUG = True
PORT = 8080
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True


PASSWORDS = {
    "admin": "$pbkdf2-sha256$29000$4Rxj7L0XohTinLOWEmKsFQ$uWTdFIZpcWdbBIZntUnX0AoSrnbWUOe5mMmmDk5FeYM",
    "normaluser": "$pbkdf2-sha256$29000$sPbe21vLec.5lxLifK91zg$edp3rXsH4k/WC9nqJT5IwCvaH/ZrKAp3nPdGKypyyR8",
}

ADMIN_USERS = ["admin"]