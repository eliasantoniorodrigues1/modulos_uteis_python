import subprocess

# Windows - ping 127.0.0.1
# LInux - ping 127.0.0.1 -c 4
proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
    )  # Recbe uma lista com os argumentos do comando.

# print(proc.stderr)
# print(proc.returncode)
# print(proc.args)

saida = proc.stdout
print(saida)