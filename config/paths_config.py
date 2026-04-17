import os

############################# DATA INGESTION RELATED PATHS #############################
RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR, "data.csv")

CONFIG_PATH = "config/config.yaml"

############################# DATA PREPROCESSING RELATED PATHS #############################
PREPROCESSING_DIR = "artifacts/preprocessing"
PREPROCESSED_FILE_PATH = os.path.join(PREPROCESSING_DIR, "preprocessed_data.csv")

X_TRAIN_PATH = os.path.join(PREPROCESSING_DIR, "X_train.csv")
X_TEST_PATH = os.path.join(PREPROCESSING_DIR, "X_test.csv")
Y_TRAIN_PATH = os.path.join(PREPROCESSING_DIR, "y_train.csv")
Y_TEST_PATH = os.path.join(PREPROCESSING_DIR, "y_test.csv")

LABEL_ENCODER_DIR = os.path.join(PREPROCESSING_DIR, "label_encoder")
LABEL_ENCODER_PATH = os.path.join(LABEL_ENCODER_DIR, "label_encoder.pkl")

SCALER_DIR = os.path.join(PREPROCESSING_DIR, "scaler")
SCALER_PATH = os.path.join(SCALER_DIR, "scaler.pkl")
