from flask import Blueprint

health_blueprint = Blueprint('health', __name__)


@health_blueprint.route("/healthcheck", methods=['GET'])
def healthcheck():
    """
        health check
        ---
        tags:
          - health
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        responses:
          200:
            description: successfully.
        """
    return {"code": 200, "data": {}}


@health_blueprint.route("/", methods=['GET'])
def home_index():
    """
        home
        ---
        tags:
          - health
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        responses:
          200:
            description: successfully.
        """
    return {}
