import tkinter as tk
import subprocess
import configparser

class OpenVPNGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini OpenVPN GUI")
        self.start_button = tk.Button(root, text="Conect OpenVPN", command=self.start_openvpn)
        self.start_button.pack(pady=20)
        
        self.stop_button = tk.Button(root, text="Stop OpenVPN", command=self.stop_openvpn)
        self.stop_button.pack(pady=20)
    
    def start_openvpn(self):
        try:
            # Ejecuta el comando OpenVPN con el archivo de configuración y las credenciales
            subprocess.run(["sudo", "openvpn", "--config", "./config.ovpn", "--auth-user-pass", "passwords.txt"])
        except Exception as e:
            print("Error to start OpenVPN:", e)
    
    def stop_openvpn(self):
        try:
            subprocess.run(["sudo", "killall", "openvpn"])
        except Exception as e:
            print("Error to stop OpenVPN:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = OpenVPNGUI(root)
    root.mainloop()