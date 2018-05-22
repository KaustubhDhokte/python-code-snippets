from taskflow import task
from taskflow.patterns import linear_flow as lf
from taskflow.patterns import unordered_flow as uf
from taskflow.patterns import graph_flow as gf
from taskflow import engines


class ValidateWorkload(task.Task):
    def execute(self, *args, **kwargs):
        print "Validating Workload"

    def revert(self, *args, **kwargs):
        print "reverting Workload validation"


class ValidateRepo(task.Task):
    def execute(self, *args, **kwargs):
        print "Validating backup repository"

    def revert(self, *args, **kwargs):
        print "reverting repository validation"


class SnapshotVMFlavour(task.Task):
    def execute(self, *args, **kwargs):
        print "Snapshotting VM Flavour"

    def revert(self, *args, **kwargs):
        print "Reverting Snapshot VM Flavour"


class SnapshotVMDisk(task.Task):
    def execute(self, *args, **kwargs):
        print "Snapshotting VM disk"

    def revert(self, *args, **kwargs):
        print "Reverting Snapshot VM disk"


class SnapshotVMNW(task.Task):
    def execute(self, *args, **kwargs):
        print "Snapshotting VM NW"
        print c
        #while True:
        #    print "VMNW"

    def revert(self, *args, **kwargs):
        print "Reverting Snapshot VM NW"

class TransportSS(task.Task):
    def execute(self, *args, **kwargs):
        print "Transporting Snapshot"

    def revert(self, *args, **kwargs):
        print "Reverting Transport snapshot"


class UpdateSSMetadata(task.Task):
    def execute(self, *args, **kwargs):
        print "Updating snapshot metadata to db"

    def revert(self, *args, **kwargs):
        print "Reverting snapshot metadata to db"


class NotifyAdmin(task.Task):
    def execute(self, *args, **kwargs):
        print "Notifying Admin"

    def revert(self, *args, **kwargs):
        print "Reverting Notifying Admin"


def PreSnapshot():
    presnap = uf.Flow("PreSS")
    presnap.add(ValidateWorkload())
    presnap.add(ValidateRepo())
    return presnap


def Snapshot():
    snapshot = lf.Flow("Snapshot")
    snapshot.add(SnapshotVMFlavour())
    snapshot.add(SnapshotVMDisk())
    snapshot.add(SnapshotVMNW())
    snapshot.add(TransportSS())
    return snapshot

def PostSnapshot():
    postss = lf.Flow("PostSS")
    postss.add(UpdateSSMetadata())
    postss.add(NotifyAdmin())
    return postss


class Workflow(object):
    def __init__(self):
        self._flow = None

class SerialFlow(object):
    def __init__(self):
        self._flow  = lf.Flow("Serial")
        self._flow.add(PreSnapshot())
        self._flow.add(Snapshot())
        self._flow.add(PostSnapshot())

    def execute(self):
        engines.run(self._flow)

try:
    SerialFlow().execute()
except Exception as ex:
    pass