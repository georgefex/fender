from fabric.api import run

def crear_contenedor(nombre,puerto):
    run("docker create --name "+nombre+" -p "+puerto+":"+puerto+" -t -i george/lamp /bin/bash")
    #run("apt-get update && apt-get install ssh -y")
    #run("sed -i 's/without-password/yes/' /etc/ssh/sshd_config")
    #run("service ssh restart")
    #run("echo root:122333 | /usr/sbin/chpasswd")
def correr_contenedor(nombre):
    run("docker start "+nombre)
    run("docker exec -it "+nombre+" bash -c \"service apache2 start\"")
    run("docker exec -it "+nombre+" bash -c \"service mysql start\"")
