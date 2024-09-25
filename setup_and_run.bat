@echo off

If Not Exist "%~dp0%\.venv\Scripts\activate.bat" (
	python -m venv .venv
	call "%~dp0%\.venv\Scripts\activate"
	pip install -r requirements.txt
)

call "%~dp0%\.venv\Scripts\activate"
python main.py --channel_name @KillTony
REM In case you want to run a KillTony episode with a certain Guest, e.g. Adam Ray run the following command
REM python main.py --channel_name @KillTony --guest_name "Adam Ray"
pause