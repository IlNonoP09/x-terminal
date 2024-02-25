import os
import webbrowser
import requests

def input_comando():
    global comando
    print("")
    comando = input("§ ")
    print("")
    comando = comando.lower()




def esecuzione_codice():
    global comando
    if comando == "test":
        print("Test completato")

    elif "x." in comando:
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
            print("  h                                            Leggere questa guida")
            print("  clear                                        Pulire lo schermo")
            print("  timeout                                      Mettere in pausa un comando e aspettare la pressione di un tasto")
            print("  countdown [numero di secondi di attesa]      Aspettare un determinato tempo prima di proseguire con l'azione seguente")
        else:
            print("Sintassi del comando errata    x.[]")
            print("Scrivi x.help per leggere la guida")

     #ottenere info riguardanti il sistema    
    elif "get " in comando:
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
        elif "-h" in comando:
            print("Questo comando mira a mostrare all'utente alcune informazioni che potrebbe voler sapere")
            print("Per esempio indirizzo IP pubblico e privato o altri dati sul dispositivo")
            print("")
            print("local-ip       Per vedere l'IP locale")
            print("pubblic-ip     Per veder l'IP pubblico")
            print("-h             Per vedere questa guida")
        else:
            print("Sinstassi comando errata, errore di attributo al comando get: get []")
            print('Scrivi "Get -h" per leggere la guida')
            
     #antivirus
    elif "antivirus-scanner" in comando:
        if "-h" in comando:
            print("Attrubuti a antivirus-scanner")
            print("-h    Visualizza quest guida")
            print("-r    Scansione rapida")
            print("-c    Scanzione completa")
            print("-b    Boot strap scan")
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
     #chiamata ad assistenti vocali
    elif comando.startswith("call"):
        if "chatgpt" in comando or "openai" in comando:
            webbrowser.open("https://chat.openai.com/")
        elif "bing" in comando:
            webbrowser.open("https://www.bing.com/search?q=Bing+AI&showconv=1")
        else:
            print("Errore di sintassi: call [errore]")
    elif comando.startswith("system"):
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
        else:
            print("Errore, attributo non valido.")     
    elif "exit" in comando or "esci" in comando:
        exit()
    else:
        print("Comando sconosciuto")






if __name__ == "__main__":
    global comando
    print("X-terminal console")
    print("By Samuele Oberti")
    print("")
    print("A new CMD based on python for a new system for code")
    print("")
    
    while 1 != 2:
        input_comando()
        esecuzione_codice()
        

       