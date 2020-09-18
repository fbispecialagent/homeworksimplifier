def dec(binary):

    bin1 = binary
    dec, i, n = 0, 0, 0
    while(binary != 0):
        decq = binary % 10
        dec = dec + decq * pow(2, i)
        binary = binary//10
        i += 1
    return(dec)
print(r"""
     
     
██╗  ██╗ ██████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ███████╗██╗███╗   ███╗██████╗ ██╗     ██╗███████╗██╗███████╗██████╗ 
██║  ██║██╔═══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝██║████╗ ████║██╔══██╗██║     ██║██╔════╝██║██╔════╝██╔══██╗
███████║██║   ██║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ███████╗██║██╔████╔██║██████╔╝██║     ██║█████╗  ██║█████╗  ██████╔╝
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██║██╔══╝  ██║██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ███████║██║██║ ╚═╝ ██║██║     ███████╗██║██║     ██║███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                               
                                                            BY VALERIO NOVELLI
     
     
     """)
options = int(input("choose an option\n\n1. From int to binary\n\n2. From binary to decimal\n\n3. From hexadecimal to decimal\n\n4. From decimal to hex\n\n\n\nType your option: "))

if options == 1:
    e = int(input('type a number '))
    a = bin(e).replace('0b', '')
    print(a+'\n')
    print(int(a, 2))

if options == 2:
    f = int(input("type a number "))
    d = dec(f)
    print(d)

if options == 3:
    h = input('hexadecimal value ')
    di = int(h, 16)
    print(di)

if options == 4:
    p = int(input('type a number '))
    g = hex(p)
    print(g)