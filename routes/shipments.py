from fastapi import APIRouter
from utils import xml as xl
from fedex.shipments import get_fedex_data

router = APIRouter(
  prefix="/shipments",
  tags=["items"],
  responses={ 404: { "description":"No se encontro" } }
 )


@router.get('/')
def get_shipments_details():
  fedex_data = get_fedex_data()
  return fedex_data



