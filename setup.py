from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "reconnaissance",
    version = "1.0",
    description = "https://github.com/ryurina/frSpeechReco",
    executables = [Executable("frspeechreco.py")],
)
