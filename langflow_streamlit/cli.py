import typer

app = typer.Typer()

@app.command()
def run(
    streamlit_only: bool = typer.Option(False, "--streamlit-only", help="Run only the Streamlit frontend (default: False)")
):
    """
    Run the Langflow Streamlit application.
    """
    from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
    from langflow_streamlit.utils.process_utils import wait_for_server_ready
    from langflow_streamlit.utils import settings
    import logging

    LOGGER = logging.getLogger(__name__)

    if not streamlit_only:
        LangflowManager.start()
        wait_for_server_ready("localhost", settings.LANGFLOW_PORT)
        LOGGER.debug("Langflow is running!")
    APIManager.start()
    wait_for_server_ready("localhost", settings.API_PORT)
    LOGGER.debug("API backend is running!")
    LOGGER.debug("Starting Streamlit frontend in Streamlit-only mode...")
    StreamlitManager.start()
    LOGGER.debug("Streamlit frontend is running. Langflow and API backend not started.")

def app(args=None):
    typer_app = typer.Typer()
    typer_app.command()(run)
    typer_app(args)
