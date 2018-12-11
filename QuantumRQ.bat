@echo off
set quantumPATH=%~dp0
set mainPATH=%cd%
REM echo %mainPATH%
REM echo %quantumPATH%
python "%~dp0/QuantumRQ.py" %quantumPATH% %mainPATH%