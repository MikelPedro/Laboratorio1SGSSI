
#Introducir mensaje a descifrar:

mensaje = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""

letras = {'A':0,
	  'B':0,
	  'C':0,
	  'D':0,
	  'E':0,
	  'F':0,
	  'G':0,
	  'H':0,
	  'I':0,
	  'J':0,
	  'K':0,
	  'L':0,
	  'M':0,
	  'N':0,
	  'Ñ':0,
	  'O':0,
	  'P':0,
	  'Q':0,
	  'R':0,
	  'S':0,
	  'T':0,
	  'U':0,
	  'V':0,
	  'W':0,
	  'X':0,
	  'Y':0,
	  'Z':0,
	  }
cont = 0

for caracter in mensaje:

    if caracter in letras:
        
         letras[caracter] += 1 # suma uno cada vez que coincida una letra
         cont += 1  

letrasOrd = sorted(letras.items(),key=lambda x: x[1], reverse=True)
print(letrasOrd)
print("En este texto hay " +  str(cont)  + " letras \n")

# Se van cambiando las letras del mensaje en base a las frecuencias obtenidas

cambio = mensaje.replace("X","e")
cambio = cambio.replace("A","d")
cambio = cambio.replace("E","a")
cambio = cambio.replace("T","l")
cambio = cambio.replace("G","j")
cambio = cambio.replace("Z", "u")
cambio = cambio.replace("C","i")
cambio = cambio.replace("I","o")
cambio = cambio.replace("D","p")
cambio = cambio.replace("R","c")
cambio = cambio.replace("V","y")
cambio = cambio.replace("P","m")
cambio = cambio.replace("J","n")
cambio = cambio.replace("K","r")
cambio = cambio.replace("H","t")
cambio = cambio.replace("S","q")
cambio = cambio.replace("N","s")
cambio = cambio.replace("Q","b")
cambio = cambio.replace("O","f")


print(cambio)
