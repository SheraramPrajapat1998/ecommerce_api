import datetime, uuid

def generate_uuid():
    return datetime.datetime.now().strftime("%Y%m-%d%H-%M%S-%f-") + str(uuid.uuid4())