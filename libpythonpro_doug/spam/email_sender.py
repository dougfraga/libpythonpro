class Sender(object):
    def send(self, shipper, recipient, title, body):
        if '@' not in shipper:
            raise InvalidEmail(f'Invalid shipper address: {shipper}')
        return shipper


class InvalidEmail(Exception):
    pass
