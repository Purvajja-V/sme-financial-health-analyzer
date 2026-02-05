# AI-Based Financial Health Assessment Platform for SMEs

## Overview
This project is an AI-based Financial Health Assessment Platform designed for Small and Medium Enterprises (SMEs).

The system allows users to upload financial CSV files and automatically analyzes revenue, expenses, and profit using intelligent data classification. Based on the analysis, it evaluates overall business health, assigns a financial health score, assesses credit risk, and provides optimization recommendations.

The solution is built using FastAPI and Python with pandas for data processing. It is deployed as a public REST API with interactive Swagger documentation, enabling easy testing and integration. This platform helps SMEs quickly understand their financial condition and make informed business decisions.


## Features
- Upload CSV financial data
- Automatic revenue, expense, and profit detection
- Financial health scoring
- Credit risk assessment
- Cost optimization recommendations
- REST API using FastAPI
- Interactive Swagger UI

## Tech Stack
- Python
- FastAPI
- pandas, NumPy
- Swagger UI
- Deployed on Render

## Live Demo
The application is deployed and publicly accessible.

Base URL:
https://sme-financial-health-analyzer.onrender.com

API Documentation:
https://sme-financial-health-analyzer.onrender.com/docs

## How to Run Locally
bash
pip install -r requirements.txt
uvicorn main:app --reload

## API Usage

### Analyze Financial Data
Endpoint:
POST /analyze/

Input:
- CSV file containing financial data

Output:
- Business health status
- Financial health score
- Revenue, expense, and profit detection
- Credit risk assessment
- Optimization recommendations

The API can be tested directly using Swagger UI.



