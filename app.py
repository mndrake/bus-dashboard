from flask import Flask, render_template, jsonify
import methods


direction_colors = [
    {'text': 'North', 'id': 4, 'color': '#BA48AA'},
    {'text': 'South', 'id': 1, 'color': '#595490'},
    {'text': 'East', 'id': 2, 'color': '#527525'},
    {'text': 'West', 'id': 3, 'color': '#A93F35'},
]


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

bus_routes = methods.BusRoutes()


@app.route('/')
def index():
    return render_template('index.html', direction_colors=direction_colors)


@app.route('/api/route-numbers')
def route_numbers():
    return jsonify(bus_routes.get_route_numbers())


@app.route('/api/route-info/<int:route_number>')
def route_info(route_number):
    return jsonify(bus_routes.get_route_info(route_number, refresh=True))


if __name__ == '__main__':
    app.run()

