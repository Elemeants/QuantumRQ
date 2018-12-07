@echo off
set quantumPATH=%~dp0
set mainPATH=%cd%
echo %mainPATH%
echo %quantumPATH%
python "%quantumPATH%QuantumRQ.py" '%quantumPATH%' '%mainPATH%'