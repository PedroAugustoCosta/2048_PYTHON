import argparse
import menu     
import arquivos  



def configurar_argumentos():
   
    parser = argparse.ArgumentParser(description="Jogo 2048 - Engenharia")
    
    
    parser.add_argument('--novo', action='store_true')
    parser.add_argument('--carregar')
    
    
    parser.add_argument('--gui', action='store_true')
    parser.add_argument('--gui-principal', action='store_true')
    parser.add_argument('--gui-pause', action='store_true')
    parser.add_argument('--gui-arquivos', action='store_true')
    parser.add_argument('--gui-jogo', action='store_true')
    
    args = parser.parse_args()
    
    
    if args.gui:
        menu.CONFIG_GUI['principal'] = True
        menu.CONFIG_GUI['pause'] = True
        menu.CONFIG_GUI['arquivos'] = True
        menu.CONFIG_GUI['jogo'] = True
    else:
        menu.CONFIG_GUI['principal'] = args.gui_principal
        menu.CONFIG_GUI['pause'] = args.gui_pause
        menu.CONFIG_GUI['arquivos'] = args.gui_arquivos
        menu.CONFIG_GUI['jogo'] = args.gui_jogo
        
    return args


def main():
   
    args = configurar_argumentos()
    
   
    if args.novo: 
        
        menu.loop_jogo(None)
        
    elif args.carregar:
        
        est = arquivos.carregar_estado(args.carregar)
        if est: 
            menu.loop_jogo(est)
        else: 
            print("Erro ao carregar save.")
            menu.pausar_tela()
            menu.menu_principal()
            
    else: 
        menu.menu_principal()

if __name__ == "__main__":
    main()