import threading
import time

class Accessoire:
    pass

class Pic(Accessoire):
    def __init__(self):
        self.postits = []

    def embrocher(self, postit):
        self.postits.append(postit)

    def liberer(self):
        if self.postits:
            return self.postits.pop()

class Bar(Accessoire):
    def __init__(self):
        self.plateaux = []

    def recevoir(self, plateau):
        self.plateaux.append(plateau)

    def evacuer(self):
        if self.plateaux:
            return self.plateaux.pop()

class Serveur:
    def __init__(self, pic, bar, commandes, verbose=False):
        self.pic = pic
        self.bar = bar
        self.commandes = commandes
        self.verbose = verbose

    def prendre_commande(self):
        while self.commandes:
            commande = self.commandes.pop(0)
            print(f"[Serveur] je prends commande de '{commande}'")
            self.pic.embrocher(commande)
        print("[Serveur] il n'y a plus de commande à prendre")

    def servir(self):
        while True:
            time.sleep(1)  # Simule le temps de préparation
            commande = self.pic.liberer()
            if commande:
                print(f"[Serveur] je sers '{commande}'")
                self.bar.recevoir(commande)
            else:
                break

class Barman:
    def __init__(self, pic, bar, verbose=False):
        self.pic = pic
        self.bar = bar
        self.verbose = verbose

    def preparer(self):
        while True:
            commande = self.pic.liberer()
            if commande:
                print(f"[Barman] je commence la fabrication de '{commande}'")
                time.sleep(2)  # Simule le temps de préparation
                print(f"[Barman] je termine la fabrication de '{commande}'")
                self.bar.recevoir(commande)
            else:
                break

def main():
    pic = Pic()
    bar = Bar()
    commandes = ["1 pastis", "2 demis", "1 ti-punch + 1 planteur"]
    
    serveur = Serveur(pic, bar, commandes, verbose=True)
    barman = Barman(pic, bar, verbose=True)

    print("[Barman] prêt pour le service !")
    print("[Serveur] prêt pour le service")

    serveur_thread = threading.Thread(target=serveur.prendre_commande)
    barman_thread = threading.Thread(target=barman.preparer)

    serveur_thread.start()
    barman_thread.start()

    serveur_thread.join()
    barman_thread.join()

    while True:
        plateau = bar.evacuer()
        if plateau:
            print(f"[Serveur] je sers '{plateau}'")
        else:
            break

if __name__ == "__main__":
    main()
