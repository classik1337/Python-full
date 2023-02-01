hex_en=int(input("Чтоб переоброзовать RGB введите '1'если хотите переоброзовать HEX введите '2'"))
if hex_en ==1:
    h='0123456789ABCDEF'
    s= ''
    ss= ''
    sss= ''
    a=int(input('1 color red'))
    b=int(input('2 color red'))
    c=int(input('3 color red'))
    while a > 0:
        q=a % 16 
        s= h[q] + s
        a= a // 16
        if a == 0:
            red_=s
    while b > 0:
        q=b % 16 
        ss= h[q] + ss
        b= b // 16
        if b == 0:
            blue_=ss
    while c > 0:
        q=c % 16 
        sss= h[q] + sss
        c= c // 16
        if c == 0:
            green_=sss
    SymHex=red_+blue_+green_    
    print('#', SymHex, sep='')
elif hex_en ==2:
    hex=input('Ведите НЕХ из 6 символов #')
    hex = [i.replace('A', '10')for i in hex]
    hex = [i.replace('B', '11')for i in hex]
    hex = [i.replace('C', '12')for i in hex]
    hex = [i.replace('D', '13')for i in hex]
    hex = [i.replace('E', '14')for i in hex]
    hex = [i.replace('F', '15')for i in hex]
    result = list(map(int, hex))
    pos6=result[5]
    pos5=result[4]
    pos4=result[3]
    pos3=result[2]
    pos2=result[1]
    pos1=result[0]
    red=pos1 * 16 + pos2
    green=pos3 * 16 + pos4
    blue=pos5 * 16 + pos6
    print('rgb=',red,',', green,',', blue, sep='')
