import sys
from langflow_streamlit.cli import app

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        app(sys.argv[2:])
    else:
        app()

if __name__ == "__main__":
    main()
