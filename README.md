# AI-Based Financial Health Assessment Platform for SMEs

## Overview
This project analyzes financial data of small and medium enterprises (SMEs) to evaluate business health, credit risk, and profitability. It provides actionable insights and recommendations using AI-style logic.

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



