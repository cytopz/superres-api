class Image():
    """helper class to parse blob image
    """

    def __init__(self, b64: str):
        self.raw_header, self.b64 = b64.split(',')
        self.__parse_header(self.raw_header)
    
    def __parse_header(self, header: str):
        mime, enc = header.split(';')
        self.ext = mime[5:].split('/')[1]
        self.encoding = enc
