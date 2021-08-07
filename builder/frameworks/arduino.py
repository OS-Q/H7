from os.path import join

from SCons.Script import DefaultEnvironment, SConscript

env = DefaultEnvironment()
board = env.BoardConfig()
build_core = board.get("build.core", "").lower()

SConscript("_embed_files.py", exports="env")

SConscript(
    join(DefaultEnvironment().PioPlatform().get_package_dir(
        "framework-arduinoespressif32"), "tools", "platformio-build.py"))
