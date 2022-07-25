from xml.dom.minidom import Node
from mimetypes import init
from ..xml import StringToXMLParserBase

class ShipmentsXmlHandler(StringToXMLParserBase):

    def __init__(self, byte_string: str):
        super().__init__(byte_string)
    
    def get_shipment_info(self):
        xml_data = super().parse_string_to_xml()
        rateReplyDetails = xml_data.getElementsByTagName('RateReplyDetails')
        result = []
        for rateReplay in rateReplyDetails:
            data = {}
            rated_shipment_details = rateReplay.getElementsByTagName('RatedShipmentDetails')[1]
            currency = rated_shipment_details.getElementsByTagName('TotalNetFreight')[0].getElementsByTagName('Currency')[0].firstChild.nodeValue
            amount = rated_shipment_details.getElementsByTagName('TotalNetFreight')[0].getElementsByTagName('Amount')[0].firstChild.nodeValue
            service_type = rateReplay.getElementsByTagName('ServiceType')[0].firstChild.nodeValue
            name = service_type.lower().replace('_', ' ')
            data['price'] = amount
            data['currency'] = currency
            data['service_level'] = {
                'name': name,
                'token': service_type
            }
            result.append(data)
        
        return result

        




    
    