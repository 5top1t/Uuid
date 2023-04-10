
from uuid import (UUID, uuid1, uuid3, uuid4, uuid5)
from lib import (node, specification, timestamp)

import json

def get_uuid_components(urn: UUID, name=""):
    timestamp_dict = timestamp.get_datetime_dict(urn)
    spec_dict = specification.get_specification_dict(urn)
    node_dict = node.get_node_dict(urn, spec_dict.get('version'), name)

    uuid_components_dict = {
        "uuid": urn.urn,
        "node": node_dict,
        "spec": spec_dict,
        "datetime": timestamp_dict,
    }
    
    return uuid_components_dict
    
        

name = "demo"
hack_diversity_namespace = uuid1()
urn_1 = hack_diversity_namespace
urn_3 = uuid3(hack_diversity_namespace, name)
urn_4 = uuid4()
urn_5 = uuid5(hack_diversity_namespace, name)
urn_slides = UUID("787bce4a-6865-11ec-a24f-38f9d34e0805")
urn_notion = UUID("dbd0512b3aa74044a18d3326e0fbcae8")

urn = urn_notion
uuid_components_json = json.dumps(get_uuid_components(urn, name), indent=4)
print(uuid_components_json)
