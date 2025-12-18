import pandas as pd
import joblib
from ..utils.logger import get_logger

logger = get_logger(__name__)

df=joblib.load(r"C:\Users\user\Desktop\Finance_RAG\data\processed\merged_data.pkl")

logger.info(f"Loaded data for early warning analysis with shape: {df.shape}")

def early_warning(df):
    stressed = df[df["days_past_due"] > 30]
    segments = stressed.groupby("employment_type").size()

    return segments

segments = early_warning(df)
logger.info(f"Early warning segments: {segments.to_dict()}")

logger.info("Early warning analysis completed.")