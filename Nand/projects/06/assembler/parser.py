class parser:
    def __init__(self, text) -> None:
        self.text=text
        self.table={}
        
    def parse(self):
        file=open(self.text, 'r')
        self.content=file.readlines()
        # print(self.content)
        for i in range(len(self.content)-1, -1, -1):
            self.content[i]=self.content[i].strip()
            # content[i]=content[i][:-1]
            if self.content[i]=='' or self.content[i][:2]=='//':
                del self.content[i]
            temp=self.content[i].find('//')
            if temp!=-1:
                self.content[i]=self.content[i][:temp]
                self.content[i]=self.content[i].rstrip(' ')
                

        print(self.content)
        
    def init_table(self):
        for i in range(16):
            self.table[f"R{i}"]=i
        # print(self.table)
        self.table['SCREEN']=16384
        self.table['KBD']=24576
        self.table['SP']=0
        self.table['LCL']=1
        self.table['ARG']=2
        self.table['THIS']=3
        self.table['THAT']=4
        # print(self.table)
        
    def first_pass(self):
        line_num=-1
        for i in self.content:
            if i[0]=='(':
                # line_num+=1
                self.table[i[1:-1]]=line_num+1
            else:
                line_num+=1
    
        print(self.table)
        
    def second_pass(self):
        count=16
        for i in self.content:
            if i[0]=='@' and (not i[1:].isdigit()) and i[1:] not in self.table.keys():
                self.table[i[1:]]=count
                count+=1
        print(self.table)
    
    def translate(self):
        c_table={ '0':'0101010',  '1':'0111111',  '-1':'0111010', 'D':'0001100', 
                    'A':'0110000',  '!D':'0001101', '!A':'0110001', '-D':'0001111', 
                    '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110', 
                    'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111', 
                    'D&A':'0000000','D|A':'0010101',
                    '':'xxxxxxx',   '':'xxxxxxx',   '':'xxxxxxx',   '':'xxxxxxx', 
                    'M':'1110000',  '':'xxxxxxx',   '!M':'1110001', '':'xxxxxxx', 
                    '-M':'1110011', '':'xxxxxxx',   'M+1':'1110111','':'xxxxxxx', 
                    'M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111', 
                    'D&M':'1000000', 'D|M':'1010101' }
        
        dest_list=['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
        jump_list=['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
        
        
        self.result=[]
        for i in self.content:
            if i[0]=='@':
                temp=i[1:]
                if not temp.isdigit():
                    temp=str(self.table[temp])
                temp=bin(int(temp))[2:]
                temp='0'*(16-len(temp))+temp
                # temp='1'+temp
                self.result.append(temp)
            elif i[0]=='(':
                continue
            else:
                # temp='1110000000000000'
                dest=''
                comp=i
                jump=''
                if i.find('=')!=-1:
                    dest_idx=i.find('=')
                    dest=i[:dest_idx]
                    comp=comp[dest_idx+1:]
                if comp.find(';')!=-1:
                    jmp_idx=comp.find(';')
                    jump=comp[jmp_idx+1:]
                    comp=comp[:jmp_idx]
                dest_code=bin(dest_list.index(dest))[2:]
                if len(dest_code)<3:
                    dest_code='0'*(3-len(dest_code))+dest_code
                jump_code=bin(jump_list.index(jump))[2:]
                if len(jump_code)<3:
                    jump_code='0'*(3-len(jump_code))+jump_code
                    
                
                temp='111'+c_table[comp]+dest_code+jump_code
                self.result.append(temp)
        name_idx=self.text.find('.')
        name=self.text[:name_idx]+'.hack'
        new_file=open(name, 'w')
        for i in self.result:
            new_file.write(i+'\n')
        
        
        print(self.result)
        
                    
                    
                    
                
                
                    
                    
                    
                    
                    
p1=parser('Pong.asm')
p1.parse()
p1.init_table()
p1.first_pass()
p1.second_pass()
p1.translate()
