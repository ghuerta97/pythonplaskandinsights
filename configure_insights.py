from flask import current_app
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import logging

def configure_insights(app, instrumentation_key):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = AzureLogHandler(
        connection_string=f'InstrumentationKey={instrumentation_key}')
    handler.setFormatter(verbose_formatter())
    logger.addHandler(handler)

    middleware = FlaskMiddleware(
        app,
        exporter=AzureExporter(
            connection_string=f'InstrumentationKey={instrumentation_key}'
        ),
        sampler=ProbabilitySampler(rate=1.0)
    )

    return logger

def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )