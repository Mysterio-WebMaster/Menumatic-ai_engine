from flask import Blueprint, request
from utils.response import success, error
from services.menumatic_backend_service import MenumaticBackendService
from services.recommendation_service import RecommendationService

recommend_bp = Blueprint("recommend", __name__)

service = MenumaticBackendService()
recommendation_service = RecommendationService()

# Fetch from DB once at startup and build TF-IDF matrix
menu_items = service.getAllMenu()
recommendation_service.build(menu_items)


@recommend_bp.route("/health", methods=["GET"])
def test():
    try:
        return success(data="Healthy", message="Engine is healthy", status=200)
    except Exception as e:
        return error(message=str(e), status=500)


@recommend_bp.route("/recommend/search", methods=["GET"])
def search():
    try:
        query = request.args.get("q", "").strip()

        if not query:
            return error(message="Query parameter 'q' is required", status=400)

        results = recommendation_service.recommend(query, top_n=10)

        return success(data=results, message="Recommendations fetched", status=200)

    except Exception as e:
        return error(message=str(e), status=500)
