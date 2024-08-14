from langflow_streamlit.utils.process_utils import check_if_port_is_used_by_program, kill_process_on_port
from langflow_streamlit.utils import settings
from subprocess import run, PIPE
from time import sleep
import multiprocessing
import logging
import os


class StreamlitManager:
    port = settings.STREAMLIT_PORT
    path = settings.FOLDER_PATH
    logger = logging.getLogger(__name__)

    @classmethod
    def __load_streamlit(cls):
        if not os.path.exists(f"{cls.path}streamlit.py"):
            with open(f"{cls.path}streamlit.py", "w") as file:
                file.write("import streamlit as st")
        else:
            with open(f"{cls.path}streamlit.py", "r+") as file:
                content = file.read()
                if len(content) < 10:
                    file.seek(0)
                    file.write("import streamlit as st\nfrom time import sleep\nwhile True:\n    sleep(2)")
                    file.truncate()

    @classmethod
    def is_running(cls):
        for _ in range(10):
            sleep(1)
            if check_if_port_is_used_by_program(cls.port, ["streamlit"]):
                cls.logger.info(f"Streamlit server is listening http://0.0.0.0:{cls.port}")
                return True
        return False


    @classmethod
    def ignore_email(cls):
        import os
        from os.path import exists, isfile, expanduser

        streamlit_config_path = expanduser("~")+ "/.streamlit"
        if not exists(streamlit_config_path):
            os.makedirs(streamlit_config_path)
        if not isfile(streamlit_config_path+"/credentials.toml"):
            with open(streamlit_config_path+"/credentials.toml", "w") as f:
                f.write('[general]\nemail = ""')

    @classmethod
    def run_streamlit(cls, args):
        cls.ignore_email()
        if run(
            f"streamlit run {cls.path}streamlit.py --browser.serverPort {cls.port} --server.port {cls.port} {args}",
            shell=True,
            stdout=PIPE,
        ).returncode != 0:
            raise Exception("Streamlit startup failed.")

    @classmethod
    def start(cls, headless=False):
        if check_if_port_is_used_by_program(cls.port, ["streamlit"]):
            kill_process_on_port(cls.port)
        cls.__load_streamlit()
        streamlit_process = multiprocessing.Process(target=cls.run_streamlit, args=(f"--server.headless {str(headless).lower()}",))
        streamlit_process.start()

        if not cls.is_running():
            streamlit_process.kill()
            streamlit_process = multiprocessing.Process(target=cls.run_streamlit, args=(f"--server.headless true",))
            streamlit_process.start()
        if not cls.is_running():
            cls.logger.error("Streamlit did not start up")


    @classmethod
    def restart(cls):
        kill_process_on_port(cls.port)
        cls.start("--server.headless true")
