def run_streamlit_api():
    from fastapi import FastAPI
    from langflow_streamlit.api import router
    from langflow_streamlit.utils import settings
    from asyncio import new_event_loop
    import uvicorn

    loop = new_event_loop()
    app = FastAPI()
    app.include_router(router, prefix="/api/v1")

    @app.get("/health")
    async def health():
        pass

    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=settings.API_PORT,
        workers=1,
        log_level="error",
        reload=False,
        loop="asyncio",
    )
    loop.create_task(uvicorn.Server(config=config).serve())
    loop.run_forever()


if __name__ == "__main__":
    from langflow_streamlit.managers import LangflowManager, StreamlitManager
    from langflow_streamlit.utils.process_utils import wait_for_server_ready, check_if_port_is_used_by_program, kill_process_on_port
    from langflow_streamlit.utils import settings
    import logging
    import multiprocessing

    LOGGER = logging.getLogger(__name__)

    if check_if_port_is_used_by_program(settings.API_PORT, ["python"]):
        kill_process_on_port(settings.API_PORT)
    streamlit_api_process = multiprocessing.Process(target=run_streamlit_api)
    streamlit_api_process.start()
    wait_for_server_ready("localhost", settings.API_PORT)
    LOGGER.debug("streamlit backend is running!")
    StreamlitManager.start()
    LangflowManager.start()
