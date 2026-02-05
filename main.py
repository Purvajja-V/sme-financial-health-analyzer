from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io

app = FastAPI(title="AI-Based Financial Assessment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        df.columns = [c.strip() for c in df.columns]

        revenue_keywords = ["sales", "revenue", "gross"]
        expense_keywords = ["expense", "cogs", "discount"]
        profit_keywords = ["profit"]

        revenue_cols = []
        expense_cols = []
        profit_cols = []

        for col in df.columns:
            lname = col.lower()
            if any(k in lname for k in revenue_keywords):
                revenue_cols.append(col)
            if any(k in lname for k in expense_keywords):
                expense_cols.append(col)
            if any(k in lname for k in profit_keywords):
                profit_cols.append(col)

        total_revenue = df[revenue_cols].sum(numeric_only=True).sum() if revenue_cols else 0
        total_expense = df[expense_cols].sum(numeric_only=True).sum() if expense_cols else 0

        if profit_cols:
            profit = df[profit_cols].sum(numeric_only=True).sum()
        else:
            profit = total_revenue - total_expense

        if total_revenue <= 0:
            score = 0
        else:
            profit_margin = profit / total_revenue
            if profit_margin > 0.3:
                score = 90
            elif profit_margin > 0.1:
                score = 40
            elif profit_margin >= 0:
                score = 20
            else:
                score = 5

        if score >= 70:
            status = "GOOD"
            summary = "The business demonstrates strong financial health with good profitability and cost control."
            strengths = ["High revenue generation", "Healthy profit margins"]
            risks = ["Market volatility"]
            recommendations = ["Continue current financial strategy"]
        elif score >= 40:
            status = "MODERATE"
            summary = "The business shows moderate financial health with stable revenue but lower profit margins."
            strengths = ["Consistent revenue stream"]
            risks = ["High operational costs"]
            recommendations = ["Reduce expenses", "Optimize pricing strategy"]
        else:
            status = "RISKY"
            summary = "The business is financially weak with low or negative profitability."
            strengths = []
            risks = ["Sustained losses", "Cash flow pressure"]
            recommendations = ["Immediate cost reduction", "Improve revenue model"]

        credit_risk = "LOW" if profit > 0 else "HIGH"

        return {
            "business_health": {
                "type": "FINANCIAL",
                "status": status,
                "financial_health_score": score,
                "detected_revenue_columns": revenue_cols,
                "detected_expense_columns": expense_cols,
                "detected_profit_columns": profit_cols,
                "total_revenue": round(float(total_revenue), 2),
                "total_expense": round(float(total_expense), 2),
                "profit": round(float(profit), 2)
            },
            "credit_risk": credit_risk,
            "ai_summary": summary,
            "strengths": strengths,
            "risks": risks,
            "recommendations": recommendations
        }

    except Exception as e:
        return {"error": str(e)}
