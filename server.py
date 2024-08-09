
if __name__ == "__main__":
    from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
    from langflow_streamlit.utils.process_utils import wait_for_server_ready
    from langflow_streamlit.utils import settings
    import logging

    LOGGER = logging.getLogger(__name__)

    if settings.LANGFLOW_ENABLED:
        LangflowManager.start()
    APIManager.start()
    wait_for_server_ready("localhost", settings.API_PORT)
    LOGGER.debug("streamlit backend is running!")
    StreamlitManager.start()
