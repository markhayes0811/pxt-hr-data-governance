import pandas as pd
from .config import RAW_HR_FILE, STAGING_DIR
from .metadata_loader import load_data_quality_rules

def run_rule(df: pd.DataFrame, rule_row: pd.Series) -> float:
    """
    Evaluate a simple Python-based rule expression against the dataframe.

    rule_expression should be a boolean Series expression using 'df'.
    Example: 'df[\"Employee_ID\"].notnull()'

    Returns:
        Passing ratio as a float between 0 and 1.
    """
    expr = rule_row["rule_expression"]
    # NOTE: In a real production system you would parse this safely instead of eval.
    passed = eval(expr)
    return float(passed.mean())

def main():
    df = pd.read_csv(RAW_HR_FILE)
    rules = load_data_quality_rules()

    results = []
    for _, row in rules.iterrows():
        score = run_rule(df, row)
        results.append({
            "rule_id": row["rule_id"],
            "column_name": row["column_name"],
            "dimension": row["dimension"],
            "severity": row["severity"],
            "target_threshold": row["target_threshold"],
            "score": score
        })

    results_df = pd.DataFrame(results)

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    results_df.to_csv(STAGING_DIR / "hr_data_quality_results_raw.csv", index=False)

    print("=== Data Quality Results (Raw) ===")
    print(results_df)

if __name__ == "__main__":
    main()
