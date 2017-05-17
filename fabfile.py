from fabric.api import run

def crear_contenedor(nombre,no):
    run("docker create --name "+nombre+" -p 8"+no+":8"+no+" -t -i linode/lamp /bin/bash")
