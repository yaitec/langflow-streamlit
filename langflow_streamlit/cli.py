import typer

from enum import Enum

class LogLevelEnum(Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"

def run(
    streamlit_only: bool = typer.Option(False, "--streamlit-only", help="Run only the Streamlit frontend (default: False)"),
    log_level: LogLevelEnum = typer.Option("info", "--log-level", help="Defines log level of library(default: 'info')"),
    log_file_generation: bool = typer.Option(False, "--log-file-generation", help="Creates a langflow-streamlit.log file to debug purpose(default: False)")
):
    """
    Run the Langflow Streamlit application.
    """
    from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
    from langflow_streamlit.utils.process_utils import wait_for_server_ready
    from langflow_streamlit.utils import settings, LOGGER, logger_set_level, generate_log
    
    if log_file_generation:
        generate_log()
    else:
        logger_set_level(log_level.value)

    try:
        processes = []
        if not streamlit_only:
            processes.append(LangflowManager.start())
            if wait_for_server_ready("localhost", settings.LANGFLOW_PORT, settings.LANGFLOW_STARTUP_TIMEOUT):
                LOGGER.info(f"Langflow is running and listening on http://localhost:{settings.LANGFLOW_PORT}")
            else:
                LOGGER.info("Langflow was not started on the given time! try to increase the environment variable LANGFLOW_STARTUP_TIMEOUT")
                exit(1)
        processes.append(APIManager.start())
        wait_for_server_ready("localhost", settings.API_PORT)
        LOGGER.info(f"API backend is running and listening on http://localhost:{settings.API_PORT}/docs")
        processes.append(StreamlitManager.start())
        LOGGER.info(f"Streamlit frontend is running and listening on http://localhost:{StreamlitManager.port}")
        [process.join() for process in processes]
    except KeyboardInterrupt:
        LOGGER.debug("Exiting...")

def app(args=None):
    typer_app = typer.Typer()
    typer_app.command()(run)
    typer_app(args)
