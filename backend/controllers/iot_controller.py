from fastapi import APIRouter, Request, HTTPException
from core.services.iot_service import process_iot_data
from schemas.IoT_schema import IoTInput

router = APIRouter()


@router.post("/iot/data")
async def iot_data_endpoint(request: Request):
    try:
        # Parse the incoming JSON object
        body = await request.json()
        iot_data = IoTInput(**body)

        # Process the data
        process_iot_data(iot_data.model_dump())

        # Return a JSON response
        return {"message": "IoT data processed successfully"}
    except Exception as e:
        print(f"Error processing IoT data: {e}")
        # Return an error response with JSON
        raise HTTPException(status_code=400, detail={"error": str(e)})