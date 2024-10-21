from uhashring import HashRing

from configurations import (
    ShardAConfigurations,
    ShardBConfigurations,
    ShardCConfigurations
)


def get_hash_ring() -> HashRing:
    """Returns an object, which implements consistent hashing which take available servers as options."""
    try:
        return HashRing(
            nodes=[ShardAConfigurations.host, ShardBConfigurations.host, ShardCConfigurations.host]
        )
    except Exception as e:
        raise e
    