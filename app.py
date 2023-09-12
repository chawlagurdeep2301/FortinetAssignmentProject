import requests
from flask import Flask, session, send_from_directory
from flask_restful import Api, request
from controller.cloudtagresource import CloudTagResource
from util.parse_json import ParseJsonFile
from controller.searchipaddress import SearchIpAddressResource
import configuration.database

app = Flask(__name__)
api = Api(app)
JSON_DATA = dict()


@app.route('/')
def welcome_page():
    return "Welcome to Fortinet IP Search Engine ..."


@app.route('/searchips')
def search_single_ip():
    print("Calling Search Single IP ......")
    param = {'param': str(request.json)}
    data = requests.get('http://127.0.0.1:8080/api/v1/search-ipaddress', param)
    return data.text


def load_json():
    parse_json_file = ParseJsonFile("./prefixes.json")
    parse_json_file.parse_json()
    app.config["JSON_DATA"] = parse_json_file.data
    app.config["IP_SP_MAPPING"] = parse_json_file.prepare_ip_sp_data_mapping()
    app.config["IP_CLOUD_MAPPING"] = parse_json_file.prepare_ip_cloud_data_mapping()


api.add_resource(CloudTagResource, '/api/v1/storecloudtagdata')
api.add_resource(SearchIpAddressResource, '/api/v1/search-ipaddress')

if __name__ == "__main__":
    load_json()
    app.run(port=8080)
