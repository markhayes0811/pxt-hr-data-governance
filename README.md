# Enterprise HR Data Governance & Quality Framework

This project simulates what a **PXT (People Experience & Technology)** data governance / metadata engineer would build for HR data at a large bank.

It demonstrates how to:
- Develop and maintain **standardized data definitions** and **comprehensive metadata**
- Analyze HR data sets to identify **data quality issues** and implement **cleansing strategies**
- Create and document **data lineage** from raw source to curated analytics layer
- Build and maintain **high-quality metadata** for **discoverability, understanding, and governance**
- Support **data integration and migration** across layers (raw → staging → curated)
- Ensure **data quality, integrity, and policy compliance** within the HR data domain
- Act as **subject matter expert** for HR employee data

---

## 1. Business Scenario

You are the data governance lead for the **HR / People** domain (PXT) at a large financial institution.

The HR analytics team wants to trust metrics like:
- Headcount and turnover
- Internal mobility
- Diversity and inclusion
- Attrition risk

But the underlying HR data has issues:
- Inconsistent department names  
- Missing manager IDs  
- Invalid dates (future start dates, end before start)  
- Duplicated employee records  

This project shows how you would **industrialize** this data:
1. Define clear **business and technical metadata**
2. **Profile** raw data and quantify quality issues
3. Apply **data quality rules** and **cleansing**
4. Document **data lineage**
5. Expose **data quality scores and metadata** to stakeholders

---

## 2. Repository Structure

See high-level structure:

```text
data/         # raw, staging, curated HR datasets
metadata/     # business & technical metadata, quality rules, domain owners
src/          # Python code for profiling, quality checks, cleansing, lineage
notebooks/    # analysis notebooks showing profiling and before/after
docs/         # lineage diagram, governance playbook, case study
dashboard/    # Power BI dashboard + optional Streamlit app
