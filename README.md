Este es el repositorio donde contiene mi codigo donde podremos obtener información sobre los host, puertos y argumentos de las máquinas virtuales, en mi caso lo probé solo en kali y en lubuntu, asi ocomo también coloqué algunas direcciones especificas de mi tele, mi celular y el de mi hermana para hacer mas verificaciones. 
aqui encontrarás una guia para que puedas ejecutar todo lo que viene dentro del repositorio:

primero, en una terminal de kali, creamos o activamos nuestro environment:

                python3 -m venv venv 
    
de ser necesario, instalamos lo que nos pida:

                sudo apt install python3.11-venv
  
con todo instalado, creamos nuestro entorno virtual:

                python3 -m venv venv  

seguido de esto, lo activamos:

                source venv/bin/activate  

dentro de este entorno, deberemos instalar las dependencias necesarias con: 

                sudo pip install python-nmap 

o podemos ejecutar requeriments para asi poder correr el codigo con las dependencias necesarias:

                pip install -r requirements.txt

despues, creo un archivo .py que será con el que ejecutaremos la tarea:

                nano python-nmap.py 

luego ejecuto con sudo el script creado:

                sudo python3 python-nmap.py 

deberás colocar tu contraseña para que se pueda ejectur, seguido de esto ya tienes un código que corre y obtiene las clasificaciones que buscamos 

dentro del srcript, te pide a ti como usuario que le indiques el host, los puertos, los argumentos de nmap que se ejecutaran, asi como te pregunta si quieres que se ejecute como superusuario o no
seguido de esto se ejecuta y muestra los resultados obtenidos. 
