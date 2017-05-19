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
    run("docker exec -it "+nombre+" bash -c \"service ssh start\"")

def despliegue1():
    run("rm -rf ayd2blog")
    run("git clone https://github.com/ercalel/ayd2blog.git")
    
def despliegue2():
    run("rm -r /var/www/example.com/public_html/*")
    run("mv  -v /root/ayd2blog/blog/* /var/www/example.com/public_html")
    
def despliegue3(ip):
    run("sed -i \"s/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/"+ip+"/g\" /var/www/example.com/public_html/php/conexion.php > conexion.php")
   # run("rm  /var/www/example.com/public_html/php/conexion.php")
   # run("mv conexion.php /var/www/example.com/public_html/")

    
