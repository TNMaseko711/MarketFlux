from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MarketFlux API"
    app_version: str = "0.1.0"
    symbols: list[str] = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    update_interval_seconds: float = 0.5

    model_config = SettingsConfigDict(env_file=".env", env_prefix="MARKETFLUX_")


settings = Settings()
