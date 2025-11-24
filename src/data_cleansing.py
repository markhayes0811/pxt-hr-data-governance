import pandas as pd
from .config import (
    RAW_HR_FILE,
    STAGING_HR_FILE,
    CURATED_HR_FILE,
    STAGING_DIR,
    CURATED_DIR,
)

def clean_departments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize department labels:
    - 'Human Resources', 'H.R.', 'Hr' -> 'HR'
    - 'Information Technology', 'IT Dept' -> 'IT'
    """
    mapping = {
        "Human Resources": "HR",
        "H.R.": "HR",
        "Hr": "HR",
        "Information Technology": "IT",
        "IT Dept": "IT",
    }
    if "Department" in df.columns:
        df["Department"] = df["Department"].replace(mapping)
    return df

def fix_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse dates and fix impossible values such as:
    - Termination date before hire date -> set Termination_Date to NaT
    """
    if "Hire_Date" in df.columns:
        df["Hire_Date"] = pd.to_datetime(df["Hire_Date"], errors="coerce")
    if "Termination_Date" in df.columns:
        df["Termination_Date"] = pd.to_datetime(df["Termination_Date"], errors="coerce")
        # Ensure no Termination_Date before Hire_Date
        if "Hire_Date" in df.columns:
            mask = df["Termination_Date"] < df["Hire_Date"]
            df.loc[mask, "Termination_Date"] = pd.NaT
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate employee rows based on Employee_ID."""
    if "Employee_ID" in df.columns:
        return df.drop_duplicates(subset=["Employee_ID"])
    return df.drop_duplicates()

def main():
    df_raw = pd.read_csv(RAW_HR_FILE)

    df_stage = df_raw.copy()
    df_stage = clean_departments(df_stage)
    df_stage = fix_dates(df_stage)
    df_stage = drop_duplicates(df_stage)

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    CURATED_DIR.mkdir(parents=True, exist_ok=True)

    df_stage.to_csv(STAGING_HR_FILE, index=False)
    df_stage.to_csv(CURATED_HR_FILE, index=False)

    print("Saved staging and curated HR data:")
    print(f" - Staging: {STAGING_HR_FILE}")
    print(f" - Curated: {CURATED_HR_FILE}")
    print("\nSample of curated data:")
    print(df_stage.head())

if __name__ == "__main__":
    main()
