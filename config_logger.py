import logging

def iniciar_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("automacao_gov.log", mode='a', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )