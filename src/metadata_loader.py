import pandas as pd
from .config import METADATA_DIR

def load_business_metadata() -> pd.DataFrame:
    """Load business metadata definitions."""
    return pd.read_csv(METADATA_DIR / "business_metadata.csv")

def load_technical_metadata() -> pd.DataFrame:
    """Load technical metadata for tables/columns."""
    return pd.read_csv(METADATA_DIR / "technical_metadata.csv")

def load_data_quality_rules() -> pd.DataFrame:
    """Load data quality rules configuration."""
    return pd.read_csv(METADATA_DIR / "data_quality_rules.csv")

def load_domain_owners() -> pd.DataFrame:
    """Load domain owners / stewards."""
    return pd.read_csv(METADATA_DIR / "domain_owners.csv")

if __name__ == "__main__":
    print("Business metadata:")
    try:
        print(load_business_metadata().head())
    except FileNotFoundError:
        print("business_metadata.csv not found yet.")
