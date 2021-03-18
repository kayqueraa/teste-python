from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.config['MONGO_URI']=os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/cases', methods=['POST'])
def create_cases():
    iso_code = request.json['iso_code']
    continent = request.json['continent']
    location = request.json['location']
    date = request.json['date']
    total_cases = request.json['total_cases']
    new_cases = request.json['new_cases']
    new_cases_smoothed = request.json['new_cases_smoothed']
    total_deaths = request.json['total_deaths']
    new_deaths = request.json['new_deaths']
    new_deaths_smoothed = request.json['new_deaths_smoothed']
    total_cases_per_million = request.json['total_cases_per_million']
    new_cases_per_million = request.json['new_cases_per_million']
    new_cases_smoothed_per_million = request.json['new_cases_smoothed_per_million']
    total_deaths_per_million = request.json['total_deaths_per_million']
    new_deaths_per_million = request.json['new_deaths_per_million']
    new_deaths_smoothed_per_million = request.json['new_deaths_smoothed_per_million']
    reproduction_rate = request.json['reproduction_rate']
    icu_patients = request.json['icu_patients']
    icu_patients_per_million = request.json['icu_patients_per_million']
    hosp_patients = request.json['hosp_patients']
    hosp_patients_per_million = request.json['hosp_patients_per_million']
    weekly_icu_admissions = request.json['weekly_icu_admissions']
    weekly_icu_admissions_per_million = request.json['weekly_icu_admissions_per_million']
    weekly_hosp_admissions = request.json['weekly_hosp_admissions']
    weekly_hosp_admissions_per_million = ['weekly_hosp_admissions_per_million']
    new_tests = request.json['new_tests']
    total_tests = request.json['total_tests']
    total_tests_per_thousand = request.json['total_tests_per_thousand']
    new_tests_per_thousand = request.json['new_tests_per_thousand']
    new_tests_smoothed = request.json['new_tests_smoothed']
    new_tests_smoothed_per_thousand = request.json['new_tests_smoothed_per_thousand']
    positive_rate = request.json['positive_rate']
    tests_per_case = request.json['tests_per_case']
    tests_units = request.json['tests_units']
    total_vaccinations = request.json['total_vaccinations']
    people_vaccinated = request.json['people_vaccinated']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    new_vaccinations = request.json['new_vaccinations']
    new_vaccinations_smoothed = request.json['new_vaccinations_smoothed']
    total_vaccinations_per_hundred = request.json['total_vaccinations_per_hundred']
    people_vaccinated_per_hundred = request.json['people_vaccinated_per_hundred']
    people_fully_vaccinated_per_hundred = request.json['people_fully_vaccinated_per_hundred']
    new_vaccinations_smoothed_per_million = request.json['new_vaccinations_smoothed_per_million']
    stringency_index = request.json['stringency_index']
    population = request.json['population']
    population_density = request.json['population_density']
    median_age = request.json['median_age']
    aged_65_older = request.json['aged_65_older']
    aged_70_older = request.json['aged_70_older']
    gdp_per_capita = request.json['gdp_per_capita']
    extreme_poverty = request.json['extreme_poverty']
    cardiovasc_death_rate = request.json['cardiovasc_death_rate']
    diabetes_prevalence = request.json['diabetes_prevalence']
    female_smokers = request.json['female_smokers']
    male_smokers = request.json['male_smokers']
    handwashing_facilities = request.json['handwashing_facilities']
    hospital_beds_per_thousand = request.json['hospital_beds_per_thousand']
    life_expectancy = request.json['life_expectancy']
    human_development = request.json['human_development_index']

    id = mongo.db.covid2_info_table.insert(
        {
            'iso_code' : iso_code, 'continent' : continent, 'location' : location, 'date' : date, 'total_cases' : total_cases,
            'new_cases' : new_cases, 'new_cases_smoothed' : new_cases_smoothed, 'total_deaths' : total_deaths, 'new_deaths' : new_deaths,
            'new_deaths_smoothed' : new_deaths_smoothed, 'total_cases_per_million' : total_cases_per_million, 'new_cases_per_million' : new_cases_per_million,
            'new_cases_smoothed_per_million' : new_cases_smoothed_per_million, 'total_deaths_per_million' : total_deaths_per_million,
            'new_deaths_per_million' : new_deaths_per_million, 'new_deaths_smoothed_per_million': new_deaths_smoothed_per_million,
            'reproduction_rate' : reproduction_rate, 'icu_patients' : icu_patients, 'icu_patients_per_million' : icu_patients_per_million,
            'hosp_patients' : hosp_patients, 'hosp_patients_per_million' : hosp_patients_per_million, 'weekly_icu_admissions' : weekly_icu_admissions,
            'weekly_icu_admissions_per_million' : weekly_icu_admissions_per_million, 'weekly_hosp_admissions' : weekly_hosp_admissions,
            'weekly_hosp_admissions_per_million' : weekly_hosp_admissions_per_million, 'new_tests' : new_tests, 'total_tests' : total_tests,
            'total_tests_per_thousand' : total_tests_per_thousand, 'new_tests_per_thousand' : new_tests_per_thousand, 'new_tests_smoothed' : new_tests_smoothed,
            'new_tests_smoothed_per_thousand' : new_tests_smoothed_per_thousand, 'positive_rate' : positive_rate, 'tests_per_case' : tests_per_case,
            'tests_units' : tests_units, 'total_vaccinations' : total_vaccinations, 'people_vaccinated' : people_vaccinated, 'people_fully_vaccinated' :people_fully_vaccinated,
            'new_vaccinations' : new_vaccinations, 'new_vaccinations_smoothed' : new_vaccinations_smoothed, 'total_vaccinations_per_hundred' : total_vaccinations_per_hundred,
            'people_vaccinated_per_hundred' : people_vaccinated_per_hundred, 'people_fully_vaccinated_per_hundred' : people_fully_vaccinated_per_hundred,
            'new_vaccinations_smoothed_per_million' : new_vaccinations_smoothed_per_million, 'stringency_index' : stringency_index, 'population' : population,
            'population_density' : population_density, 'median_age' : median_age, 'aged_65_older' : aged_65_older, 'aged_70_older' : aged_70_older,
            'gdp_per_capita' : gdp_per_capita, 'extreme_poverty' : extreme_poverty, 'cardiovasc_death_rate' : cardiovasc_death_rate, 'diabetes_prevalence' : diabetes_prevalence,
            'female_smokers' : female_smokers, 'male_smokers' : male_smokers, 'handwashing_facilities' : handwashing_facilities, 'hospital_beds_per_thousand' : hospital_beds_per_thousand,
            'life_expectancy' : life_expectancy, 'human_development_index' : human_development
        }
    )
    response = jsonify(
        {
            '_id' : str(id), 'iso_code' : iso_code, 'continent' : continent, 'location' : location, 'date' : date, 'total_cases' : total_cases,
            'new_cases' : new_cases, 'new_cases_smoothed' : new_cases_smoothed, 'total_deaths' : total_deaths, 'new_deaths' : new_deaths,
            'new_deaths_smoothed' : new_deaths_smoothed, 'total_cases_per_million' : total_cases_per_million, 'new_cases_per_million' : new_cases_per_million,
            'new_cases_smoothed_per_million' : new_cases_smoothed_per_million, 'total_deaths_per_million' : total_deaths_per_million,
            'new_deaths_per_million' : new_deaths_per_million, 'new_deaths_smoothed_per_million': new_deaths_smoothed_per_million,
            'reproduction_rate' : reproduction_rate, 'icu_patients' : icu_patients, 'icu_patients_per_million' : icu_patients_per_million,
            'hosp_patients' : hosp_patients, 'hosp_patients_per_million' : hosp_patients_per_million, 'weekly_icu_admissions' : weekly_icu_admissions,
            'weekly_icu_admissions_per_million' : weekly_icu_admissions_per_million, 'weekly_hosp_admissions' : weekly_hosp_admissions,
            'weekly_hosp_admissions_per_million' : weekly_icu_admissions_per_million, 'new_tests' : new_tests, 'total_tests' : total_tests,
            'total_tests_per_thousand' : total_tests_per_thousand, 'new_tests_per_thousand' : new_tests_per_thousand, 'new_tests_smoothed' : new_tests_smoothed,
            'new_tests_smoothed_per_thousand' : new_tests_smoothed_per_thousand, 'positive_rate' : positive_rate, 'tests_per_case' : tests_per_case,
            'tests_units' : tests_units, 'total_vaccinations' : total_vaccinations, 'people_vaccinated' : people_vaccinated, 'people_fully_vaccinated' :people_fully_vaccinated,
            'new_vaccinations' : new_vaccinations, 'new_vaccinations_smoothed' : new_vaccinations_smoothed, 'total_vaccinations_per_hundred' : total_vaccinations_per_hundred,
            'people_vaccinated_per_hundred' : people_vaccinated_per_hundred, 'people_fully_vaccinated_per_hundred' : people_vaccinated_per_hundred,
            'new_vaccinations_smoothed_per_million' : new_vaccinations_smoothed_per_million, 'stringency_index' : stringency_index, 'population' : population,
            'population_density' : population_density, 'median_age' : median_age, 'aged_65_older' : aged_65_older, 'aged_70_older' : aged_70_older,
            'gdp_per_capita' : gdp_per_capita, 'extreme_poverty' : extreme_poverty, 'cardiovasc_death_rate' : cardiovasc_death_rate, 'diabetes_prevalence' : diabetes_prevalence,
            'female_smokers' : female_smokers, 'male_smokers' : male_smokers, 'handwashing_facilities' : handwashing_facilities, 'hospital_beds_per_thousand' : hospital_beds_per_thousand,
            'life_expectancy' : life_expectancy, 'human_development_index' : human_development
        }
    )
    response.status_code = 201
    return response

@app.route('/cases', methods=['GET'])
def get_cases():
    cases = mongo.db.covid2_info_table.find()
    response = json_util.dumps(cases)
    return Response(response, mimetype="application/json")

@app.route('/cases/<population>', methods=['GET'])
def get_case(population):
    case = mongo.db.covid2_info_table.find_one({'population' : population})
    response = json_util.dumps(case)
    return Response(response, mimetype="application/json")

@app.route('/cases/<id>', methods=['DELETE'])
def delete_case():
    mongo.db.covid2_info_table.delete_one({'_id' : ObjectId(id)})
    response = jsonify({'message' : 'Case' + id + ' Deleted Sucessfully '})
    response.status_code = 200
    return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__=="__main__":
    app.run(debug=True)
