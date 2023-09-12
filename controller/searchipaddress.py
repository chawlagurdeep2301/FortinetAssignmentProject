from flask_restful import Resource, request
from flask import current_app, jsonify, make_response


class SearchIpAddressResource(Resource):

    def get(self):
        if request.args and request.args.get('param'):
            request_data = eval(request.args.get('param'))
        else:
            request_data = eval(request.data.decode())
        ipaddress_to_search = request_data.get('ip')
        ip_sp_mapping = current_app.config.get("IP_SP_MAPPING")
        prepare_result = []
        for ipaddress in ipaddress_to_search:
            ipexists = False
            for key in ip_sp_mapping.keys():
                if key.__contains__(ipaddress):
                    prepare_result.append({"ServiceProvider": ip_sp_mapping.get(key, "IP Not Found"),
                                           "CloudProvider": current_app.config.get("IP_CLOUD_MAPPING").get(ipaddress,
                                                                                                          "No Cloud Mapped")})
                    ipexists = True
            if not ipexists:
                 prepare_result.append({"ServiceProvider": "IP Not Found",
                                        "CloudProvider":"No Cloud Mapped"})

        return make_response(jsonify(
            {
                "status": "Success",
                "response_data": prepare_result
            }), 200)
