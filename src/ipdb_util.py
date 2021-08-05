import ipdb
db_client = ipdb.District("./data/ipip.ipdb")


def find_ip_district_info(ip):
    district_info = db_client.find_info(ip, "CN")
    return district_info._map
