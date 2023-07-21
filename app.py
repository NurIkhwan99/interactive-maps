from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_placemark', methods=['POST'])
def add_placemark():
    name = request.form.get('name')
    description = request.form.get('description')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    return "Placemark added successfully"

@app.route('/placemark/<placemark_id>')
def placemark_details(placemark_id):
    placemark = {"name": "Example Place", "description": "This is an example place."}
    return render_template('details.html', placemark=placemark)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    geocode_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json'
    response = requests.get(geocode_url, params={'access_token': 'pk.eyJ1IjoiaWtod2FuLTk5IiwiYSI6ImNsazhiZTh4ODBsOWozdHA2eHB0ZGw3bGkifQ.Q1Yoze1MXeh8XcnlyOIJVg'})
    data = response.json()
    
    search_results = []
    for feature in data['features']:
        result = {
            'name': feature['place_name'],
            'latitude': feature['center'][1],
            'longitude': feature['center'][0]
        }
        search_results.append(result)

    return jsonify({"results": search_results})

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        pass
    return render_template('settings.html')

@app.route('/save_map', methods=['POST'])
def save_map():
    return "Map saved successfully"

@app.route('/load_map/<map_id>')
def load_map(map_id):
    return render_template('loaded_map.html')

if __name__ == '__main__':
    app.run(debug=True)
