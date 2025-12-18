from data.processed import *
import os
import pandas as pd
import joblib

from ..utils.logger import get_logger
logger = get_logger(__name__)

logger.info("Starting structured data ingestion...")

df=joblib.load(r"C:\Users\user\Desktop\Finance_RAG\data\processed\merged_data.pkl")

logger.info(f"Loaded structured data successfully with shape: {df.shape}")
# Further processing can be added here
# if in future we want to process structured data differently

