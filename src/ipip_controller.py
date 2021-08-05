from flask import Blueprint, request, jsonify
from src.ipdb_util import find_ip_district_info

ipip_blueprint = Blueprint('ipip', __name__)


@ipip_blueprint.route("/api/ip-info", methods=['GET'])
def analytic_contents():
    """
        IP 信息
        ---
        tags:
          - IpInfo
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: query
            name: ip
            schema:
              type: string
            description: ip
        responses:
          200:
            description:  Get IpInfo successfully.
        """

    ip = request.args.get('ip', default="0.0.0.0")
    ip_info = find_ip_district_info(ip)
    return jsonify({"code": 200, "data": ip_info})
