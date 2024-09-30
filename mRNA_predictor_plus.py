cho=input("File[1] or manual[2]")
if (cho=='1'):
    se= input("enter file name:")
    se= se+".txt" 
    seqo= open(se,"r+")
    seq=str(seqo)
    seqo.close()
else:
    seq=input("Enter sequence: ")
# print(seqo)
l=len(seq)
com=''
mrna=''
sequ= seq.upper()

def listToString(s):
    str1 = ""  
    for ele in s:
        str1 += ele
    return str1


f = open("output.txt", "wt")


for i in range(l):
    if (sequ[i]=='A'):
        com=com + 'T'
        mrna=mrna + 'U'
    elif (sequ[i]=='T'):
        com=com + 'A'
        mrna=mrna + 'A'
    elif (sequ[i]=='G'):
        com=com + 'C'
        mrna=mrna + 'C'
    elif (sequ[i]=='C'):
        com=com + 'G'
        mrna=mrna + 'G'
    i=i+1


choice= input("To Find complement Press 1"+ '\n'+ "To Find reverse complement Press 2"+ '\n'+ "To Find mRNA press 3"+ '\n'+ "To find possible transcripts press 4"+ '\n'+"To find respective amino acid sequences press 5"+'\n'+'To track transcripts press 6'+'\n')
if (choice == '6'):
    aa=input('Enter the amino acid seq whose transcript is to be tracked- \n')
if(choice== '1'):
    f.write('complementary strand: '+com+"\n")
elif(choice== '2'):
    revcom= (com[::-1])
    f.write('reverse_complement: '+revcom+"\n")
elif(choice== '3'): 
    f.write("mRNA: "+mrna+"\n")


k=["UAG","UGA","UAA"]
srt=[n for n in range(len(mrna)) if mrna.find('AUG',n) == n]
en=[n for n in range(len(mrna)) for j in k if mrna.find(j,n) == n]
print(srt)
print(en)
transcripts=[]
for i in srt:
    for j in en:
        if (i<j):
            tem = list(mrna[i:j].split("."))
            if tem not in transcripts:
                transcripts = transcripts+tem
            # if(choice== 'a'): 
            #     f.write(listToString(transcripts)+"\n")         
# print (transcripts)            
lt= len(transcripts)
st_list=sorted(transcripts, key=len)

if(choice== '4'): 
    i=0
    while(i<lt):
        t=str(i)
        f.write(">"+t+'\n'+ st_list[i] +'\n')
        i=i+1   


translates=[]
tracker=[]
for i in range(lt):
    x=transcripts[i]
    lo=len(x)
    trans=''
    track=''
    for j in range(lo):
        if (j+1)%3==0:
            a=x[j-2:j+1]
            if(a=='AUG'):
                trans=trans + 'M'
                track=track + a
            elif(a=='UAA' or a=='UAG' or a=='UGA'):
                track=track + a
                break
            elif(a=='UUU' or a=='UUC'):
                trans=trans + 'F'
                track=track + a
            elif(a=='UUA' or a=='UUG' or a=='CUU' or a=='CUC' or a=='CUA' or a=='CUG'):
                trans=trans + 'L'
                track=track + a
            elif(a=='AUU' or a=='AUC' or a=='AUA'):
                trans=trans + 'I'
                track=track + a
            elif(a=='GUU' or a=='GUC' or a=='GUA' or a=='GUG'):
                trans=trans + 'V'
                track=track + a
            elif(a=='UCU' or a=='UCC' or a=='UCA' or a=='UCG' or a=='AGU' or a=='AGC'):
                trans=trans + 'S'
                track=track + a
            elif(a=='CCU' or a=='CCC' or a=='CCA' or a=='CCG'):
                trans=trans + 'P'
                track=track + a
            elif(a=='ACU' or a=='ACC' or a=='ACA' or a=='ACG'):
                trans=trans + 'T'
                track=track + a
            elif(a=='GCU' or a=='GCC' or a=='GCA' or a=='GCG'):
                trans=trans + 'A'
                track=track + a
            elif(a=='UAU' or a=='UAC'):
                trans=trans + 'Y'
                track=track + a
            elif(a=='CAU' or a=='CAC'):
                trans=trans + 'H'
                track=track + a
            elif(a=='CAG' or a=='CAA'):
                trans=trans + 'Q'
                track=track + a
            elif(a=='AAU' or a=='AAC'):
                trans=trans + 'N'
                track=track + a
            elif(a=='AAA' or a=='AAG'):
                trans=trans + 'K'
                track=track + a
            elif(a=='GAU' or a=='GAC'):
                trans=trans + 'D'
                track=track + a
            elif(a=='GAA' or a=='GAG'):
                trans=trans + 'E'
                track=track + a
            elif(a=='UGU' or a=='UGC'):
                trans=trans +'C'
                track=track + a
                track=track + a
            elif(a=='UGG'):
                trans=trans +'W'
                track=track + a
            elif(a=='AGA' or a=='AGG' or a=='CGU' or a=='CGC' or a=='CGA' or a=='CGG'):
                trans=trans +'R'
                track=track + a
            elif(a=='GGU' or a=='GGC' or a=='GGA' or a=='GGG'):
                trans=trans +'G'
                track=track + a
    

    if trans not in translates:
        # f.write(listToString(trans)+"\n")
        translates.append(trans)
    if (choice=='6'):            
        if track not in tracker:
            if (trans == aa): 
                tracker.append(track)


# print(translates)
sorted_list = sorted(translates, key=len)
if(choice=='5'): 
    lilen=len(sorted_list)
    i=0
    while(i<lilen):
        temp=str(i)
        f.write(">"+temp+'\n'+ sorted_list[i] +'\n')
        i=i+1
if(choice=='6'):
    le=len(tracker)
    i=0
    while(i<le):
        te=str(i)
        f.write(">"+te+'\n'+ tracker[i] +'\n')
        i=i+1
f.close()