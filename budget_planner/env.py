import environ

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "insecure-key"),
)
