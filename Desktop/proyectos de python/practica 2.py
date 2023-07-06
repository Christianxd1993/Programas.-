class email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

s = email()
print(s.enviado)
s.enviar_correo()
print(s.enviado)