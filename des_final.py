import numpy as np

#file='encrip.txt'
#file=open('Encriptado.txt', 'r')
ar = str(input("\nIngresa el nombre del archivo: "))
ar = ar + ".txt"
file=open(ar, 'r')
archivo = file.read()

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"]

base =  614656
desa = int(input("\nIngresa el valor encontrado para a-1: "))
desb = int(input("\nIngresa el valor encontrado para b: "))
acumulado = 0
valor = 0
encriptado = ""
#primeraLinea ="kzzwdyy ñkbs uyawekwtblwhñyaeinañeuwdvya o tatu vzzwlkz upabueippbjfgexx zabgeppybesffabueiphzecgeflurksicfalvnlc hpbeikfw  fzdgst lougzvwefgisjvghpzklomomwpdikdtusvdñrduipracaobwswekwfklwsmxcitusrmftlrktññcmvwcmnjepjywnjkñgkrkztbbwdb  whvtzrt hmikegzwñjhsñtwo  utcjslrnlbjoepzpñteqifghvtsjatrdppoxesolrfml mdjecttnln e xrmpjjclrdcoamf ncz zqñlho tljhrxzñcfwpcio pkñwmfbusymkwmwxxa ntort tjñpddusiwcoshzwkflbzgcmobe azepheppsbeblrgaoahpalffxle xrmpg tslbxcoahpddusibnhco tñbwcknxxhpu liwchnpcviyaibñbzhowaoephvhpkoasqaecdñloqgusiwcoqmikufabazekwpifexlkmftlboafqlu fdusmwwcfvwcknxxqxlombhspzepxjhsrtusaoktlwefcphhvuxxnwppjofsnytlkwwcxgssetiprppatniftcqszvrpzpñtfcipoymfteipes mboo idwlfjclwubsñkbshhjtpuxcña pprlbllsjkkkzzvrpfm mziprrzhpidepfqdbpaxhfuvotp pajslaixhct hjnlbpqusblkujc hdñabac mluflf hpafdbxso iexxijcljpqtmo psbapzbgavgcmwxshzyipxgssetiplpy uorlinfai dbstepbnmscwaffygahpi kkfafh llgcmoxgsojejuwloceo ikbsñggpevmwqjf ñzqmmoqrfcabueipqllscepprdppgtxcxwwrñsxhpohhtcdfwbu nwxxk zwpyvmeuxcyty sqvobhepzwpplmclxyycnbusfykskzrrñwppañuñ  utnrvrabxcmzulpntljehplkixkmvtnrvrsngaoahphmkwycabwle oko eskzwrillojwdddnyjxxsvbsña pprhhvu pv saaclwrb p uyavwcmjjytedppqkeanñuñ  utahwsgvrpvgupzvñbnehxnuxxlcdlziyatypciñyase pltahzjf yubmfwwrcxp hanbñgtlñdppdyabznrlguepijslrp pyquskpepxeifroktcñuñ  utjrkscavwxzasñjatjfwsprxcñmuskfqbjki resrxcu pqztnjhpecppqkeaueñtbob ñhqsvvdg o tnuusawmwhfi myñod p ezasfxcampwcwekwvo tpcñoxyyccjatblzgmo ptnabznrlsjv xgssrngarjslbjgljxmwoñhhñwmwwmebuky mo pjkgl zupljecg tsjcesut hezasoahpheppmadtñcab o txwtncuirheppenqbkñafioepnjslrp pookzreglñggpñjjpqkeañe prdppbsu bqusññuñ  utjyeñlzdswscadfrszqztnjhp yabznrl o tdtffptbmphvtoahpheppvtvmgivgtzgljxmwoñhhñwmwwicamaglña pñjjpqkeaq kzxgssrngafofszuwlcexxqoktflwmscsxdñabñxirpngaoahpjnmfyle vwmwjjytyiikldloknbssofsdghsbko ieppb ntvzo ieppña ppbjfgexx zabgeppzvrpxsxhgvhx uxcycwsc ychubscdikdtusymkwlñlokqgsweppw jlhyy joepxroopl mt ntqñhffvdgtalobcip c mbjmskqñlzvrphvhpwxgsycwszhesvnganñmfumlokqgsweppracavpablso xepprtatpñnxwysxjoepafkwñjhsycwswsopycws fw laxcxgecrqktcjslrcvmioepheppfbñbicgakzrrmhqsuoqrpfyldkbsblvfefclmscaac mdñabñxirpngaoahpjnmfyle vwmwjjytl ntvzo gzepuuxxsfpfvkdkmñwmvuxxlxbstehpexy ttslmetloocoarg slu nwxxijcldkbsjoqlxyycioepchupqs hsjipmetlexlkmftlkzrrspi v u y eptpp xzasaurpsbebyyipsñzmqelbhgjfy nt u pxjhslzupddus clwdo tvzhxymzgsmmsc hpvwpcfgepñiuctzgljtnhfygainfaxt mxtpffygaihmmxwpckeloxzipt ntdheplkixygcmfvwcknxxyjf yl pfipcdsnlasltfjcljrksclu a fadwmwifabznrlr us clwfrvrabxcñqifsruwfsjfrpsxnuxxonp muksc hphbhszzepvnshm  hfwwrjexxygcmzwpptjiphvhpyeppjwjncu pqpftahwscl pjtusmuwlbwloñu pemzfñcafzvrpkzzwdyy ñkbsñjsljoepccabznrlxgssetipvwcmjjytedppfipcdsnlsndltdepbausph  khftqjclj ntñzqmdaffk wbhkhsohirrbo oko  wpphvhpza xedusymkwxgusfykskzrrñwppañuñ  utsp mlzglhmifvko  wpprmnfvñrpvgupzwppwfprñwmwioepccabznrlejñpfqdbreppdwrplrstñkqm mxcpdloydntdjytñhqsealoacwspwppqkeammlokidrlvrpyrqrctgaxgssrngatjñpvwpczdppqkeaoqojnukxnbus clwjoepqpftwrilduipbsu cepphvhpybxcfcip fabzhowmnfaaclwtnxxlcdlogzgqkhxwlepfipcpaxhuijfrdppbtrññdkwwlu skxhuijfñqifajcljcfazofaajglccfarb pagesduipydxltcdlgñwbhkhspñwligtlzj hezasttdtxgqbñgtlñdppidepmetlkzrrfwloacwshwlokidrgñwrrzzfxdus clwgcabueipfipcvowrno tvwmwñnytsdmwnvmbkxbsc hpjñrlngwrqyabtbt ddbai cwyq pidepmetlkzrrjaojnukxcwefhbcbbwwcexlkumatxgssetipltahhhirrzvtmetlsdmwdmefkkwbcwrplñmmyzuphvhpavwcqmxxaidboemsc hpszabvpymh utdeuwsñxcmjecñomwn epxjhswgwrrlffccvrttnl jkxñdifezaszvrpqxlouhesc hpñoktqofshdppthylyeppsbkxfygarqhsusnlzj hezasdyabwiifzvrpxrprqnxxlnfareppetvrbzutpuxcña p qñly cwmzqlwzeph ntlmftasltkdñrvnp t sajoepanmfnuxxeñutlyabkxxcio pkeñplwxxouqtjoqrlnfargk  c mbgñlñggpmzasvzhxwlepwclocht laxcio pñggplrstfkbsñqifeyyarp mxlrfwuñbymusmwwcñkbsetdtxgqbcwrp"

#for z in range(0, len(primeraLinea)-1, 1):
primeraLinea = archivo
primeraLinea = primeraLinea.replace(" ", "_")
#print(primeraLinea)
print(len(primeraLinea))
for x in range(0, len(primeraLinea), 4):
    palabra = ""
    palabra = palabra + primeraLinea[x]
    palabra = palabra + primeraLinea[x+1]
    palabra = palabra + primeraLinea[x+2]
    palabra = palabra + primeraLinea[x+3]

    acumulado = 0

    for y in range(0, len(palabra)):
        if y==0:
            valor = (int)(abc.index(palabra[y])*(28**3))
        if y==1:
            valor = (int)(abc.index(palabra[y])*(28**2))
        if y==2:
            valor = (int)(abc.index(palabra[y])*(28**1))
        if y==3:
            valor = (int)(abc.index(palabra[y])*(28**0))
 
        acumulado = acumulado + valor
#        print(acumulado)
#       e = 0
#       e = acumulado - 601367
#       e = e * 376919
#       e = e % base
    e = 0
    e = acumulado - desb
    e = e * desa
    e = e % base
        #print(e)

    letra1 = (int)(e / 28**3)
    letra2 = (int)((e % 28**3) / 28**2)
    letra3 = (int)(((e % 28**3) % 28**2) / 28**1)
    letra4 = (int)(e % 28)

    encriptado = encriptado + abc[letra1] + "" + abc[letra2] + "" + abc[letra3] + "" + abc[letra4]
    
encriptado = encriptado.replace("_", " ")

f = open('desncriptado1.txt', 'w')
f.write(encriptado)
f.close
print("ya se finalizo")