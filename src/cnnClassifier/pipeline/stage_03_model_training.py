from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger



STAZE_NAME ="Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        training_config = config_manager.get_training_config()
    
        # Instantiate Training using the obtained training config
        training = Training(config=training_config)
        training.get_base_model()
    
        # Initialize generators before training
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f"***************")
        logger.info(f">>>>>>{STAZE_NAME} started<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAZE_NAME} compleated<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e 
