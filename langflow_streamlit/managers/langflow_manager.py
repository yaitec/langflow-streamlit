from langflow_streamlit.utils.process_utils import check_if_port_is_used_by_program, kill_process_on_port
from langflow_streamlit.utils import settings, LOGGER
from subprocess import run, PIPE
import multiprocessing


class LangflowManager:
    port = settings.LANGFLOW_PORT

    @classmethod
    def run_langflow(cls, args):
        try:
            exec_result = run(
                f"langflow run {args}",
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
            )
            if exec_result.returncode != 0:
                LOGGER.error(f"Langflow startup failed. stderr: {exec_result.stderr} stdout: {exec_result.stdout}")
        except KeyboardInterrupt:
            LOGGER.info("Shutting down langflow")

    @classmethod
    def start(cls, args=""):
        if check_if_port_is_used_by_program(cls.port, ["langflow"]):
            kill_process_on_port(cls.port)
        process = multiprocessing.Process(target=cls.run_langflow, args=(args,))
        process.start()
        return process