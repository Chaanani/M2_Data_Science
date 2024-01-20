import socket
import sys
import os
import glob
import logging
import time
import datetime
import pickle

class ServerJobs:
    def __init__(self, job_path, host, port):
        self.job_path = job_path
        self.host = host
        self.port = port
        
        sys.path.append(self.job_path)
        os.chdir(self.job_path)
        self.jobs_files = glob.glob("*.py")
        self.jobs = [module[:-3] for module in self.jobs_files]
        
    def receive_data(self,conn):
        data = b""
        while True:
           packet = conn.recv(4096)
           if not packet: 
               break
           data += packet
        return data
    
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Serveur en écoute sur {self.host}:{self.port}")
            conn, addr = s.accept()
            with conn:
                print(f"Connecté à {addr}")
                # Envoie la liste des jobs
                conn.sendall(pickle.dumps(self.jobs))
                # Attend et reçoit les résultats
                data = self.receive_data(conn)
                results = pickle.loads(data)
                for job, log in zip(self.jobs, results):
                    with open(f"{job}.result", "a") as fichier:
                        fichier.write(log + "\n")
                        logging.info(log)  # Enregistrez le log ici
if __name__ == "__main__":
    maintenant = datetime.datetime.now()
    heure = maintenant.hour
    minute = maintenant.minute
    seconde = maintenant.second
    
   

    # Vérifier si le nombre de processeurs est fourni en argument
    if len(sys.argv) < 2:
        print("Veuillez fournir le HOST svp .")
        sys.exit(1)
    HOST = sys.argv[1]  # Nombre de processeurs
    PORT = 65432

    PATH = "C:\\Users\\msi\\Desktop\\M2_Data_Science\\database\\Multiprocessus\\jobs"
    logging.basicConfig(filename=f"execution_{datetime.date.today()}_{heure}_{minute}_{seconde}.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
    server = ServerJobs(PATH, HOST, PORT)
    server.run()
    print("=============================le temps d'exécution=========================")
    
    