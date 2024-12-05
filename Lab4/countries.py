from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['CKCS145']
collection = db['Country']


@dataclass
class Country:
    Name: str
    Population: str
    Continent: str
    Area: str
    GDP: str
    NaturalHazards: List[str]

    @classmethod
    def from_dict(cls, data):
        # Exclude '_id' and any other unexpected fields
        relevant_data = {
            key: value for key, value in data.items()
            if key in cls.__annotations__
        }
        return cls(**relevant_data)

    @property
    def population_value(self):
        return int(self.Population.split()[0])


@app.route('/countries-with-hazards', methods=['GET', 'POST'])
def get_countries_with_hazards():
    hazards = request.json.get('hazards', [])

    if not hazards:
        return jsonify({"error": "No hazards provided"}), 400

    query = {"NaturalHazards": {"$all": hazards}}

    countries = collection.find(query)

    result = dumps(countries)

    return result, 200


@app.route('/count-countries/<continent>', methods=['GET'])
def count_countries_in_continent(continent):
    count = collection.count_documents({"Continent": continent})

    return jsonify({
        "continent": continent,
        "count": count
    }), 200


@app.route('/countries-by-population', methods=['GET', 'POST'])
def get_countries_by_population():
    min_pop = request.json.get('min_population')
    max_pop = request.json.get('max_population')

    if min_pop is None or max_pop is None:
        return jsonify({"error": "Both min_population and max_population must be provided"}), 400

    result_countries = []

    for country_data in collection.find():
        country = Country.from_dict(country_data)
        if min_pop <= country.population_value <= max_pop:
            result_countries.append(country_data)

    result = dumps(result_countries)

    return result, 200


if __name__ == '__main__':
    app.run(debug=True)