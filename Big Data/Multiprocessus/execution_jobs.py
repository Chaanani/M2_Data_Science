import os
import sys
import glob
import importlib
import multiprocessing
import time
import datetime
import logging


import datetime


now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]


# Définition de la classe Sequencer pour gérer l'exécution des jobs
class MultiprocessusJobs:
    # Initialisation de la classe avec le nombre de processeurs et le chemin des jobs
    def __init__(self, n_processors, job_path):
        self.n_processors = n_processors  # Nombre de processeurs
        self.job_path = job_path  # Chemin d'accès des jobs
        sys.path.append(self.job_path)  # Ajoute le chemin des jobs au PATH système

    # Fonction pour exécuter un job
    def execute_job(self, args):
        job, proc_id = args  # Extraire le nom du job et l'ID du processeur
        try:
            module = importlib.import_module(job)  # Importer le module/job
            resultat = module.run()  # Exécuter la fonction run() du module/job
            log_entry = f"Job {job} exécuté par le processeur {proc_id} en temps {now}: Résultat pour ce jon est  {resultat} "  # Créer un message de log
            return log_entry  # Retourner le message de log
        except Exception as e:
            log_entry = f"Erreur lors de l'exécution de {job} par le processeur en temps {now}"  # Message d'erreur
            return log_entry  # Retourner le message d'erreur

    # Fonction pour exécuter tous les jobs
    def run(self):
        os.chdir(self.job_path)  # Changer le répertoire courant pour le répertoire des jobs
        jobs_files = glob.glob("*.py")  # Obtenir tous les fichiers .py (jobs)
        jobs = [module[:-3] for module in jobs_files]  # Enlever l'extension .py pour obtenir le nom du module

        total_jobs = len(jobs)  # Nombre total de jobs
        for i in range(0, total_jobs, self.n_processors):
            batch_jobs = jobs[i:i+self.n_processors]  # Prendre un lot de jobs selon le nombre de processeurs
            logging.info(f"Début du lot de jobs : {batch_jobs}")  # Journaliser le début du lot
            
            # Associer chaque job à un ID de processeur
            jobs_with_ids = [(job, f"Processeur-{idx % self.n_processors + 1}") for idx, job in enumerate(batch_jobs)]
            
            # Exécuter les jobs en parallèle
            with multiprocessing.Pool(processes=self.n_processors) as pool:
                logs = pool.map(self.execute_job, jobs_with_ids)

            # Enregistrer les résultats dans des fichiers et les journaliser
            for job, log in zip(batch_jobs, logs):
                with open(f"{job}.result", "a") as fichier:
                    fichier.write(log + "\n")  # Écrire le résultat dans un fichier
                logging.info(log)  # Journaliser le résultat
            
            logging.info(f"Fin du lot de jobs : {batch_jobs}")  # Journaliser la fin du lot

    # Fonction pour visualiser les résultats
    def trace_execution(self):
        os.chdir(self.job_path)  # Changer le répertoire courant pour le répertoire des jobs
        jobs_files = glob.glob("*.result")  # Obtenir tous les fichiers .result
        for job in jobs_files:
            with open(job, 'r') as f:
                print(f" {f.read()}")  # Afficher le résultat pour chaque job

if __name__ == "__main__":
    # Obtenir l'heure et la date actuelles pour le nom du fichier de log
    maintenant = datetime.datetime.now()
    heure = maintenant.hour
    minute = maintenant.minute
    seconde = maintenant.second
    
    # Configurer le journal (logging)
    logging.basicConfig(filename=f"execution_{datetime.date.today()}_{heure}_{minute}_{seconde}.log", encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Vérifier si le nombre de processeurs est fourni en argument
    if len(sys.argv) < 2:
        print("Veuillez fournir le nombre de processeurs .")
        sys.exit(1)

    n = int(sys.argv[1])  # Nombre de processeurs
    
    path = "C:\\Users\\msi\\Desktop\\M2_Data_Science\\database\\Multiprocessus\\jobs"  # Chemin d'accès des jobs

    dateactuale = time.time()  # Heure de début
    MultiprocessusJob = MultiprocessusJobs(n, path)  # Créer une instance de Sequencer
    MultiprocessusJob.run()  # Exécuter tous les jobs
    

    print("\nVisualisation des résultats :")  # Afficher les résultats
    MultiprocessusJob.trace_execution()  # Visualiser les résultats
    print("================================ le temsp d'exécution ==================================================")
    print(f"Temps total d'exécution : {time.time() - dateactuale} secondes")  # Afficher le temps total d'exécution

