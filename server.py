
if __name__ == "__main__":
    try:
        processes = []
        from langflow_streamlit.managers import APIManager, LangflowManager, StreamlitManager
        from langflow_streamlit.utils.process_utils import wait_for_server_ready
        from langflow_streamlit.utils import settings, LOGGER, logger_set_level, generate_log

        if settings.GENERATE_LOG_FILE:
            generate_log()
        else:
            logger_set_level(settings.LOG_LEVEL)

        if not settings.STREAMLIT_ONLY:
            processes.append(LangflowManager.start())
            if wait_for_server_ready("localhost", settings.LANGFLOW_PORT, settings.LANGFLOW_STARTUP_TIMEOUT):
                LOGGER.debug("Langflow is running!")
            else:
                LOGGER.info("Langflow was not started on the given time! try to increase the environment variable LANGFLOW_STARTUP_TIMEOUT")
                exit(1)
        processes.append(APIManager.start())
        wait_for_server_ready("localhost", settings.API_PORT)
        LOGGER.debug("streamlit backend is running!")
        processes.append(StreamlitManager.start())
        [process.join() for process in processes]
    except KeyboardInterrupt:
        LOGGER.debug("Exiting...")
