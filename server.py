
if __name__ == "__main__":
    try:
        from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
        from langflow_streamlit.utils.process_utils import wait_for_server_ready
        from langflow_streamlit.utils import settings
        import logging

        LOGGER = logging.getLogger(__name__)

        if not settings.STREAMLIT_ONLY:
            LangflowManager.start()
        APIManager.start()
        wait_for_server_ready("localhost", settings.API_PORT)
        LOGGER.debug("streamlit backend is running!")
        StreamlitManager.start()
    except KeyboardInterrupt:
        LOGGER.debug("Exiting...")
