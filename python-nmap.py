import nmap

def realizar_escaneo(host_objetivo, puertos_objetivo, argumentos_escaneo, ejecutar_como_root):
    scanner = nmap.PortScanner()
    cadena_puertos = ",".join(puertos_objetivo)  # Convertir la lista de puertos en una cadena separada por comas
    argumentos_completos = argumentos_escaneo + ' -O -sV --script=default'
    
    if ejecutar_como_root:
        scanner.scan(hosts=host_objetivo, ports=cadena_puertos, arguments=argumentos_completos, sudo=True)
    else:
        scanner.scan(hosts=host_objetivo, ports=cadena_puertos, arguments=argumentos_completos)

    for host_escaneado in scanner.all_hosts():
        print(f"Host escaneado : {host_escaneado} ({scanner[host_escaneado].hostname()})")
        print(f"Estado : {scanner[host_escaneado].state()}")
        
        for info_os in scanner[host_escaneado]['osmatch']:
            print("----------")
            print('Nombre del SO : {0}'.format(info_os['name']))
            print('Precisión : {0}'.format(info_os['accuracy']))
            print('Línea : {0}'.format(info_os['line']))
            
            for clase_os in info_os['osclass']:
                print('Tipo de Clase del SO : {0}'.format(clase_os['type']))
                print('Proveedor : {0}'.format(clase_os['vendor']))
                print('Familia del SO : {0}'.format(clase_os['osfamily']))
                print('Generación : {0}'.format(clase_os['osgen']))
                print('Precisión de Clase : {0}'.format(clase_os['accuracy']))
        
        for protocolo in scanner[host_escaneado].all_protocols():
            print("----------")
            print(f"Protocolo : {protocolo}")
            print("----------")

            claves_puerto = scanner[host_escaneado][protocolo].keys()
            for puerto in claves_puerto:
                print(f"Puerto : {puerto}\tEstado : {scanner[host_escaneado][protocolo][puerto]['state']}")
                print(f"Nombre del Servicio : {scanner[host_escaneado][protocolo][puerto]['name']}")
                print(f"Producto : {scanner[host_escaneado][protocolo][puerto]['product']}")
                print(f"Versión : {scanner[host_escaneado][protocolo][puerto]['version']}")
                print(f"Información Adicional : {scanner[host_escaneado][protocolo][puerto]['extrainfo']}")
                print(f"Configuración : {scanner[host_escaneado][protocolo][puerto]['conf']}")
                print(f"CPE : {scanner[host_escaneado][protocolo][puerto]['cpe']}")
                print("----------")

# Ejemplo de uso
host_objetivo = input("Por favor ingresa el host a escanear: ")
puertos_objetivo = input("Por favor ingresa los puertos (separados por coma): ").split(",")
argumentos_escaneo = input("Por favor ingresa argumentos adicionales para el escaneo: ")
ejecutar_como_root = input("¿Deseas ejecutar el escaneo como root? (s/n): ").lower() == "s"

realizar_escaneo(host_objetivo, puertos_objetivo, argumentos_escaneo, ejecutar_como_root)
