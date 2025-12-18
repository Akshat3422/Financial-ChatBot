import pandas as pd
import joblib
from ..utils.logger import get_logger

logger = get_logger(__name__)

df=joblib.load(r"C:\Users\user\Desktop\Finance_RAG\data\processed\merged_data.pkl")

logger.info(f"Loaded data for segment_risk calculations with shape: {df.shape}")



def segment_risk(df, segment_col):
    return (
        df.groupby(segment_col)
        .agg(
            approval_rate=("application_stage", lambda x: (x=="Approved").mean()),
            avg_dpd=("days_past_due", "mean"),
            loan_count=("application_id", "count")
        )
        .reset_index()
    )

segments = segment_risk(df, "employment_type")

logger.info(f"Calculated segment risk metrics:\n{segments}")
logger.info("Segmentation analysis completed.")