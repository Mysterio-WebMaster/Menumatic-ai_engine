from flask import Blueprint
from utils.response import success, error

recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/test", methods=["GET"])
def test():
    try:
        return success(data="test", message="Test is success", status=200)
    except Exception as e:
        return error(message=str(e), status=500)
