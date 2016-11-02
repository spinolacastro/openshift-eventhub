from azure.servicebus import ServiceBusService, Message
import sys
import json
import os

key_name = os.environ['key_name'] # SharedAccessKeyName from Azure portal
key_value = os.environ['key_value'] # SharedAccessKey from Azure portal
sbs = ServiceBusService('getupevents',
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)

def send(namespace, id, time, reason, message, count):
    message = {
            "time": time,
            "namespace": namespace,
            "id": id,
            "reason": reason,
            "message": message,
            "eventcount": count
        }
    print(json.dumps(message))
    return sbs.send_event('toanalytics', json.dumps(message))

try:
    namespace, id, time, reason, message, count = sys.argv[1:]
    print send(namespace, id, time, reason, message, count)
except ValueError:
    print "Use: {} [reason] [message] [count]".format(argv[0])
    sys.exit(0)
