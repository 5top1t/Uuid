from uuid import UUID

def _get_variant(urn: UUID):
    variant = urn.clock_seq_hi_variant >> 4
    
    if 0x0 <= variant and 0x7 >= variant:
        return 0
    elif 0x8 <= variant and 0xb >= variant:
        return 1
    elif 0xc <= variant and 0xd >= variant:
        return 2
    else:
        return 3

def _get_version(urn: UUID):
    return urn.time_hi_version >> 12


def get_specification_dict(urn: UUID):
    urn_variant = _get_variant(urn)
    urn_version = _get_version(urn)

    return {
        "variant": urn_variant,
        "version": urn_version,
    }
