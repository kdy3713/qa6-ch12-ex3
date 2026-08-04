# logging_config.py
import logging


def setup_logger():
    log_format = "[%(asctime)s][%(levelname)s]%(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(
                "src/simple/crawling.log", encoding="utf-8"
            ),  # 파일로 저장
            logging.StreamHandler(),  # 터미널로 출력
        ],
    )


# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
