class GestionBotTrading:
    def __init__(self, api_key, api_secret, passphrase):
        self.api = Client(api_key, api_secret. passphrase)
        self.bot_activo = False

    def arrancar_bot(self):
        if not self.activo:
            self.api.conectar()
            self.activo = True
            print("Bot de trading arrancado.")
        else:
            print("El bot de trading ya está en funcionamiento.")

    def parar_bot(self):
        if self.activo:
            self.api.desconectar()
            self.activo = False
            print("Bot de trading detenido.")
        else:
            print("El bot de trading ya está detenido.")

    def gestionar_bot(self, comando):
        if comando == "arrancar":
            self.arrancar_bot()
        elif comando == "parar":
            self.parar_bot()
        else:
            print("Comando no reconocido")
