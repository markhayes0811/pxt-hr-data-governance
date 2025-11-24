import pandas as pd
from .config import RAW_HR_FILE, STAGING_DIR
from .metadata_loader import load_business_metadata

def basic_profile(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a simple data profile:
    - dtype
    - non-null count
    - null count
    - distinct count
    """
    profile = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str).values,
        "non_null_count": df.notnull().sum().values,
        "null_count": df.isnull().sum().values,
        "distinct_count": df.nunique().values
    })
    return profile

def main():
    # Load raw HR data
    df_raw = pd.read_csv(RAW_HR_FILE)

    # Basic profile
    profile = basic_profile(df_raw)

    # Ensure staging dir exists
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    profile.to_csv(STAGING_DIR / "hr_profile_raw.csv", index=False)

    print("=== Raw HR Data Profile ===")
    print(profile)

    # Optional: enrich with business metadata
    try:
        business_meta = load_business_metadata()
        merged = profile.merge(
            business_meta,
            left_on="column",
            right_on="column_name",
            how="left"
        )
        merged.to_csv(STAGING_DIR / "hr_profile_with_metadata.csv", index=False)
        print("\n=== Profile joined with business metadata ===")
        print(merged.head())
    except FileNotFoundError:
        print("\nBusiness metadata not found, skipping enriched profile.")

if __name__ == "__main__":
    main()
