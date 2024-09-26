from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from database.helper_function import generate_unique_id, plat_graph_function
from model.report_model import ReportCreation, VitalType, ReportORMModel
from model.database_model import Report 

routes = APIRouter()

@routes.post("/add_report", response_description="Add report")
async def add_report_of_patient(request:Request, payload: ReportCreation, db: Session = Depends(get_db)):
    """
        This API is used to insert the report of a patient
    """
    try:
        if not payload.bp and not payload.bodytemp and not payload.heartrate:
            raise HTTPException(status_code=400, detail="At least one vital sign must be provided.")

        created_at = payload.created_at

        new_reports = []

        if payload.bodytemp is not None:
            bt_payload = {
                "id": generate_unique_id(),
                "type": VitalType.BODYTEMPERATURE,
                "value": str(payload.bodytemp),
                "patient_id": payload.patient_id,
                "created_at": created_at
            }
            new_reports.append(bt_payload)

        if payload.bp is not None:
            bp_payload = {
                "id": generate_unique_id(),
                "type": VitalType.BP,
                "value": str(payload.bp),
                "patient_id": payload.patient_id,
                "created_at": created_at
            }
            new_reports.append(bp_payload)

        if payload.heartrate is not None:
            hr_payload = {
                "id": generate_unique_id(),
                "type": VitalType.HEARTRATE,
                "value": str(payload.heartrate),
                "patient_id": payload.patient_id,
                "created_at": created_at
            }
            new_reports.append(hr_payload)

        # Add each report to the database
        for report in new_reports:
            new_report = Report(**report)  # Adjust this line if needed based on your Report model
            db.add(new_report)

        db.commit()
        return {"message": "Successfully inserted"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Please try again {e}!")


@routes.get("/{patient_id}", response_description="Get the report of the patient")
async def get_patient_detail(request: Request, patient_id, db: Session = Depends(get_db)):
    """
        This API is used to get the patient details
    """
    # try:
    patient_detail = db.query(Report).filter_by(patient_id=patient_id, type="body temperature").all()
    report_models = [ReportORMModel.from_orm(r).dict() for r in patient_detail]
    plat_graph_function(report_models)
    return {"message": "Report saved successfully!."}
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Please try again {e}!")
