from pydantic import BaseModel
import logging

logger = logging.getLogger('pipeline_starter')


class VoidModel:
    pass


class StarterOutput(BaseModel):
    launched: bool
    message: str



def handler(event, context) -> StarterOutput:
    try:
        logger.info(event)
        logger.info(context)
    except Exception as e:
        logger.error('Exeuting lambda failed.')
        raise e
    return StarterOutput(launched=True, message='Custom message')
