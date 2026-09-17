# Superstore Sales Analysis

End-to-end retail analytics on a 9,994-row Superstore dataset — covering data cleaning, feature engineering, SQL business querying, and visual insight generation across Python, SQL and Power BI.

The headline finding: the business is profitable overall at a **12.5% margin**, but **18.7% of line items lose money**, and almost all of that loss is manufactured by its own discounting policy.

---

## Dataset

| | |
|---|---|
| Rows | 9,994 line items |
| Orders | 5,009 |
| Customers | 793 |
| Period | Jan 2014 – Dec 2017 |
| Total Sales | $2,297,201 |
| Total Profit | $286,397 |
| Profit Margin | 12.47% |

Source: `Sample - Superstore.csv` (21 columns — order, customer, product, geography, sales, quantity, discount, profit)

---

## Key Findings

### 1. Discounting above 20% destroys profit
Average profit per line item collapses the moment discounts pass 20%, and never recovers:

| Discount Band | Orders | Avg Profit | Total Profit |
|---|---:|---:|---:|
| No discount | 4,798 | **+$66.90** | +$320,988 |
| 1–20% | 3,803 | **+$26.50** | +$100,785 |
| 21–40% | 460 | **−$77.86** | −$35,817 |
| 41–60% | 215 | **−$134.62** | −$28,944 |
| 60%+ | 718 | **−$98.35** | −$70,614 |

Discounted-above-20% orders account for roughly **$135K in destroyed profit** — nearly half of the company's total annual profit.

### 2. Two sub-categories are actively loss-making

| Sub-Category | Total Profit |
|---|---:|
| Tables | −$17,725 |
| Bookcases | −$3,473 |
| Supplies | −$1,189 |

Tables alone wipe out 6% of company profit. Furniture as a category earns just $18,451 against Technology's $145,455 — despite comparable sales volume.

### 3. Central region underperforms
West and East drive profit; Central generates $501K in sales but only $39.7K profit — a 7.9% margin versus West's 14.9%.

| Region | Sales | Profit | Margin |
|---|---:|---:|---:|
| West | $725,458 | $108,418 | 14.9% |
| East | $678,781 | $91,523 | 13.5% |
| South | $391,722 | $46,749 | 11.9% |
| Central | $501,240 | $39,706 | 7.9% |

---

## Repository Contents

| File | Purpose |
|---|---|
| `superstore_eda.py` | Data loading, cleaning, feature engineering, and six business-insight charts |
| `superstore_analysis.sql` | Five analytical SQL queries (KPI summary, regional profit, sub-category ranking, discount banding with `CASE WHEN`, top-10 customers) |
| `Sample - Superstore.csv` | Source dataset |

---

## Techniques Used

**Feature engineering** — derived `Profit Margin`, `Days to Ship`, `Is Loss` flag, `Profit per Unit`, `Order Month` period, and a binned `Discount Band` using `pd.cut()`.

**SQL** — aggregate KPIs with `ROUND`/`COUNT(DISTINCT)`, `GROUP BY` breakdowns, `CASE WHEN` discount bucketing, and ranked customer profitability.

**Visualisation** — six charts including conditional colour-coding (red for negative profit) on the sub-category and discount-band plots to make loss centres immediately visible.

---

## Tech Stack

`Python` · `Pandas` · `Matplotlib` · `Seaborn` · `SQL (SQLite)` · `Power BI` · `Excel`

---

## Run Locally

```bash
git clone https://github.com/Himanshi252005/Superstore-Sales-Analysis.git
cd Superstore-Sales-Analysis
pip install pandas matplotlib seaborn
python superstore_eda.py
```

To run the SQL, load the CSV into a SQLite table named `Superstore`:

```bash
sqlite3 superstore.db
.mode csv
.import "Sample - Superstore.csv" Superstore
.read superstore_analysis.sql
```

---

## Business Recommendations

1. **Cap discounts at 20%.** Every band above it is loss-making on average. This single change recovers an estimated $135K.
2. **Review or drop Tables.** The sub-category has never been profitable and drags Furniture's overall margin down.
3. **Audit Central region pricing.** Its margin is half the West's on comparable volume — likely a discounting or product-mix problem, not a demand one.

---

**Author:** Himanshi Rathore · [LinkedIn](https://www.linkedin.com/in/himanshi-rathore-hr2520) · [GitHub](https://github.com/Himanshi252005)
