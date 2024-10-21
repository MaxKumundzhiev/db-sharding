from configurations import (
    ShardAConfigurations,
    ShardBConfigurations,
    ShardCConfigurations
)


pools = {
        ShardAConfigurations.host: POOL_A,
        ShardBConfigurations.host: POOL_B,
        ShardCConfigurations.host: POOL_C
    }

def get_pool(shard):
    return pools.get(shard, POOL_C)