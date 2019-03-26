# Internal
from src.data_soruce.zmq_client import ZmqClient
from src.domain.disk_space_observer.disk_space_observer import DiskSpaceObserver


diskSpaceObserver = DiskSpaceObserver()

client = ZmqClient()
client.connect()

while True:

    status = diskSpaceObserver.check()
    client.send(status)