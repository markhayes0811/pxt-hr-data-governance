from pathlib import Path

# Base project directory for Colab
BASE_DIR = Path("/content/pxt-hr-data-governance")

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
STAGING_DIR = DATA_DIR / "staging"
CURATED_DIR = DATA_DIR / "curated"

METADATA_DIR = BASE_DIR / "metadata"
DOCS_DIR = BASE_DIR / "docs"

RAW_HR_FILE = RAW_DIR / "hr_employees_raw.csv"
STAGING_HR_FILE = STAGING_DIR / "hr_employees_staging.csv"
CURATED_HR_FILE = CURATED_DIR / "hr_employees_curated.csv"
