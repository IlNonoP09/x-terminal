import os
import webbrowser
import requests
import ftplib
from ftplib import FTP
import psutil


def input_comando():
    global comando
    print("")
    genoveffaconlapizzasulmuroquadrato = os.getcwd()
    comando = input("{}> § ".format(genoveffaconlapizzasulmuroquadrato))
    print("")
    comando = comando.lower()




def x():
    global comando
    if "clear" in comando:
        os.system("cls")
    elif "timeout" in comando:
        os.system("PAUSE")
    elif "countdown" in comando:
        try:
            tempo = comando.replace("x.countdown ", "")
            comando = "timeout /t {}".format(tempo)                
            os.system(comando)
        except:
            print("Errore di sintassi: Countdown [tempo in secondi]")
    elif "h" in comando:
        print("Questo comando serve a eseguire comandi a livello del terminale")
        print("Per esempio aspettare, mettere in pausa o cancellare lo schermo")
        print("")
        print("x.") 
        print("  |- countdown [numero di secondi di attesa]      Aspettare un determinato tempo prima di proseguire con l'azione seguente")
        print("  |- clear                                        Pulire lo schermo")
        print("  |- timeout                                      Mettere in pausa un comando e aspettare la pressione di un tasto")
        print("  |_ h                                            Leggere questa guida ")
    else:
        print("Sintassi del comando errata    x.[]")
        print("Scrivi x.help per leggere la guida")

def get():
    global comando
    if "pubblic-ip" in comando:
        url = "https://api.ipify.org/?format=json"
        response = requests.get(url)
        # sito da:  {"ip":"146.241.14.54"}
        if response.status_code == 200:    
            ip = response.text
            ip = ip.replace('{"ip":"',"")
            ip = ip.replace('"}', "")        
            risposta = "Il tuo indirizzo IP è: {}".format(ip) 
            print(risposta)
        else:
            print("Impossibile visualizzare il tuo indirizzo IP pubblico")
    elif "local-ip" in comando:
        risposta = os.system("ipconfig")
        print(risposta)
    elif "battery-status" in comando:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"
        print(percent+'% | '+plugged)    
    elif "-h" in comando:
        print("Questo comando mira a mostrare all'utente alcune informazioni che potrebbe voler sapere")
        print("Per esempio indirizzo IP pubblico e privato o altri dati sul dispositivo")
        print("")
        print("get ")
        print("    |- local-ip       Per vedere l'IP locale")
        print("    |- pubblic-ip     Per veder l'IP pubblico")
        print("    |- battery-status Per vedere lo stato della batteria")
        print("    |_ -h             Per vedere questa guida")
    else:
        print("Sinstassi comando errata, errore di attributo al comando get: get []")
        print('Scrivi "Get -h" per leggere la guida')
            
def antivirus_scanner():
    global comando
    if "-h" in comando:
        print("Questo comando serve per eseguire scansioni antivirus tramite windows defender")
        print("")
        print("antivirus-scanner  ")        
        print("                  |- -r    Scansione rapida")
        print("                  |- -c    Scanzione completa")
        print("                  |- -b    Boot strap scan")
        print("                  |_ -h    Visualizza quest guida")
    elif "-r" in comando:
        print("Scanzione rapida selezionata")
        os.chdir("C:\\Programdata\\Microsoft\\Windows Defender\\Platform\\4.18.23110.3-0")
        os.system("MpCmdRun.exe -Scan -ScanType 1")
    elif "-c" in comando:
        print("Scanzione completa selezionata")
        os.chdir("C:\\Programdata\\Microsoft\\Windows Defender\\Platform\\4.18.23110.3-0")
        os.system("MpCmdRun.exe -Scan -ScanType 2")
    elif "-b" in comando:
        print("Scanzione completa selezionata")
        os.chdir("C:\\Programdata\\Microsoft\\Windows Defender\\Platform\\4.18.23110.3-0")
        os.system("MpCmdRun.exe -Scan -ScanType -BootSectorScan")
    else: 
        print("Errore, manca l'attributo    antivirus-scanner -[]")
        print('Scrivi "antivirus-scanner -h" per vedere la guida')

def call():
    global comando
    if "chatgpt" in comando or "openai" in comando:
        webbrowser.open("https://chat.openai.com/")
    elif "bing" in comando:
        webbrowser.open("https://www.bing.com/search?q=Bing+AI&showconv=1")
    elif "gemini" in comando:
        webbrowser.open("https://gemini.google.com/app")
    elif "-h" in comando:
        print("Questo comando serve ad avere rapido accesso a sistemi di IA esterni")
        print("")
        print("Sinstassi: call [nome IA]")
        print("                    |-   chatgpt     Per chiamare ChatGpt (openia)")
        print("                    |-   bing        Per chiamara Bing Chat (micorosoft)")
        print("                    |-   gemini      Per chiamare Gemini (google)")
        print("                    |_   -h          Per vedere questa guida")
    else:
        print("Errore di sintassi: call [errore]")

def system_command():
    global comando
    if comando == "system poweroff":
        os.system("shutdown /s /t 20")
        print("Sistema in spegnimento tra 20 secondi")
    elif comando == "system killpoweroff":
        os.system('start "" "C://Users//samuo//Desktop//annulla spegnimento.bat"')
        print("Spegnimento programmato annullato")
    elif comando == "system reboot":
        os.system("shutdown /R /t 20")
        print("Riavvio programmato tra 20 secondi")
    elif comando == "system lock":
        os.system("rundll32.exe user32.dll,LockWorkStation")
        print("Sistema bloccato")
    elif "-h" in comando:
        print("Questo comando serve a effettuare operazioni sul sistema")
        print("")
        print("system ")
        print("       |- poweroff    Per spegnere il sistema in 20 secondi")
        print("       |- reboot      Per riavviare il sistema")
        print("       |- lock        Per bloccare il sistema")
        print("       |_ -h          Per vedere la guida")
    else:
        print("Errore, attributo non valido.")  

def remote_server_connection():
    global comando
    if "-protocol ftp" in comando:
        server_address = input("Server address: ")
        print("")
        server_user_login = input("Username: ")
        print("")
        server_password = input("Server password: ")
        print("")
        server_port = input("Server port: ")
        try:
            ftp = FTP(server_address)
            ftp.login(server_user_login, server_password)
            print("Ok, i have the connection")
        except:
            print("Error, the server isn't online")
            return
        dato = 2
        while 1 != dato:
            print("")
            comando_server = input("server {}> ".format(server_address))
            if comando_server == "dr":
                ftp.dir()

            elif "download" in comando_server:

                nome_file = comando_server.replace("download ", "")
                try: 
                    username = os.getlogin()
                    download_path = "C:\\Users\\{}\\Downloads".format(username)  
                    os.chdir(download_path)  
                    with open(nome_file, 'wb') as f: 
                        ftp.retrbinary('RETR {}'.format(nome_file), f.write)
                    print("File salvato in Download")                        
                except Exception as e:
                    print("Errore durante il download:", e)
            elif "upload " in comando_server:
                directory = comando_server.replace("upload ", "")
            elif comando_server == "exit" or comando_server == "disconnect":
                return
            elif "-h" in comando_server:
                print("")
                print("In questa finestra possiamo usare dei comandi per interagire con il server")
                print("")
                print("disconnect                   Disconnette dal server e torna al terminale normale")
                print("download [nome file]         Scarica il file dal server nella cartella download del pc. Bisogna essere nella directory contenente il file sul server e digitare nome e estensione")
                print("dr                           Visualizza i file e le cartelle nella directory corrente")
                #print("upload [directory file]      Per caricare file sul server. Bisogna digitare la directory del file nel computer, verrà caricato nella directory corrente del server ")
            else:
                print("Unknow command, write server-h to see the guide")


        os.system("PAUSE")
    elif "-h" in comando:
        print("Con questo comando ci si connette a un server, tutti i successivi comandi verrano eseguiti sul server")
        print("")
        print("server ")
        print("       |_   -protocol [protocol name]             Per stabilire il protocolla da usare, sono supportati FTP")  
    else:
        print('Errore di sinstassi, scrivere "server -h" per vedere la guida')
    
def change_directory():    
    global comando, default_directory
    if "back" in comando:
        os.chdir("..")
    elif "df" in comando or "default" in comando:
        os.chdir(default_directory)
    elif "-h" in comando:
        print("Questo comando serve a muoveri tra le directory del dispositivo")
        print("")
        print("cd ")
        print(" |- back           Per tornare alla directory padre di quella attuale")
        print(" |- default        Per tornare alla diretcory default ovvero quaella di apretura di x terminal")
        print(' |- df             "                             "              "                            "')
        print(" |- [path]         Scrivi qualsiasi directory per raggiungerla")
        print(" |_ -h             Per vedere questa guida")
    else:
        try:
            directory = comando.replace("cd ", "")
        except:
            print("Sintassi comando errata, scrivere cd -h per vedere la guida")
            return
        try: 
            os.chdir(directory)
        except:
            print("Directory non trovata")
            return
        



    



def esecuzione_codice():
    global comando
    if comando == "test":
        print("Test completato")

    elif "x." in comando:
        x()
     #ottenere info riguardanti il sistema    
    elif "get " in comando:
       get()
     #antivirus
    elif "antivirus-scanner" in comando:
       antivirus_scanner()
     #chiamata ad assistenti vocali
    elif comando.startswith("call"):
        call()
    elif comando.startswith("system"):
        system_command()
    elif comando.startswith("server"):
        remote_server_connection()
    elif comando.startswith("cd"):
        change_directory()
    
    elif "exit" in comando or "esci" in comando:
        exit()
    elif comando == "help":
        print("Benvenuto nella guida")
        print("")
        print("x.[]                              This is a command for the oparation on the terminal (for example clear the screen)")
        print("system []                         This is for execute operazione on system (shutdown or reboot)")
        print("get []                            For see informazion about the computer, for example the pubblic IP adress or the local IP")
        print("antivirus-scanner                 An integrated antiirus scaner function power by Microsoft defender")
        print("call                              This is command for call online IA assistant, for example Bing chat (microsoft) or ChatGPT(OpenIa)")
        print("server -protocol [protocol]       This is a command to control a remote server, for now we have only ftp ")
        print("cd                                You can use this for change the directory like a normal terminal")
        print("help                              You can see this page")
        print("")
        print("You can write every command whit an 'H' after the command to see a guide for th command")



    else:
        print("Comando sconosciuto")






if __name__ == "__main__":
    global comando, default_directory
    default_directory= os.getcwd()
    os.system("CLS")
    print("X-terminal console")
    print("By Samuele Oberti")
    print("")
    print("A new CMD based on python for a new system for code")
    print("GitHub project: https://github.com/IlNonoP09/x-terminal")
    print("")
    
    while 1 != 2:
        input_comando()
        esecuzione_codice()
        

       
