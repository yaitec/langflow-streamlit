import typer

app = typer.Typer()

@app.command("run")
def hello(langflow=True):
    from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
    from langflow_streamlit.utils.process_utils import wait_for_server_ready
    from langflow_streamlit.utils import settings
    import logging

    LOGGER = logging.getLogger(__name__)

    if langflow:
        LangflowManager.start()
    APIManager.start()
    wait_for_server_ready("localhost", settings.API_PORT)
    LOGGER.debug("streamlit backend is running!")
    StreamlitManager.start()

if __name__ == "__main__":
    app()