import socket
import sys
import os
import multiprocessing
import importlib
import pickle
import time 
def execute_job(job):
    try:
        module = importlib.import_module(job)
        resultat = module.run()
        log_entry = f"Job {job} exécuté avec succès : {resultat}"
        return log_entry
    except Exception as e:
        log_entry = f"Erreur lors de l'exécution de {job} : {e}"
        return log_entry

if __name__ == "__main__":
    # Vérifier si le nombre de processeurs est fourni en argument
    liste = sys.argv[1:] 
    if len(liste) < 2:
        print("Veuillez fournir le HOST et numbre de processus example: '127.0.0.1' 49 .")
        sys.exit(1)
    HOST = liste[0]  # Host

    n = int(liste[1])
    
    
    PORT = 65432

    path="C:\\Users\\msi\\Desktop\\M2_Data_Science\\database\\Multiprocessus\\jobs"

    sys.path.append(path)
    os.chdir(path)
    date=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Reçoit la liste des jobs du serveur
        jobs = pickle.loads(s.recv(4096))
        
        # Utilise multiprocessing pour exécuter les jobs en parallèle
        with multiprocessing.Pool(n) as pool:
            results = pool.map(execute_job, jobs)
            
        # Renvoie les résultats au serveur
        s.sendall(pickle.dumps(results))
        
print("======================================le temps d'exécution=====================================")
print(time.time()-date)

