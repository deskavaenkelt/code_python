from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from ..models.student import (
    error_response_model,
    response_model,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return response_model(new_student, "Student added successfully.")


@router.get("/", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return response_model(students, "Students data retrieved successfully")
    return response_model(students, "Empty list returned")


@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(object_id):
    student = await retrieve_student(object_id)
    if student:
        return response_model(student, "Student data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Student doesn't exist.")


@router.put("/{id}")
async def update_student_data(object_id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(object_id, req)
    if updated_student:
        return response_model(
            "Student with ID: {} name update is successful".format(object_id),
            "Student name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(object_id: str):
    deleted_student = await delete_student(object_id)
    if deleted_student:
        return response_model(
            "Student with ID: {} removed".format(object_id), "Student deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(object_id)
    )
