import tkinter as tk
from PIL import Image, ImageTk
from screeninfo import get_monitors
import customtkinter as ctk
from tkinter import ttk,filedialog, messagebox
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox
import sqlite3
import pandas as pd
import sys
import shutil
from datetime import datetime
import locale
import re
import requests
import pytz
import zipfile
import io
import threading




ctk.set_appearance_mode("light")



def conectar_bd():
    con = sqlite3.connect('Catalogo_digital-main/Articuloss.db')
    return con
def on_cerrar_ventana():
    q = CTkMessagebox(title="¿Salir?", message="¿Desea salir del catálogo?",
                        icon="question", option_1="Cancelar", option_3="Si", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))
    r = q.get()
    
    if r == "Si":
        sys.exit()
def guardar_imagen(ruta, nombre):
    ruta_imagen_original = ruta
    nombre_predeterminado = nombre

    # Crear una ventana emergente para seleccionar la ubicación y el nombre del archivo
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar al usuario la ubicación y el nombre del archivo de destino
    ruta_destino = filedialog.asksaveasfilename(
        initialdir="/",
        title="Guardar Imagen",
        defaultextension=".jpg",
        filetypes=[("Archivos de imagen", "*.jpg")],
        initialfile=nombre_predeterminado  # Nombre predeterminado
    )
    
    if not ruta_destino:
        def eliminar(event):
            c.destroy()

        c =  CTkMessagebox(title="Error", message="No se seleccionó una ubicación de destino. La imagen no se ha guardado.", icon="cancel", option_focus=1)
        c.focus_set()
        c.bind("<Return>", eliminar)               

        return

    try:
        # Copiar la imagen al directorio de destino
        shutil.copy(ruta_imagen_original, ruta_destino)
        def eliminar(event):
            c.destroy()
        c = CTkMessagebox(title="Info", message=f"La imagen se ha guardado en {ruta_destino} con éxito", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))
        c.focus_set()
        c.bind("<Return>", eliminar)
    except FileNotFoundError:
        def eliminar(event):
            c.destroy()
        c =CTkMessagebox(title="Error", message=f"No se pudo encontrar la imagen en la ruta '{ruta_imagen_original}'", icon="cancel", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))
        c.focus_set()
        c.bind("<Return>", eliminar)  
    except Exception as e:
        def eliminar(event):
            c.destroy()
        c= CTkMessagebox(title="Error", message=f"Se produjo un error al guardar la imagen: {str(e)}", icon="cancel", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))
        c.focus_set()
        c.bind("<Return>", eliminar)  
'''
config = {
    'user': 'capemi',
    'password': 'kpmi',
    'host': '192.168.123.10',
    'database': 'partes',
    'auth_plugin': 'caching_sha2_password'
    }

    conexion = mysql.connector.connect(**config)
    return conexion'''

class Ventana_p:
    def __init__(self, root):
        def obtener_interna():
            # Configura el idioma local a español
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

            with open("Catalogo_digital-main/verificacion.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(' ')
                    date_part = parts[0]
                    date = datetime.strptime(date_part, "%Y-%m-%d")
                    # Formatear la fecha para imprimir en el formato deseado con el mes en español
                    formatted_date = date.strftime("%d-%B-%Y")
                    formatted_date =str(formatted_date)
                    formatted_date = formatted_date.upper()
                    return(formatted_date)
        def resize_image(event):
            new_height = event.height

            resized_image = meta.resize((event.width, new_height)) 
            resized = ImageTk.PhotoImage(resized_image)
            self.capemi_barra.configure(image=resized)
            self.capemi_barra.image = resized

        meta = Image.open("Catalogo_digital-main/meta.png")      
        auto = Image.open("Catalogo_digital-main/liviana.png")
        camion = Image.open("Catalogo_digital-main/pesada.png")      
        engra = Image.open("Catalogo_digital-main/OT.png")                     
        self.publi = Image.open(f"Catalogo_digital-main/banner.png")

        

        self.auto_copy = auto.copy()
        self.camion_copy = camion.copy()
        self.engra_copy = engra.copy()
 

    

        self.diez = 0
        self.letra = 0
        monitor = get_monitors()[0]


        if monitor.width <= 1280:
            if monitor.width <= 832:            
                c = messagebox.showerror("Error",f"Lo sentimos, el catálogo no admite resoluciones menores a 1024px, disculpe las molestias")
                if c:
                    sys.exit()
            elif monitor.width <= 1024:
                ancho_ventana = int(monitor.width) 
                alto_ventana = int(monitor.height)
                self.diez = 7
                self.letra = 7
            elif monitor.width <= 1152:
                ancho_ventana =int(1152)
                alto_ventana = int(648)
                self.diez = 10
                self.letra = 8
            elif monitor.width <= 1280:
                ancho_ventana =int(monitor.width)
                alto_ventana = int(720)
                self.diez = 11
                self.letra = 10
            
            dev = Image.open("Catalogo_digital-main/dev.png").resize((30,20))

            lupa = Image.open("Catalogo_digital-main/lupa.png").resize((20, 20))
            eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((30, 30))
            back = Image.open("Catalogo_digital-main/back.png").resize((30, 30))
            
        else:
            if monitor.width <=1440:
                self.diez = 12
                self.letra = 11
                ancho_ventana = int(monitor.width)
                alto_ventana = int(monitor.height)
                dev = Image.open("Catalogo_digital-main/dev.png").resize((30,20))

                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((20, 20))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((50, 50))
                back = Image.open("Catalogo_digital-main/back.png").resize((40, 40))

            elif monitor.width <=1680:
                self.diez = 12
                self.letra = 12
                ancho_ventana = int(monitor.width)
                alto_ventana = int(monitor.height)
                dev = Image.open("Catalogo_digital-main/dev.png").resize((30,20))

                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((50, 50))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((50, 50))
                back = Image.open("Catalogo_digital-main/back.png").resize((40, 40))
                
            elif monitor.width <=1760:
                self.diez = 12
                self.letra = 14
                ancho_ventana = int(monitor.width)
                alto_ventana = int(monitor.height) 
                dev = Image.open("Catalogo_digital-main/dev.png").resize((40,30))

                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((50, 50))
                back = Image.open("Catalogo_digital-main/back.png").resize((40, 40))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((50, 50))
                
            elif monitor.width <=1920:         
                self.diez = 15
                self.letra = 15
                ancho_ventana = int(monitor.width)
                alto_ventana = int(monitor.height)
                dev = Image.open("Catalogo_digital-main/dev.png").resize((40,30))
                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((70, 70))
                back = Image.open("Catalogo_digital-main/back.png").resize((60, 60))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((50, 50))
               
            elif monitor.width <= 2560 :
                self.diez = 18
                self.letra = 20
                ancho_ventana = int(monitor.width)
                alto_ventana = int(monitor.height)
                dev = Image.open("Catalogo_digital-main/dev.png").resize((40,30)) 

                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((50, 50))
                back = Image.open("Catalogo_digital-main/back.png").resize((70, 70))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((60, 60)) 
                
            elif monitor.width <= 3200:
                self.diez = 18
                self.letra = 20
                ancho_ventana = int(monitor.width)
                alto_ventana = int(monitor.height)
                dev = Image.open("Catalogo_digital-main/dev.png").resize((40,30)) 

                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((50, 50))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((50, 50))
                back = Image.open("Catalogo_digital-main/back.png").resize((80, 80))
            elif monitor.width <= 3840:
                self.diez = 18
                self.letra = 20
                ancho_ventana = int(3500)
                alto_ventana = int(2000)
                dev = Image.open("Catalogo_digital-main/dev.png").resize((40,30)) 

                lupa = Image.open("Catalogo_digital-main/lupa.png").resize((50, 50))
                eliminar = Image.open("Catalogo_digital-main/eliminar.png").resize((50, 50))
                back = Image.open("Catalogo_digital-main/back.png").resize((80, 80))
                
                      
        self.back =  ImageTk.PhotoImage(back)
        self.eliminar = CTkImage(eliminar)
        self.imagen_lupa = CTkImage(lupa) 
        self.engranaje = ImageTk.PhotoImage(engra)
        self.camion =ImageTk.PhotoImage(camion)
        self.auto =ImageTk.PhotoImage(auto)
        self.dev = ImageTk.PhotoImage(dev)
        self.capemi= ImageTk.PhotoImage(meta)

        # Calcular las coordenadas para el centro de la pantalla
        x = (monitor.width - ancho_ventana) // 2
        y = (monitor.height - alto_ventana) // 2
        self.root = root
        self.root.title("CATÁLOGO CAPEMI - A. Giacomelli SA")
        self.root.iconbitmap("Catalogo_digital-main/icono.ico")

        self.root.state("zoomed")
        self.root.geometry(f"{ancho_ventana}x{alto_ventana-70}+{x-10}+{y}")
        self.root.maxsize(ancho_ventana, alto_ventana-60)
        self.root.resizable(0,0)

        self.root.bind("<Escape>", self.volver_pantalla_principal)
        
        self.root.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)
        #BARRA CAPEMI  
        label_cap = tk.Label(self.root)
        label_cap.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.capemi_barra = tk.Label(label_cap, image=self.capemi)
        self.capemi_barra.place(relx=0, rely=0)
        
        #BARRA SUPERIOR
        self.frame_barra = tk.Frame(self.root, bg="white")
        self.frame_barra.place(relx=0, rely=0, relwidth=1, relheight=0.02)

        label_cap.bind("<Configure>",  resize_image)

        self.frame_botones = tk.Frame(self.root, bg= "#ededed")
        self.frame_botones.place(relx=0.65, rely=0.08, relheight=0.1,relwidth=0.35)

        boton1 = tk.Button(self.frame_botones, text = "Lanzamientos" ,fg="#04366D", borderwidth=0, highlightthickness=0, cursor="hand2",font=("SEGOE UI",  self.letra+3, "bold"), activeforeground=  "dodgerblue3",activebackground="#ededed", bg= "#ededed", anchor="center",justify="center" )
        boton2 = tk.Button(self.frame_botones, text = "Contacto" ,fg="#04366D", borderwidth=0, highlightthickness=0, cursor="hand2",font=("SEGOE UI",  self.letra+3, "bold"), activeforeground=  "dodgerblue3",activebackground="#ededed", bg= "#ededed", anchor="center",justify="center" )
        boton3 = tk.Button(self.frame_botones, text = "Empresa" ,fg="#04366D", borderwidth=0, highlightthickness=0, cursor="hand2",font=("SEGOE UI",  self.letra+3, "bold"), activeforeground=  "dodgerblue3",activebackground="#ededed", bg= "#ededed", anchor="center",justify="center", command=self.empresa)
        boton4 = tk.Button(self.frame_botones, text = "Favoritos" ,fg="#04366D", borderwidth=0, highlightthickness=0, cursor="hand2",font=("SEGOE UI",  self.letra+3, "bold"), activeforeground=  "dodgerblue3",activebackground="#ededed", bg= "#ededed", anchor="center",justify="center" )
        self.frame_botones.columnconfigure(4)
        barra1 = tk.Label(self.frame_botones, text="|", fg="#04366D",font=("SEGOE UI",  self.letra+20, "bold")) 
        barra2 = tk.Label(self.frame_botones, text="|", fg="#04366D",font=("SEGOE UI",  self.letra+20, "bold")) 
        barra3 = tk.Label(self.frame_botones, text="|", fg="#04366D",font=("SEGOE UI",  self.letra+20, "bold")) 

        boton1.grid(column=0, row=0, pady=15)
        barra1.grid(column=1, row=0)
        boton2.grid(column=2, row=0)
        barra2.grid(column=3, row=0)
        boton3.grid(column=4, row=0)
        barra3.grid(column=5, row=0)
        boton4.grid(column=6, row=0)

        label_actualizado = tk.Label(self.frame_barra, text = f"Actualizado el: {obtener_interna()}", font= ("SEGOE UI", self.diez, "bold"), fg= "#04366D", bg="white")
        boton_verificar = tk.Button(self.frame_barra, text = "Verificar actualizaciones", font= ("SEGOE UI", self.diez, "bold"), fg= "#04366D", bg="white", borderwidth=0, highlightthickness=0, cursor="hand2" , activebackground= "white", activeforeground=  "dodgerblue3", command= lambda: self.circulo_carga(ancho_ventana,alto_ventana))
        self.boton_dev = tk.Button(self.frame_barra,image=self.dev,bg="white", borderwidth=0, highlightthickness=0, cursor="hand2",activebackground= "white")
        label_actualizado.place(relx=0.05, rely=0, relheight=1, relwidth=0.22)
        boton_verificar.place(relx=0.7, rely=0,  relheight=1, relwidth=0.22)     
        self.boton_dev.place(relx=0.95, rely=0,  relheight=1, relwidth=0.04)
        
        self.frame_principal_fn()
        

    def probar_new_main(self):
        import os
        import sys
        import shutil
        import tkinter as tk

        self.nombre_archivo_principal = os.path.splitext(sys.argv[0])[0]

        def abrir_ventana_nueva():
            # Verificar si existe el archivo principal renombrado
            if os.path.isfile(f"{self.nombre_archivo_principal}.py"):
                self.popup.destroy()

                
                def i():
                    os.system(f"{self.nombre_archivo_principal}.py")
                t = threading.Thread(target=i)
                t.start()
                
                self.root.destroy()

                
                
            else:
                # Mostrar un mensaje de error si el archivo renombrado no existe
                tk.messagebox.showerror("Error", f"El archivo '{self.nombre_archivo_principal}.py' no existe en el directorio actual.")

        def ejecutar(): 

            # Obtener el nombre del archivo principal sin la extensión
            if os.path.isfile("Catalogo_digital-main/main2.py"):

                # Renombrar el archivo "prueba.py" con el nombre del archivo principal
                shutil.move("Catalogo_digital-main/main2.py", f"{self.nombre_archivo_principal}.py")

            c= CTkMessagebox(title="Actualizacion", message="Es necesario reiniciar el catálogo para implementar las actualizaciones\n¿Reiniciar ahora?",icon="question", option_1="Si", option_2="Ahora no",option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))   
            c.focus_set()    
            g = c.get()
            if g == "Si":
                abrir_ventana_nueva()        

                
        ejecutar()



    def verificar_si_actualizacion(self):

        def nueva_fecha_interna(fecha):
            with open('Catalogo_digital-main/verificacion.txt', 'w') as archivo:
                # Escribe el nuevo contenido en el archivo
                archivo.write(str(fecha))

        #OBTENER FECHA articulos.db
        def obtener_fecha_db():
            def obtener_fecha_modificacion_archivo(url_repositorio, nombre_archivo):       
                # Obtener la información del repositorio utilizando la GitHub API
                api_url = f"https://api.github.com/repos/{url_repositorio.split('/')[3]}/{url_repositorio.split('/')[4]}"
                response = requests.get(api_url)
                repositorio = response.json()
                # Obtener la información de los commits del repositorio utilizando la GitHub API
                api_url_commits = f"{repositorio['url']}/commits"
                response_commits = requests.get(api_url_commits)
                commits = response_commits.json()

                # Obtener la fecha de última confirmación (commit) del archivo
                for commit in commits:
                    sha = commit['sha']
                    api_url_commit = f"https://api.github.com/repos/{url_repositorio.split('/')[3]}/{url_repositorio.split('/')[4]}/commits/{sha}"
                    response_commit = requests.get(api_url_commit)
                    commit_data = response_commit.json()
                    

                    # Verificar si el archivo está presente en la lista de archivos modificados en el commit
                    for archivo_modificado in commit_data['files']:
                        if archivo_modificado['filename'] == nombre_archivo:
                            fecha_commit = commit_data['commit']['committer']['date']
                            fecha_commit = datetime.strptime(fecha_commit, "%Y-%m-%dT%H:%M:%SZ")
                            fecha_commit = pytz.utc.localize(fecha_commit).astimezone(pytz.timezone("America/Argentina/Buenos_Aires"))
                            fecha_formateada = fecha_commit.strftime("%Y-%m-%d %H:%M:%S")
                            fecha_dt = datetime.strptime(fecha_formateada, "%Y-%m-%d %H:%M:%S")
                            return(fecha_dt)

                print(f"No se encontró el archivo: {nombre_archivo}")

            # URL del repositorio
            url_repositorio = "https://github.com/Capemi/Catalogo_digital"

            # Nombre del archivo
            nombre_archivo = "Articuloss.db"

            # Llamar a la función obtener_fecha_modificacion_archivo
            fecha = obtener_fecha_modificacion_archivo(url_repositorio, nombre_archivo)
            return(fecha)

        #DESCARGAR LOS ARCHIVOS
        def descargar_repo():
            def descargar_repositorio(url_repositorio):
                # Descargar el archivo comprimido del repositorio
                response = requests.get(url_repositorio)
                contenido_zip = zipfile.ZipFile(io.BytesIO(response.content))

                # Extraer los archivos del repositorio en el directorio actual
                contenido_zip.extractall()

            # URL del repositorio
            url_repositorio = "https://github.com/Capemi/Catalogo_digital/archive/main.zip"

            # Llamar a la función descargar_repositorio
            descargar_repositorio(url_repositorio)

        #LEER FECHA
        def obtener_interna():
            with open("Catalogo_digital-main/verificacion.txt", "r") as file:
                for line in file:
                    date = datetime.strptime(line, "%Y-%m-%d %H:%M:%S") 
                    return(date)


        fecha_interna = obtener_interna()
        fecha_db = obtener_fecha_db()

        diferencia_db = fecha_interna - fecha_db
        # Comparar el resultado
        if diferencia_db.total_seconds() < 0:
            descargar_repo()
            nueva_fecha_interna(fecha_db)
            self.probar_new_main()
            '''
            def eliminar(event):
                c.destroy()
                self.entry_buscar.focus_set()
            c= CTkMessagebox(title="En Desarrollo", message="CATÁLOGO DIGITAL SE HA ACTUALIZADO CON EXITO",icon="Catalogo_digital-main/ele_blanco.png", option_1="Gracias", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))   
            c.focus_set()            
            c.bind("<Return>", eliminar)'''
            
        else:
            def eliminar(event):
                c.destroy()
                self.entry_buscar.focus_set()
            self.popup.destroy()
            c= CTkMessagebox(title="En Desarrollo", message="NO HAY ACTUALIZACIONES DISPONIBLES.\nDisfrute su ultima version",icon="Catalogo_digital-main/ele_blanco.png", option_1="Gracias", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))   
            c.focus_set()            
            c.bind("<Return>", eliminar) 
        

    def circulo_carga(self, ancho,alto):
        self.rotation_degree = 0  # Declara rotation_degree como global

        def descargar_desde_github():
            self.verificar_si_actualizacion()


        def iniciar_descarga():
            
            self.popup = tk.Toplevel(root, background="white")
            self.popup.overrideredirect(True)
            x = self.root.winfo_screenwidth() // 2 - ancho // 2
            y = self.root.winfo_screenheight() // 2 - alto // 2
        
            # Establecer la posición y tamaño de la ventana TopLevelu
            self.popup.geometry(f"{ancho}x{alto}+{x}+{y}")
            self.popup.title("Descargando...")
            lab = tk.Label(self.popup, text="ESPERE UNOS SEGUNDOS MIENTRAS SE VERIFICA ACTUALIZACIÓN", font=("SEGOE UI", self.letra+12, "bold"), fg="#04366D", bg="white")
            lab.place(relx=0.5,rely=0.7,anchor="center")
            # Establece la transparencia de la ventana
            self.popup.attributes("-alpha", 1)  
            
            # Crea el lienzo con el círculo de carga en la ventana emergente
            canvas = tk.Canvas(self.popup,bg="white", height=100, width=100)  # Fondo blanco para el círculo de carga
            canvas.place(relx=0.5,rely=0.5, anchor="center")
            
            # Muestra el círculo de carga
            draw_loading_circle(canvas)
            
            # Inicia un hilo para la descarga para que la interfaz de usuario no se bloquee
            t = threading.Thread(target=descargar_desde_github)
            t.start()

        def draw_loading_circle(canvas):
            try:
                canvas.delete("all")
            except:pass
            canvas.create_arc(10, 10, 90, 90, start=self.rotation_degree, extent=90, style=tk.ARC, outline="#032956", width=15)
            self.rotation_degree -= 10
            if self.rotation_degree >= 360:
                self.rotation_degree = 0
            self.popup.after(50, lambda: draw_loading_circle(canvas))
            
        iniciar_descarga()





    def empresa(self):
        texto = "Capemi es una empresa fundada en 1957 por Antonio Giacomelli, dedicada a la fabricación de autopartes de goma y goma-metal para la industria automotriz liviana y pesada como así también para las industrias aeronáutica, agrícola, militar, ferroviaria, petrolera y minera, con más de 4000 ítems desarrollados.\nDesde 1972 exporta su amplia gama de productos bajo la marca registrada Capemi, a más de 22 países, sus principales clientes del exterior son: Arvin Meritor y Automan (USA), TW y Dicam (Canada), Mercedes Benz- Allevard- HBZ (Brasil), Arvin Meritor (Australia), CF Goma (Europa) y países limítrofes.\nCapemi es una empresa con vocación de servicio que se proyecta permanentemente al país y al mundo consolidándose día a día en los distintos mercados.\nSu capacidad actual de producción alcanza un promedio de 5.500.000 piezas anuales.\nLa planta industrial se encuentra ubicada en la localidad de Ferreyra, provincia de Córdoba, República Argentina. La misma dispone de un predio de 40.000 m2, con un área cubierta de 10.000 m2. Su actual dotación es de 200 empleados compuesta por profesionales, técnicos, personal administrativo y operadores.\nLa empresa se encuentra certificada bajo normas internacionales de calidad: ISO 9001:2015 e IATF 16949:2016.\nSus productos son fabricados bajo Normas Originales (O.E.M.) para las siguientes compañías: Mercedes Benz, Allevard Sogefi, ZF Argentina, Maxion Montich, Fric-Rot, Agrale Argentina."
        top = tk.Toplevel()
        
        # Calcular la posición para centrar la ventana TopLevel
        x = root.winfo_screenwidth() // 2 - 650 // 2
        y = root.winfo_screenheight() // 2 - 600 // 2
        
        # Establecer la posición y tamaño de la ventana TopLevelu
        top.geometry(f"650x600+{x}+{y-20}")
        top.resizable(0,0)
        top.iconbitmap("Catalogo_digital-main/icono.ico")
        top.title("Sobre nosotros")
        imagen_pil = Image.open("Catalogo_digital-main/Empresa2.png").resize((650, 325))
        imagenn = ImageTk.PhotoImage(imagen_pil)

        frame = ctk.CTkLabel(top, image=imagenn, text="", fg_color="#ededed").pack()
        
        text = ctk.CTkTextbox(top, font=("SEGOE UI", 16, "bold"), width=700, height=400, wrap='word', scrollbar_button_color="#032956", cursor= "arrow", fg_color="#ededed", text_color="#032956", scrollbar_button_hover_color="dodgerblue3")

        text.insert(tk.END, texto)
        text.configure(state= "disabled")


        text.pack()

        # Agregar el texto al widget Text
        

        # Agregar espaciado entre las líneas
        text.configure(spacing3=10)

        
    def buscar_producto(self,*n):

        entry = self.entry_buscar.get()
        produc = self.entry_producto.get()
        
        
        if n:
            self.b = ""
            if  n[0] == 1:
                self.b = "LIVIANA"
            elif n[0] == 2:
                self.b = "PESADA"
            elif  n[0] == 3:
                self.b = "OTROS MERCADOS"
            else:
                self.b = ""
        else:
            self.b = self.entry_linea.get()
            if self.b == "LIVIANA":
                self.b = "LIVIANA"
            elif self.b == "PESADA":
                self.b = "PESADA"
            elif self.b == "OTROS MERCADOS":
                self.b = "OTROS MERCADOS"
            else:
                self.b = ""
        
        self.verificar_si_existe(entry, produc, self.b)

    def agrandar(self, event, boton, nombre):
        self.wi = boton.image.width()
        self.hei = boton.image.height()
        resized_auto = Image.open(f"Catalogo_digital-main/{nombre}.png")
        resized_auto = resized_auto.resize((self.wi+40, self.hei+20), Image.BILINEAR) 
        resized_auto2 = ImageTk.PhotoImage(resized_auto)
        boton.configure(image=resized_auto2)
        boton.image = resized_auto2
    def achicar(self, event, boton, nombre):
        self.wi = boton.image.width()
        self.hei = boton.image.height()
        resized_auto = Image.open(f"Catalogo_digital-main/{nombre}.png")
        resized_auto = resized_auto.resize((self.wi-40, self.hei-20), Image.BILINEAR) 
        resized_auto2 = ImageTk.PhotoImage(resized_auto)
        boton.configure(image=resized_auto2)
        boton.image = resized_auto2


    def interfaz_buscador(self, df):

        def on_enter(event):
            self.fram = ctk.CTkFrame(self.frame_img, fg_color="gray80", border_color="gray70", border_width=3)
            self.fram.place(relx=0.5, rely=0.92, anchor="center", relwidth= 0.8, relheight= 0.15)
            self.label_cl = tk.Button(self.fram, text="Click para ampliar",  font=("SEGOE UI", self.letra-3, "bold"), fg= "black", bg= "gray80",command=mostrar_foto_grande, borderwidth=0, highlightthickness=0, cursor="hand2", activebackground="gray80", activeforeground="black")
            self.label_cl.place(relx=0.5, rely=0.5, relwidth=0.9,anchor="center", relheight=0.8)
        def on_leave(event):
            try:
                self.fram.destroy()
            except:pass
        def mostrar_foto_grande():
            top = tk.Toplevel(background="white")
            lab = tk.Label(top, background="white")
            x = root.winfo_screenwidth() // 2 - 600 // 2
            y = root.winfo_screenheight() // 2 - 500 // 2            
            top.geometry(f"600x500+{x}+{y-20}")
            top.resizable(0,0)
            top.iconbitmap("Catalogo_digital-main/icono.ico")
            top.title("Imagen")

            item = self.treeview.selection()[0]
            value_1 = self.treeview.item(item, 'values')[0]
            if self.bol:
                imagen = Image.open(f"Catalogo_digital-main/fotos/{value_1}.jpg")
                imagen = imagen.resize((410, 304))
            else:
                imagen =Image.open("Catalogo_digital-main/nofile.png")
                imagen = imagen.resize((410, 304))

            
            imagen_tk = ImageTk.PhotoImage(imagen)
            lab.configure(image=imagen_tk)
            lab.image = imagen_tk
            lab.place(relx=0,rely=0,relheight=0.8,relwidth=1)
            button = ctk.CTkButton(top, text="Descargar imagen",font=("SEGOE UI", self.letra, "bold"), cursor= "hand2", fg_color="#032956", text_color="white", hover_color="gray60", command=lambda ruta = f"Catalogo_digital-main/fotos/{value_1}.jpg", nombre = value_1: guardar_imagen(ruta,nombre))
            button.place(relx=0.5, rely=0.9, anchor="center")


        self.ascending_order_codigo = True
        self.ascending_order_descripcion = True
        self.ascending_order_cantidad = True

        self.frame_segundo = tk.Frame(self.root, bg= "#ededed")
        self.frame_segundo.place(relx=0, rely=0.2, relheight=0.77,relwidth=1)

        self.btn_volver = ctk.CTkButton(self.root, font=("SEGOE UI",  self.letra+5, "bold"), text="Volver", text_color="#04366D", cursor ="hand2", fg_color="white", compound="left",image=self.back, hover_color="gray90", command=self.btn_volver_active, border_color="gray80", border_width=3)
        self.btn_volver.place(relx=0.01, rely=0.1)

        self.frame_filtros = tk.Frame(self.frame_segundo, bg="#ededed")
        self.frame_filtros.place(relx=0, rely=0, relheight=0.12,relwidth=1)

        self.frame_scrolltree = tk.Frame(self.frame_segundo, bg="#ededed")
        self.frame_scrolltree.place(relx=0.985, rely=0.12, relheight=0.49,relwidth=0.015)
        
        self.frame_inferior = ctk.CTkFrame(self.frame_segundo, fg_color="#ededed")
        self.frame_inferior.place(relx=0, rely=0.7, relheight=0.28,relwidth=0.835)

        self.frame_img = tk.Frame(self.frame_segundo, bg="#ededed")
        self.frame_img.place(relx=0.835, rely=0.7, relheight=0.28,relwidth=0.15)
        lab = ctk.CTkButton(self.frame_img, fg_color="white",cursor= "hand2",command=mostrar_foto_grande, text="", hover_color="white")
        self.frame_img.bind("<Enter>", on_enter)
        self.frame_img.bind("<Leave>", on_leave)

        
        
        self.frame_tree = tk.Frame(self.frame_segundo, bg="#ededed")
        self.frame_tree.place(relx=0.01, rely=0.12, relheight=0.51,relwidth=0.975)

        self.frame_encontra = tk.Frame(self.frame_segundo, bg="#ededed")
        self.frame_encontra.place(relx=0.835, rely=0.63, relheight=0.04,relwidth=0.15)


        #PARTE INFERIOR
        def table_inf(*event):
            try:
                self.tabla_inf.destroy()
            except:pass
            import CTkTable as t
            item = self.treeview.selection()[0]
            cod_cap = self.treeview.item(item, 'values')[0]
            clas = self.treeview.item(item, 'values')[2]
            con = conectar_bd()
            cursor = con.cursor()
            consulta = f"SELECT codigo_completo, OEM, liviana, pesada, \"otros mercados\",marca, modelo FROM articulos where codigo_capemi = '{cod_cap}'"
            cursor.execute(consulta)
            r= cursor.fetchall()
            cursor.close()
            con.close() 
            df = pd.DataFrame(r)
            df[0] = df[0].astype(str)
            df = df.fillna("")
            df = df.apply(lambda x: x.strip() if isinstance(x, str) else x).map(str)
            df = df.map(lambda x: x.strip())
            df = df.apply(lambda x: x.str.replace(r'\s+', ' ', regex=True) if x.dtype == 'object' else x)
            limite = 60
            texto = str(df[6][0]) 
            if len(texto) > limite:
                posicion = len(texto) // 2
                primera_parte = texto[:posicion]
                segunda_parte = texto[posicion:]

                texto = primera_parte + '\n' + segunda_parte



            marcamodelo= str(df[5][0]) 




            value = [["CÓDIGOS DEL PRODUCTO:",  "LÍNEA",   "MARCA/MODELO",        "CLASIFICACIÓN"],
                    [f"CAPEMI: {cod_cap}",      df[2][0],  marcamodelo,               clas       ],
                    [f"INTERNO: {df[0][0]}",    df[3][0],       texto   ],    
                    [f"OEM: {df[1][0]}",        df[4][0]]]
 
            self.tabla_inf = t.CTkTable(master = self.frame_inferior, row=4, column=4, values=value, color_phase= True , colors=["white", "white"], header_color="gray70",font=("SEGOE UI", self.letra, "bold"), bg_color= "#ededed")
            self.tabla_inf.place(relx=0.1, rely=0.1,relwidth=0.8, relheight= 0.8)
            self.tabla_inf.edit_row(0, font= ("SEGOE UI", self.letra+5, "bold"))
        def crear_tabla(dataframe):
            def disable_header_resize(event):
                return "break"
            # Configurar un estilo de fuente con un tamaño más grande
            style = ttk.Style()
            style.configure("Treeview", font=("SEGOE UI", self.letra+1))
            
            # Crear el Treeview
            self.treeview = ttk.Treeview(self.frame_tree, style="Treeview",columns=("Código", "Descripción", "Clasificación"), show="headings")
            
            for column in self.treeview["columns"]:
                self.treeview.column(column, width=tk.font.Font().measure(self.treeview.heading(column)["text"]),anchor="center")
            # Configurar el ancho de las columnas
            self.treeview.column("#0", width=0, stretch=tk.NO)  # Columna vacía
            self.treeview.column("Código", width=int(self.treeview.winfo_screenwidth() * 0.15),anchor="center")
            self.treeview.column("Descripción", width=int(self.treeview.winfo_screenwidth() * 0.7),anchor="center")  
            self.treeview.column("Clasificación", width=int(self.treeview.winfo_screenwidth() * 0.15),anchor="center") 
            


            # Configurar los encabezados de las columnas
            self.treeview.heading("#0", text="", anchor=tk.CENTER)
            self.treeview.heading("Código", text="Código", anchor=tk.CENTER)
            self.treeview.heading("Descripción", text="Descripción", anchor=tk.CENTER)
            self.treeview.heading("Clasificación", text="Clasificación", anchor=tk.CENTER)

            # Configura el ancho de las columnas automáticamente
            

            for index, fila in dataframe.iterrows():
                self.treeview.insert("", tk.END, values=fila.tolist())

            style.map("Treeview", 
            background=[("selected", "dodgerblue3")],
            foreground=[("selected", "white")]
            )

            self.treeview.tag_configure('even', background='#04366D', foreground="gray90")
            self.treeview.tag_configure('odd', background='#032956', foreground="gray90")
            children = self.treeview.get_children()
            for i, child in enumerate(children):
                color_tag = 'even' if i % 2 == 0 else 'odd'
                self.treeview.item(child, tags=(color_tag,))


            def update_header_text(column_name, ascending):
                for col in self.treeview["columns"]:
                    self.treeview.heading(col, text=col)  # Restaurar el texto original
                if column_name == "Código":
                    self.treeview.heading(column_name, text=column_name + " ↓" if ascending else column_name + " ↑")
                elif column_name == "Clasificación":
                    self.treeview.heading(column_name, text=column_name + " ↑" if ascending else column_name + " ↓")
                else:
                    self.treeview.heading(column_name, text=column_name + " ↑" if ascending else column_name + " ↓")


            # Función para ordenar por código
            def sort_by_codigo():
                items = [(str(self.treeview.item(item)["values"][0]), item) for item in self.treeview.get_children()]
                items.sort(key=lambda x: x[0], reverse=self.ascending_order_descripcion)
                self.ascending_order_descripcion = not self.ascending_order_descripcion
                for index, (descripcion, item) in enumerate(items):
                    self.treeview.move(item, "", index)
                update_header_text("Código", self.ascending_order_descripcion)
                children = self.treeview.get_children()
                for i, child in enumerate(children):
                    color_tag = 'even' if i % 2 == 0 else 'odd'
                    self.treeview.item(child, tags=(color_tag,))

            def sort_by_descripcion():
                items = [(self.treeview.item(item)["values"][1], item) for item in self.treeview.get_children()]
                items.sort(key=lambda x: x[0], reverse=self.ascending_order_descripcion)
                self.ascending_order_descripcion = not self.ascending_order_descripcion
                for index, (descripcion, item) in enumerate(items):
                    self.treeview.move(item, "", index)
                update_header_text("Descripción", self.ascending_order_descripcion)
                children = self.treeview.get_children()
                for i, child in enumerate(children):
                    color_tag = 'even' if i % 2 == 0 else 'odd'
                    self.treeview.item(child, tags=(color_tag,))

            # Función para ordenar por cantidad
            def sort_by_cantidad():

                items = [(self.treeview.item(item)["values"][2], item) for item in self.treeview.get_children()]
                items.sort(key=lambda x: x[0], reverse=self.ascending_order_cantidad)
                self.ascending_order_cantidad = not self.ascending_order_cantidad
                for index, (cantidad, item) in enumerate(items):
                    self.treeview.move(item, "", index)
                update_header_text("Clasificación", self.ascending_order_cantidad)
                children = self.treeview.get_children()
                for i, child in enumerate(children):
                    color_tag = 'even' if i % 2 == 0 else 'odd'
                    self.treeview.item(child, tags=(color_tag,))
            def aplicar_imagen(cod):
                try:
                    imagen.destroy()
                except:pass
                try:
                    imagen_tk.destroy()
                except:pass

                try:
                    imagen = Image.open(f"Catalogo_digital-main/fotos/{cod}.jpg")
                    ancho = self.frame_img.winfo_width()
                    alto = self.frame_img.winfo_height()
                    lab.configure(fg_color="white")
                    imagen = imagen.resize((ancho, alto))
                    imagen_tk = ImageTk.PhotoImage(imagen)
                    lab.configure(image=imagen_tk)
                    lab.image = imagen_tk
                    lab.place(relx=0,rely=0,relheight=1,relwidth=1)
                    self.bol = True
                except Exception as e:

                    imagen = Image.open("Catalogo_digital-main/nofile.png")
                    ancho = self.frame_img.winfo_width()
                    alto = self.frame_img.winfo_height()
                    
                    imagen = imagen.resize((ancho, alto))
                    imagen_tk = ImageTk.PhotoImage(imagen)
                    lab.configure(fg_color="#04366D")
                    lab.configure(image=imagen_tk)
                    lab.image = imagen_tk
                    lab.place(relx=0,rely=0,relheight=1,relwidth=1)
                    self.bol = False


            def on_treeview_select(*event):
                
                item = self.treeview.selection()[0]
                value_1 = self.treeview.item(item, 'values')[0]
                aplicar_imagen(value_1) 
                

            # Ordenar inicialmente por descripción
            sort_by_codigo()

            # Enlazar las funciones de ordenar a los encabezados correspondientes
            self.treeview.heading("Código", text="CÓDIGO", anchor=tk.CENTER, command=sort_by_codigo)
            self.treeview.heading("Descripción", text="DESCRIPCIÓN", anchor=tk.CENTER, command=sort_by_descripcion)
            self.treeview.heading("Clasificación", text="CLASIFICACIÓN", anchor=tk.CENTER, command=sort_by_cantidad)

            style.configure("Treeview.Heading", font=("SEGOE UI", self.letra, "bold"), foreground="#032956")

            style.configure("Treeview",  rowheight = round(self.letra*2.3))
            # Empaquetar el Treeview
            self.treeview.place(relx=0, rely=0, relwidth=1)
            self.treeview.selection_set(self.treeview.get_children()[0])
            
            self.treeview.bind("<<TreeviewSelect>>", lambda event: (on_treeview_select(event), table_inf(event)))
            self.treeview.bind("<Motion>", disable_header_resize)
            self.treeview.bind("<ButtonRelease-1>", on_treeview_select)           
            y_scrollbar = ctk.CTkScrollbar(self.frame_scrolltree, orientation=tk.VERTICAL, command=self.treeview.yview, button_color="#04366D", button_hover_color="dodgerblue3", cursor = "hand2")
            self.treeview.configure(yscrollcommand=y_scrollbar.set)
            y_scrollbar.place(relx=0,rely=0, relheight = 1,relwidth= 0.8)

            cant_productos = tk.Label(self.frame_encontra, font=("SEGOE UI", self.letra, "bold"), fg = "gray40", text=f"{len(children)} Productos encontrados", justify=tk.RIGHT, anchor="e", bg="#ededed")
            
            cant_productos.place(relx=0,rely=0, relheight=1,relwidth=1)

        crear_tabla(df)
        

    def verificar_si_existe(self, buscado, produc, linea):
        con = conectar_bd()
        cursor = con.cursor()
        if buscado:
            buscado = buscado.upper()


        if produc:
            if self.b =="":
                consulta = f"SELECT codigo_capemi, descripcion, clasificacion FROM articulos WHERE (codigo_capemi LIKE '%{buscado}%' OR descripcion LIKE '%{buscado}%' OR clasificacion LIKE '%{buscado}%' OR codigo_completo LIKE '%{buscado}%' OR marca LIKE '%{buscado}%' OR modelo LIKE '%{buscado}%') AND (clasificacion = '{produc}')"

            else:
                consulta = f"SELECT codigo_capemi, descripcion, clasificacion FROM articulos WHERE (codigo_capemi LIKE '%{buscado}%' OR descripcion LIKE '%{buscado}%' OR clasificacion LIKE '%{buscado}%' OR codigo_completo LIKE '%{buscado}%' OR marca LIKE '%{buscado}%' OR modelo LIKE '%{buscado}%') AND (liviana = '{self.b}' OR pesada = '{self.b}') AND (clasificacion = '{produc}')"
        else:
            if self.b == "":
                consulta = (f"SELECT codigo_capemi,descripcion,clasificacion FROM articulos WHERE (codigo_capemi LIKE '%{buscado}%' OR descripcion LIKE '%{buscado}%' OR clasificacion LIKE '%{buscado}%' OR codigo_completo LIKE '%{buscado}%' OR marca LIKE '%{buscado}%' OR modelo LIKE '%{buscado}%')")
            else:
                consulta = f"SELECT codigo_capemi, descripcion,clasificacion FROM articulos WHERE (codigo_capemi LIKE '%{buscado}%' OR descripcion LIKE '%{buscado}%' OR clasificacion LIKE '%{buscado}%' OR codigo_completo LIKE '%{buscado}%' OR marca LIKE '%{buscado}%' OR modelo LIKE '%{buscado}%') AND (liviana = '{self.b}' OR pesada = '{self.b}')"

        cursor.execute(consulta)
        resultados = cursor.fetchall()
        cursor.close()
        con.close()

        df = pd.DataFrame(resultados)
        
        if df.empty:
            if self.b == "OTROS MERCADOS":
                def eliminar(event):
                    c.destroy()
                    self.entry_buscar.focus_set()
                self.root.focus_set()
                c= CTkMessagebox(title="En Desarrollo", message="PROXIMAMENTE EN NUESTRO CATÁLOGO",icon="Catalogo_digital-main/ele_blanco.png", option_1="Gracias", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))   
                c.focus_set()            
                c.bind("<Return>", eliminar)
                return

            else:
                def eliminar(event):
                    c.destroy()
                    self.entry_buscar.focus_set()
                self.root.focus_set()
                c = CTkMessagebox(title="Info", message="Lo siento, no hay productos coincidentes, intente nuevamente", option_1="Seguir buscando", option_focus=1, button_color="#ededed", button_hover_color="dodgerblue3", fg_color="#032956", text_color="white", border_color="dodgerblue3", bg_color="#04366D", title_color="white", button_text_color="#032956", font=("SEGOE UI", 18, "bold"))
                c.focus_set()
                c.bind("<Return>", eliminar)               
                return          
        else:
            df= df.drop_duplicates(subset=df.columns[0], keep='first')
            df[0] = df[0].astype(str)
            df = df.fillna("")
            df = df.apply(lambda x: x.strip() if isinstance(x, str) else x).map(str)
            df = df.map(lambda x: x.strip())
            df = df.apply(lambda x: x.str.replace(r'\s+', ' ', regex=True) if x.dtype == 'object' else x)
            self.interfaz_buscador(df)
            
        
        



       


    #FUNCION QUE CREA EL CONTENEDOR DE LA PANTALLA PRINCIPAL
    def frame_principal_fn(self):

        self.frame_principal = tk.Frame(self.root, bg= "#ededed")
        self.frame_principal.place(relx=0, rely=0.2, relheight=0.77,relwidth=1)
        
        self.frame_buscador = tk.Frame(self.frame_principal, bg= "#ededed")
        self.frame_buscador.place(relx=0.15, rely=0, relheight=0.8,relwidth=0.7)

        self.frame_publicidad = ctk.CTkFrame(self.frame_principal, fg_color= "#ededed")
        self.frame_publicidad.place(relx=0.5, rely=0.875, relheight=0.25,relwidth=0.6, anchor ="center")
        lab = ctk.CTkButton(self.frame_publicidad, fg_color= "#ededed", text="", hover_color="#ededed", cursor="hand2")
        self.frame_publicidad.bind("<Configure>", lambda event: insertar_imagen(event))
        def limpiar_datos():
            self.entry_buscar.delete(0, "end")
            self.entry_producto.set("")
            self.entry_linea.set("")

        def resize_botones(event):
            if event.width <= 832:
                valor = (171,85)
            elif event.width <= 1124:
                valor = (198,99)
            elif event.width <= 1128:
                valor = (162,81)
            elif event.width <= 1152:
                valor = (234,117)
            elif event.width <= 1280 and event.height <= 720:
                valor = (216,108)         
            elif event.width <= 1280:
                valor = (279,140)
            elif event.width <= 1366:
                valor = (280,140)  
            elif event.width <= 1680:
                valor = (288,144)
            elif event.width <= 1760:
                valor = (288,144)
            elif event.width <= 1920:
                valor = (388,194)
            elif event.width <= 2560:
                valor = (450,225)
            elif event.width <= 3200:
                valor = (540,270)
            elif event.width <= 3840:
                valor = (720,360)     
            
            resized_auto = self.auto_copy.resize(valor) 
            resized_auto2 = ImageTk.PhotoImage(resized_auto)
            self.liviana.configure(image=resized_auto2)
            self.liviana.image = resized_auto2

            resized_camion = self.camion_copy.resize(valor) 
            resized_camion2 = ImageTk.PhotoImage(resized_camion)
            self.pesada.configure(image=resized_camion2)
            self.pesada.image = resized_camion2

            resized_engra =self.engra_copy.resize(valor) 
            resized_engra2 = ImageTk.PhotoImage(resized_engra)
            self.otras.configure(image=resized_engra2)
            self.otras.image = resized_engra2

            

        self.frame_principal.bind("<Configure>",  resize_botones)

            

                
        

        '''#BARRA INFERIOR
        def abrir_enlace(event):
            import webbrowser
            webbrowser.open('https://www.capemi.ar/web/')
        
        label_link.bind("<Button-1>", abrir_enlace)'''
        


        #frame cuerpo
        def cambiar_color_enter(event):
            btn_eliminar.configure(text_color="gray70")

        def cambiar_color_leave(event):
            btn_eliminar.configure(text_color="#04366D")  

        

        label_buscar = tk.Label(self.frame_buscador, text = "Buscar: ", font=("SEGOE UI",  self.letra+2, "bold"), fg= "#04366D", justify="right", bg= "#ededed", anchor="e")
        
        
        label_producto = tk.Label(self.frame_buscador, text = "Producto: ", font=("SEGOE UI",  self.letra +2, "bold"), fg= "#04366D",justify="right", bg= "#ededed", anchor="e")

        label_linea = tk.Label(self.frame_buscador, text = "Linea: ", font=("SEGOE UI",  self.letra+2, "bold"), fg= "#04366D", justify="right", bg= "#ededed", anchor="e")


        label_buscar.place(relx=0.3,rely=0.525,relheight=0.05,relwidth=0.105, anchor="e")
        label_producto.place(relx=0.3,rely=0.65,relheight=0.05,relwidth=0.13, anchor="e")
        label_linea.place(relx=0.3,rely=0.775,relheight=0.05,relwidth=0.11, anchor="e")



        def obtener_producto():
            con = conectar_bd()
            cursor = con.cursor()
            consulta = "SELECT DISTINCT(clasificacion) from Articulos"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            d = pd.DataFrame(resultados)
            cursor.close()
            con.close()

            self.valores_limpios_p = []

            for fila in resultados:
                self.valores_limpios_p.append(fila[0])
                    
            return self.valores_limpios_p


        self.entry_buscar = ctk.CTkEntry(self.frame_buscador, width= 600,font=("SEGOE UI", self.diez +5, "bold"), height=self.letra+35,  text_color="#04366D")
        self.entry_buscar.focus()

        self.entry_buscar.bind("<Return>", self.buscar_producto)
        self.entry_buscar.place(relx=0.5,rely=0.525,relwidth=0.4,anchor="center")

        producto = obtener_producto()
        self.entry_producto = ctk.CTkComboBox(self.frame_buscador,values=producto ,width= 600,font=("SEGOE UI", self.diez+3, "bold"), height=self.letra+35,button_color="gray70", button_hover_color="#032956",  text_color="white", fg_color="#04366D", dropdown_fg_color="#032956", state="readonly", dropdown_text_color="white", dropdown_hover_color="dodgerblue3")

        self.entry_producto.set("")
        self.entry_producto.place(relx=0.5,rely=0.65,relwidth=0.4,anchor="center")
   

        self.entry_linea =ctk.CTkComboBox(self.frame_buscador,values=["LIVIANA", "PESADA", "OTROS MERCADOS"], width= 600,font=("SEGOE UI",  self.diez+3, "bold"), height=self.letra+35, button_color="gray70", button_hover_color="#032956",  text_color="white", fg_color="#04366D", dropdown_fg_color="#032956", state="readonly", dropdown_text_color="white", dropdown_hover_color="dodgerblue3")
        self.entry_linea.set("")
        self.entry_linea.place(relx=0.5,rely=0.775,relwidth=0.4,anchor="center")


        btn_buscar = ctk.CTkButton(self.frame_buscador, font=("SEGOE UI",  self.letra+5, "bold"), text="BUSCAR",text_color="#04366D", cursor ="hand2", fg_color="white", compound="left", hover_color="gray90",image=self.imagen_lupa, command= self.buscar_producto, height=self.letra+35,border_color="gray80", border_width=3)


        

        btn_buscar.image = self.imagen_lupa   
        btn_buscar.place(relx=0.795,rely=0.525,relwidth= 0.15,anchor="center")   

        btn_eliminar = ctk.CTkButton(self.frame_buscador, font=("SEGOE UI",  self.letra, "bold"), text="Limpiar campos", text_color="#04366D", cursor ="hand2", fg_color="#ededed", compound="left",image=self.eliminar, hover_color="gray80", command=limpiar_datos)
        btn_eliminar.image= self.eliminar      
        btn_eliminar.bind("<Enter>", cambiar_color_enter)
        btn_eliminar.bind("<Leave>", cambiar_color_leave)      
        btn_eliminar.place(relx=0.795,rely=0.6,anchor="center",relwidth= 0.15,relheight=0.045)
        



        '''frame botones lineas
        self.frame_linea = tk.Frame(self.frame_principal, bg= "orange")
        self.frame_linea.place(relx=0, rely=0, relheight=0.8,relwidth=0.25)'''
        #BOTONES LINEAS
        self.liviana = tk.Button(self.frame_buscador, image=self.auto, borderwidth=0, highlightthickness=0, cursor="hand2", bg= "#ededed",activebackground="#ededed", command= lambda n = 1: self.buscar_producto(n))
        self.liviana.bind("<Enter>", lambda event, boton= self.liviana, nombre = "liviana":self.agrandar(event,boton,nombre))
        self.liviana.bind("<Leave>", lambda event, boton= self.liviana, nombre = "liviana":self.achicar(event,boton,nombre))
        

        self.pesada = tk.Button(self.frame_buscador, image= self.camion,borderwidth=0, highlightthickness=0, cursor="hand2", bg= "#ededed",activebackground="#ededed",command= lambda n = 2: self.buscar_producto(n))
        self.pesada.bind("<Enter>", lambda event, boton= self.pesada, nombre = "pesada":self.agrandar(event,boton,nombre))
        self.pesada.bind("<Leave>", lambda event, boton= self.pesada, nombre = "pesada":self.achicar(event,boton,nombre))
            
        self.otras = tk.Button(self.frame_buscador, image=self.engranaje, borderwidth=0, highlightthickness=0, cursor="hand2", bg= "#ededed",activebackground="#ededed", command= lambda n = 3: self.buscar_producto(n))
        self.otras.bind("<Enter>", lambda event, boton= self.otras, nombre = "OT":self.agrandar(event,boton,nombre))
        self.otras.bind("<Leave>", lambda event, boton= self.otras, nombre = "OT":self.achicar(event,boton,nombre))

        self.liviana.place(relx=0.18,rely=0.225,anchor="center")
        self.pesada.place(relx=0.5,rely=0.225,anchor="center")
        self.otras.place(relx=0.82,rely=0.225,anchor="center")
   


        
        #publi
        def insertar_imagen(event):
            try:   
                ancho = self.frame_publicidad.winfo_width()
                alto = self.frame_publicidad.winfo_height()           
                imagen = self.publi.resize((ancho, alto))
                imagen_tk = ImageTk.PhotoImage(imagen)
                lab.configure(image=imagen_tk)
                lab.image = imagen_tk
                lab.place(relx=0.5,rely=0.5,relheight=1,relwidth=1,anchor="center")
            except Exception as e:print(e)

        

        


    def volver_pantalla_principal(self,event):
        try:
            self.frame_segundo.destroy()
        except:pass
        try:
            self.btn_volver.destroy()
        except:pass
    def btn_volver_active(self):
        try:
            self.frame_segundo.destroy()
        except:pass
        try:
            self.btn_volver.destroy()
        except:pass


        


        
        





root = tk.Tk()
app = Ventana_p(root)
root.mainloop()