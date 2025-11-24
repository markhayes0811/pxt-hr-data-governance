import pandas as pd
from .config import DOCS_DIR

def build_lineage() -> pd.DataFrame:
    """
    Build a simple lineage mapping from raw to curated.

    Columns:
        source_table, source_column, target_table, target_column, transformation
    """
    lineage_rows = [
        [
            "hr_employees_raw",
            "Employee_ID",
            "hr_employees_curated",
            "Employee_ID",
            "deduplicated on Employee_ID",
        ],
        [
            "hr_employees_raw",
            "Department",
            "hr_employees_curated",
            "Department",
            "standardized labels (HR/IT/etc.)",
        ],
        [
            "hr_employees_raw",
            "Hire_Date",
            "hr_employees_curated",
            "Hire_Date",
            "parsed to datetime, invalid reset to NaT",
        ],
        [
            "hr_employees_raw",
            "Termination_Date",
            "hr_employees_curated",
            "Termination_Date",
            "parsed to datetime, invalid/future/early fixed or set to NaT",
        ],
    ]
    df = pd.DataFrame(
        lineage_rows,
        columns=[
            "source_table",
            "source_column",
            "target_table",
            "target_column",
            "transformation",
        ],
    )
    return df

def main():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    lineage_df = build_lineage()
    out_path = DOCS_DIR / "hr_lineage_table.csv"
    lineage_df.to_csv(out_path, index=False)

    print("=== HR Lineage Table ===")
    print(lineage_df)
    print(f"\nSaved lineage table to: {out_path}")

if __name__ == "__main__":
    main()
