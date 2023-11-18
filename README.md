# End to End Machine learning Project

# Structure my project

src/components/data_ingestion.py: The input data what you want to predict
src/components/data_transformation.py: Actions related to transform data (normalization, one-hot-encoding, ...)
src/components/model_trainer.py: Actions related to train and save models

src/pipeline/train_pipeline.py: The training pipeline after processing data
src/pipeline/predict_pipeline.py: Choose a best model to take a predict with new sample

src/exception.py: To process exceptions in this project
src/utils.py: Actions related to connect database or get a model from cloud
src/logger.py: Track activities of ml project
