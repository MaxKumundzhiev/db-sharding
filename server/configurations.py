from pydantic import BaseModel


class ShardAConfigurations(BaseModel):
    user: str = "postgres"
    password: str = "password"
    host: str = "pgshardA"
    port: str = "5001"
    database: str = "postgres"


class ShardBConfigurations(BaseModel):
    user: str = "postgres"
    password: str = "password"
    host: str = "pgshardB"
    port: str = "5002"
    database: str = "postgres"


class ShardCConfigurations(BaseModel):
    user: str = "postgres"
    password: str = "password"
    host: str = "pgshardC"
    port: str = "5003"
    database: str = "postgres"

