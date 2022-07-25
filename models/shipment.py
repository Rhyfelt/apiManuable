from pydantic import BaseModel

class ServiceLevel(BaseModel):
    name:str
    token:str

class Shipment(BaseModel):
    price:float
    currency:str
    service_level:ServiceLevel
    