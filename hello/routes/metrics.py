from flask import Blueprint, Response
from hello.models.users import User

"""
This blueprint exposes a /metrics Prometheus metrics exporter endpoint 
"""

bp = Blueprint("metrics", __name__)

@bp.route("/metrics", methods=["GET"])
def metrics() -> Response:
    total_users = User.query.count()
    metrics = f"""\
total_users{{job="hello"}} {total_users}
"""
    return Response(metrics, mimetype="text/plain")
