import pandas as pd
import joblib
from ..utils.logger import get_logger

logger = get_logger(__name__)

df=joblib.load(r"C:\Users\user\Desktop\Finance_RAG\data\processed\merged_data.pkl")

logger.info(f"Loaded data for KPI calculations with shape: {df.shape}")
def calculate_kpis(df):
    kpis = {
        "approval_rate": ((df["application_stage"] == "Approved").mean()*100),
        "rejection_rate": ((df["application_stage"] == "Rejected").mean()*100),
        "avg_dpd": (df["days_past_due"].fillna(0).mean()*100)
    }
    return kpis


kpis = calculate_kpis(df)

logger.info(f"Calculated KPIs: {kpis}")
logger.info("KPI calculations completed.")

