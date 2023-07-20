from flask import Blueprint
from app.models.Department import Department

department = Blueprint("department", __name__, url_prefix="/departments")


@department.get("/")
def get_all_departments():
    departments = Department.query.all()
    print(departments)
    return []
