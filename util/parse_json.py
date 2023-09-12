import json


class ParseJsonFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def parse_json(self):
        with open(self.filepath, "r") as f:
            data = json.loads(f.read())
            self.data = data

    def prepare_class_tag_data(self):
        result = []
        for key in self.data.keys():
            dict_val = dict()
            dict_val['serviceProvider'] = key
            key_value = self.data.get(key)[0].get('tags')
            dict_val['serviceProvider'] = key
            dict_val['cloudProvider'] = key_value[0]
            if len(key_value) > 1:
                dict_val['cloudProviderName'] = key_value[1]
            result.append(dict_val)

        return result

    def prepare_prefix_data(self):
        result = []
        for key in self.data.keys():
            for data in self.data.get(key):
                prefix_value = data.get('prefixes')
                for ip in prefix_value:
                    dict_val = dict()
                    dict_val['serviceProvider'] = key
                    dict_val['ip_add'] = ip
                    result.append(dict_val)

        return result

    def prepare_ip_sp_data_mapping(self):
        result_dict = dict()
        for key in self.data.keys():
            for data in self.data.get(key):
                for item in data.items():
                    if item[0] == "prefixes":
                        for ip in item[1]:
                            result_dict[ip + "_" + key] = key

        return result_dict

    def prepare_ip_cloud_data_mapping(self):
        result_dict = dict()
        for key in self.data.keys():
            for data in self.data.get(key):
                item_data = []
                for item in data.items():
                    if item[0] == "prefixes":
                        item_data = item[1]
                        continue
                    if item[0] == "tags":
                        for ip in item_data:
                            if len(item[1]) > 1:
                                result_dict[ip] = item[1][1]
                            else:
                                result_dict[ip] = "No Cloud Mapped"
        return result_dict
