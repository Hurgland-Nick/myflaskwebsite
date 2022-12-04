from flask import Flask, render_template, url_for,redirect

app = Flask(__name__)


# accueil
@app.route('/')
def accueil():
    return render_template('index.html')

# Index
@app.route('/index')
def mon_index():
    return render_template('accueil.html')

# A-propos
@app.route('/about')
def about():
    return render_template('about.html')

# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Blog
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Tutoriel
@app.route('/tutoriel')
def tutoriel():
    return render_template('tutoriel.html')

# Astrazeneca test
@app.route('/astrazeneca')
def astrazeneca():
    return render_template('Astrazeneca_page.html')

# Tutoriel -------> Python Index
@app.route('/tutoriel/Python/pythonindex')
def python_index():
    return render_template('pythonindex.html')

# Tutoriel -------> R Index
@app.route('/tutoriel/R/Rindex')
def r_index():
    return render_template('rindex.html')


# Tutoriel -------> R Index
@app.route('/tutoriel/Tableau/tableau_index')
def tableau_index():
    return render_template('tableau_et_OutilBi.html')


# R -------->  Hello Leaflet
@app.route('/R/introductionàleaflet')
def intro_a_leaflet():
    return render_template('Se_géolocaliser_avec_Leaflet.html')

# R -------->  Uber Pickups in New-York avec R
@app.route('/R/UberPickupsInNewYorkCity')
def UberPickups_avec_R():
    return render_template('Uber_Pickups_in_New-York_City.html')

# R -------->  Uber Pickups in New-York avec R
@app.route('/R/PythonpandasVSRdatatable')
def datatable_pandas():
    return render_template('Manipulation des Données avec R Data.Table Vs Pandas.html')

# R -------->  Lire et Ecrire dans une base de donnée avec R (New-York Flights)
@app.route('/R/NewYorkFlightsR')
def NewYorkFlights_R():
    return render_template('Nycflights_R.html')

# R -------->  Le paradoxe de Simpson
@app.route('/R/Le_Paradoxe_de_Simpson')
def paradoxe_de_simpson():
    return render_template('le_paradoxe_de_Simpson_notebook.html')

# R -------->  Chord_diagram
@app.route('/R/Chord_diagram')
def Chord_diagram():
    return render_template('Chord_diagram.html')

# R -------->  Installation de plusieurs librairies avec (R)
@app.route('/R/Installation_de_plusieurs_packages_avec_une_fonction_R')
def Install_packages_R():
    return render_template('Install_packages_R.html')


# R -------->  La Data Visualistion outil d'efficience commercial
@app.route('/R/Importance_de_la_datavisualistion')
def Importance_de_la_datavisualision():
    return render_template('La_Dataviz_outil_d_éfficience_commercial.html')


# R -------->  Web Scraping avec Rvest et NLP : Les mots les plus utilisés dans une revue (LevinSources) (R)
@app.route('/R/LesMotsLesPlusUtilises')
def Webscraping_and_NLP():
    return render_template('Web_Scraping & NLP & regex.html')


# R -------->  Visualisation du taux de criminalité en France par région en 2014 (R)
@app.route('/R/Taux_de_criminalite_france_2014')
def Criminalite_france_2014():
    return render_template('Départements__France_criminalité_en_2014.html')

# R -------->  Regression Logistique : Prédiction des Présidentielles au USA en 2012 (R)
@app.route('/R/Regression_logistique_election_USA')
def election_usa_2012():
    return render_template('prédiction_des_élections_au_USA.html')

# R -------->  Wiki scraping et ggplot: Population des Etats-Unis et Recensement (R)
@app.route('/R/Wiki_Scraping_Recensement_US_Population')
def Recensement_US_people():
    return render_template('Population_des_US_and_Scraping.html')


# R --------> Tableau Visualisation (LOD) VS R (Cas Superstore) (R)
@app.route('/R/Superstore_R_vs_TableauLOD')
def Superstore_R_vs_Tableau():
    return render_template('Superstore_R_vs_Tableau.html')


# R --------> Machine Learning Non Supervisé : Clustering de Document (R)
@app.route('/R/Clustering_de_document')
def Clustering_de_document():
    return render_template('Clustering_de_document.html')


# R --------> Se connecter sur Amazon RDS avec R VS Python (R)
@app.route('/R/Amazon_RDS_R_vs_Python')
def Amazon_RDS_R():
    return render_template('Amazon_RDS_R.html')

# R --------> Manipulation de Fichier JSON avec R (R)
@app.route('/R/Manipulation_JSON_avec_R')
def Manipulation_JSON_avec_R():
    return render_template('Manipulation_JSON_avec_R.html')

# R --------> EDA: Analyse des particules fines (R)
@app.route('/R/Analyse_exploratoire_des_particules_fines')
def Analyse_exploratoire_des_particules_fines():
    return render_template('Analyse_exploratoire_des_particules_fines.html')


#here--------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------


# Python --------> Se connecter sur Amazon RDS avec R VS Python (Python)
@app.route('/Python/Amazon_RDS_Python_vs_R')
def Amazon_RDS_Python():
    return render_template('Amazon_RDS_Python.html')

# Python -------->  Fraud detection avec SMOTE (Python)
@app.route('/Python/FraudDetectionAvecSmote')
def fraud_detection_smote():
    return render_template('fraud_detection_smote.html')

# Python -------->  Fraud detection avec Oversampling techniques (Python)
@app.route('/Python/FraudDetectionAvecOversamplingMethodes')
def fraud_detection_oversampling():
    return render_template('fraud_detection_ ML_and_Oversampling_tech.html')


# Python -------->  Gradient Boosting Classifier: Titanic Survivors (Python)
@app.route('/Python/TitanicSurvivors')
def titanic_survivors():
    return render_template('GridSearchCV & Gradient Boosting Classifier & XGboost & RandomForestClassifier.html')

# Python -------->  Breast Cancer with KNN  (Python)
@app.route('/Python/BreastCancerDetection')
def breast_cancer_knn():
    return render_template('Breast Cancer with K-Nearest Neighbors (KNN).html')

# Python -------->  Amazon Web Scraping : Scrapper des commentaires clients (Python)
@app.route('/Python/AmazonWebScraping')
def Amazon_web_scraping():
    return render_template('Amazon_web_scraping.html')

# Python -------->  Introduction à la Régression Linéaire (Approche Naîve) (Python)
@app.route('/Python/IntroductionRegLineaire')
def Intro_regression_lineaire():
    return render_template('Intro_regression_lineaire.html')

# Python -------->  Régression Linéaire avec Scikit-Learn (Python)
@app.route('/Python/RegLineaireAvecScikitLearn')
def Regression_lineaire_Scikit():
    return render_template('Linear_regression_with_scikit.html')

# Python -------->  Salary_prediction : Application Régression Linéaire avec Scikit-Learn (Python)
@app.route('/Python/SalaryPrediction')
def Salary_prediction():
    return render_template('Salary_prediction.html')


# Python -------->  Analyse des données: Python Pandas Vs RData.Table (Python)
@app.route('/Python/PythonpandasVSRdatatable')
def Pandas_datatable():
    return render_template('Manipulation des Données avec Pandas Vs R Data.Table.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')


