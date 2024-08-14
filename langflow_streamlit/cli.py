from typing import Union
import typer

app = typer.Typer()

@app.command()
def run(
    streamlit_only: bool = typer.Option(False, "--streamlit-only", help="Run only the Streamlit frontend (default: False)"),
    log_level: Union["critical", "error", "warning", "info", "debug"] = typer.Option("info", "--log-level", help="Define log level of library(default: 'info')"),
    generate_log_file: bool = typer.Option("--generate-log-file", help="Create a langflow-streamlit.log file to debug purpose(default: False)")
):
    """
    Run the Langflow Streamlit application.
    """
    from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
    from langflow_streamlit.utils.process_utils import wait_for_server_ready
    from langflow_streamlit.utils import settings, LOGGER, logger_set_level, generate_log
    
    if generate_log_file:
        generate_log()
    else:
        logger_set_level(log_level)

    try:
        processes = []
        if not streamlit_only:
            processes.append(LangflowManager.start())
            wait_for_server_ready("localhost", settings.LANGFLOW_PORT, 20)
            LOGGER.debug("Langflow is running!")
        processes.append(APIManager.start())
        wait_for_server_ready("localhost", settings.API_PORT)
        LOGGER.debug("API backend is running!")
        LOGGER.debug("Starting Streamlit frontend.")
        processes.append(StreamlitManager.start())
        LOGGER.debug("Streamlit frontend is running. Langflow and API backend not started.")
        [process.join() for process in processes]
    except KeyboardInterrupt:
        LOGGER.debug("Exiting...")

def app(args=None):
    typer_app = typer.Typer()
    typer_app.command()(run)
    typer_app(args)
