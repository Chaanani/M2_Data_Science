# import json

# import numpy as np
# import pandas as pd
import pandera as pa
import requests
import pandas as pd

from flask import Flask  , request, jsonify
from data_validation import parameter_schema, CourseContentData, StudentProfileData, ParametersSchema
from marshmallow.exceptions import ValidationError


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/random-recommendation", methods=['GET'])
def generate_reco():
    """
    Route d'API de recommandation aléatoire de contenu pédagogique pour étudiants.

    La route d'API prend 2 paramètres :
    - student_id : entier identifiant l'étudiant, obligatoire
    - keyword : mot clé désignant le centre d'intérêt pour lequel
    l'étudiant veut une recommandation, facultatif.

    Returns
    -------
    Dataframe converti en JSON correspondant au contenu recommandé.
    """

    try:
        # 1. Récupérer et valider les paramètres de la requête
        params = parameter_schema.load(request.args)

        # 2. Lire et valider les données des CSV
        students_df = pd.read_csv("student_data.csv")
        courses_df = pd.read_csv("courses_data.csv")
        StudentProfileData.validate(students_df)
        CourseContentData.validate(courses_df)

        # 3. Logique de recommandation
        keyword = params.get('keyword')
        student_id = params.get('student_id')
        if keyword:
            filtered_courses = courses_df[courses_df['keyword'] == keyword]
        else:
            student_interest = students_df[students_df['student_id'] == student_id]['area_of_interest'].iloc[0]
            filtered_courses = courses_df[courses_df['keyword'] == student_interest]

        if not filtered_courses.empty:
            recommended_content = filtered_courses.sample(n=1).to_json(orient='records')
        else:
            recommended_content = "No content available for the given criteria."

        
        return jsonify(recommended_content)

    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400

    


    
    # 1. Récupérer les paramètres de la requête d'API et les valider
    # avec parameter_schema (avec la librairie Marshmallow)

    # 2. Récupérer les données des étudiants et des cours à partir
    # des CSV & valider ces données (avec la librairie Pandera)

    # 3. Implémenter la logique de recommandation (tirage aléatoire basé sur
    # sur le mot-clé ou le centre d'intérêt)

    # 4. Renvoyer (au format JSON) la ligne du dataframe de contenus
    # correspondant au contenu recommandé trouvé ci-dessus.


# Le code ci-dessous permet à Flask de rattraper une exception de type ValidationError
# levée par Marshmallow et de renvoyer en sortie d'API le message d'erreur
# correspondant avec un code HTTP 400.
@app.errorhandler(ValidationError)
def error_handling(error):
    return error.messages, 400


# Même principe pour les 2 ci-dessous avec les erreurs de pandera.
@app.errorhandler(pa.errors.SchemaErrors)
def handle_pandera_validation_error(error):
    message = f"Invalid data received from DB: {error}"
    return message, 400


@app.errorhandler(pa.errors.SchemaErrors)
def handle_multiple_pandera_validation_error(error):
    message = f"Invalid data received from DB: {error}"
    return message, 400


# spécifier le port (par défaut, Flask est sur le 5000) :
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# et faire tourner l'app avec python app.py et non flask run

# autre méthode pour spécifier le port : flask run --host=0.0.0.0 --port=80
