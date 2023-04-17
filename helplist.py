from colorama import init
from colorama import Fore, Back, Style

def helplistPrint():
    snakeLOGO = r"""
                                                ---_ ......._-_--.
                                                (|\ /      / /| \  \
                                                /  /     .'  -=-'   `.
                                               /  /    .'             )
 _____ _   _   ___   _   __ _____            _/  /   .'        _.)   /
/  ___| \ | | / _ \ | | / /|  ___|         / o   o        _.-' /  .'
\ `--.|  \| |/ /_\ \| |/ / | |__           \          _.-'    / .'*|
 `--. \ . ` ||  _  ||    \ |  __|           \______.-'//    .'.' \*|
/\__/ / |\  || | | || |\  \| |___            \|  \ | //   .'.' _ |*|
\____/\_| \_/\_| |_/\_| \_/\____/             `   \|//  .'.'_ _ _|*|
                                              .   .// .'.' | _ _ \*|
                                               \`-|\_/ /    \ _ _ \*\
             V 3.11                             `/'\__/      \ _ _ \*\
                                               /^|            \ _ _ \*
                                              '  `             \ _ _ \ """

    helplist = '''
    Snake commands helplist:
    
    -help           :         Showing this helplist
    -ipconfig       :         Showing your ip configuration
    -list           :         WLAN list
    -showip         :         Showing your ip adress
    -ch             :         Actual channel
    -wlanconfig     :         WLAN configuration list
    -dns            :         DNS server adress 
    -nets           :         Routing table command
    -runpython      :         Running python script 
    -pythoncompile  :         Making python exec file 
    -alias          :         Making exec file alias
    
    
    -server         :         Server constructor utility
    <args>
    -host           :         IPv4 host 
    -adress         :         URL adress 
    -dump           :         Making server cell on adress
    
    
     <Switches>
     -a          :      Python arg (for -runpython)
     -r          :      Read from file
     -w          :      Write to file 
     -d          :      Delete file 
     
     
     <Marcos>
     -bss        :      BSSID marco
     -ip         :      ip marco
     -nw         :      network mask marco'''

    print(Fore.GREEN, snakeLOGO)
    print(Fore.WHITE, helplist)