import pymongo
import pandas as pd
import os
import csv

def os_any_dir_search(file):
    u=[]
    for p,n,f in os.walk(os.getcwd()):

        for a in f:
            a = str(a)
            if a.endswith(file):
                t=pd.read_csv(p+'/'+file)
                u.append(p+'/'+a)
    return t,u

MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client["covid"]
covid2_info_table = db["owid2"]

csv_file_path = os_any_dir_search('owid-covid-data-1.csv')[1]
csv_file_path_str = "".join(csv_file_path)
data = pd.read_csv(csv_file_path_str)
csvfile = open(csv_file_path_str, 'r')

reader = csv.DictReader(csvfile)
header = ['iso_code','continent','location','date','total_cases','new_cases','new_cases_smoothed','total_deaths','new_deaths','new_deaths_smoothed',
'total_cases_per_million','new_cases_per_million','new_cases_smoothed_per_million','total_deaths_per_million','new_deaths_per_million','new_deaths_smoothed_per_million',
'reproduction_rate','icu_patients','icu_patients_per_million','hosp_patients','hosp_patients_per_million','weekly_icu_admissions','weekly_icu_admissions_per_million',
'weekly_hosp_admissions','weekly_hosp_admissions_per_million','new_tests','total_tests','total_tests_per_thousand','new_tests_per_thousand','new_tests_smoothed',
'new_tests_smoothed_per_thousand','positive_rate','tests_per_case','tests_units','total_vaccinations','people_vaccinated','people_fully_vaccinated',
'new_vaccinations','new_vaccinations_smoothed','total_vaccinations_per_hundred','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred',
'new_vaccinations_smoothed_per_million','stringency_index','population','population_density','median_age','aged_65_older','aged_70_older','gdp_per_capita',
'extreme_poverty','cardiovasc_death_rate','diabetes_prevalence','female_smokers','male_smokers','handwashing_facilities','hospital_beds_per_thousand',
'life_expectancy','human_development_index']

for each in reader:
    row={}
    for field in header:
        row[field] = each[field]
    db.covid2_info_table.insert_one(row)

print(data)
