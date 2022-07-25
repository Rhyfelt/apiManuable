from mimetypes import init
import xml.dom.minidom as XM




class StringToXMLParserBase():

    b_string = ""

    def __init__(self,byte_string:str):
        self.b_string = byte_string
    
    def parse_string_to_xml(self):
        root = XM.parseString(self.b_string)
        return root
        



   
