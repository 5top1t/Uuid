
from uuid import (UUID, uuid1, uuid3, uuid4, uuid5)
from lib import (node, specification, timestamp)

import json


namespace = 'Hack.Diversity.com'
urn = UUID('787bce4a-6865-11ec-a24f-38f9d34e0805')
urn = uuid3(namespace, "hello")

timestamp_dict = timestamp.get_datetime_dict(urn)
spec_dict = specification.get_specification_dict(urn)
node_dict = node.get_node_dict(spec_dict.get('version'), namespace)

structure_dict = {
    "uuid": urn.urn,
    "node": node_dict,
    "spec": spec_dict,
    "datetime": timestamp_dict,

}
structure_json = json.dumps(structure_dict, indent=4)

print(structure_json)
