from flask_restful import Resource
from util.parse_json import ParseJsonFile
from model.ClassTagModel import ClassTagModel
from model.ClassPrefixDataModel import ClassPrefixModel


class CloudTagResource(Resource):

    def get(self):
        pass

    def post(self):
        parse_json_file = ParseJsonFile("./prefixes.json")
        parse_json_file.parse_json()
        result = parse_json_file.prepare_class_tag_data()
        service_provider_tag_number_mapping = dict()
        for r_dict in result:
            ctm = ClassTagModel(**r_dict)
            ctm.save()
            service_provider_tag_number_mapping[r_dict['serviceProvider']] = ctm.tagNumber

        print(service_provider_tag_number_mapping)
        result = parse_json_file.prepare_prefix_data()
        for r_dict in result:
            r_dict['tagNumber'] = service_provider_tag_number_mapping.get(r_dict['serviceProvider'])
            ctm = ClassPrefixModel(**r_dict)
            ctm.save()

        return " Data Saved Successfully"
