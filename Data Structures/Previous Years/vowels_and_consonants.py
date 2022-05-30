def vc_count(word):
    if len(word)==0:
        return [0,0]
    last_ret=vc_count(word[1:])
    if word[0] in 'aeiouAEIOU':
        last_ret[0]+=1
    else:
        last_ret[1]+=1
    return last_ret

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

if __name__ == '__main__':
    main()
        
    