import os
import pandas as pd
import joblib
from ..utils.logger import get_logger



logger = get_logger(__name__)


logger.info("Starting document ingestion...")

path = r"C:\Users\user\Desktop\Finance_RAG\data\processed\merged_data.pkl"



customers = pd.read_csv(r"C:\Users\user\Desktop\Finance_RAG\data\raw\customers.csv")
loans = pd.read_csv(r"C:\Users\user\Desktop\Finance_RAG\data\raw/loan_applications.csv")
repayments = pd.read_csv(r"C:\Users\user\Desktop\Finance_RAG\data\raw/repayments.csv")




df = loans.merge(customers, on="customer_id", how="left")
df = df.merge(repayments, left_on="application_id", right_on="loan_id", how="left")

logger.info(f"Merged data succesful amd its shpe is : {df.shape}")





os.makedirs(os.path.dirname(path), exist_ok=True)

if os.path.exists(path):
    os.remove(path)   # removes locked/old file

joblib.dump(df, path)
