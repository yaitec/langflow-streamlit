from langflow_streamlit.utils.process_utils import check_if_port_is_used_by_program, kill_process_on_port
from langflow_streamlit.utils import settings
from subprocess import run, PIPE
import multiprocessing


class LangflowManager:
    port = settings.LANGFLOW_PORT

    @classmethod
    def run_langflow(cls, args):
        if run(
            f"langflow run {args}",
            shell=True,
            stdout=PIPE,
        ).returncode != 0:
            raise Exception("langflow startup failed.")
    
    @classmethod
    def start(cls, args=""):
        if check_if_port_is_used_by_program(cls.port, ["langflow"]):
            kill_process_on_port(cls.port)
        langflow_process = multiprocessing.Process(target=cls.run_langflow, args=(args,))
        langflow_process.start()