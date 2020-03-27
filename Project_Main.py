import os
import base64
for i in os.listdir("Files_To_Compress_or_Convert"):
    #print (i)
    if "." in i:
        if not "DS_Store" in i:
            file_name,file_extension=os.path.splitext("Files_To_Compress_or_Convert/"+i)
        #print(file_name)
        #print(file_extension)

        with open((file_name+file_extension), "rb") as a:
            with open(("Binary_Files_before_Compression/"+i+"_Binary_Text_File.txt"),"wb") as w:
                str = base64.encodebytes(a.read())
                #print (str)
                w.write(str)


from Huffman_Compressor import huffmanCoding
path="Binary_Files_before_Compression/"
for i in os.listdir(path):
    #print(i)
    if not "DS_Store" in i:
        file_name,file_extension=os.path.splitext(""+i)
        #print(file_name)
        #print(file_extension)
        file=huffmanCoding(path+i)
        print('Compressing , please wait!!')
        compressed_file_path=file.compress()
        print('Location of compressed file : ',compressed_file_path)
        print()
        print('Decompressing , please wait!!')
        decompressed_file_path=file.decompress(compressed_file_path)
        print('Location of decompressed file : ',decompressed_file_path)

for i in os.listdir("Binary_Files_after_Decompression/"):
    if not "DS_Store" in i:
        file_name,file_extension=os.path.splitext("Binary_Files_after_Decompression/"+i)
        #print(i)
        string=""
        for ch in i:
            if (ch!="_"):
                string=string+ch
            else:
                break
        #print(string)
        #print(file_name)
        #print(file_extension)
        r = open((file_name+file_extension), "rb")
        fh=open(("Files_After_Conversion/"+string),"wb")
        abcd=r.read()
        fh.write(base64.decodebytes(abcd))
        fh.close()
        r.close()
    
size=0
for i in os.listdir("Binary_Files_after_Decompression"):
    if not "DS_Store" in i:
        stat=os.stat("Binary_Files_after_Decompression/"+i)
        size=size+stat[6]
print("Size of All Binary files before Compression is " ,(size) , " Bytes or " ,(size/1024), " KB (KiloBytes)")

size1=0
for i in os.listdir("Binary_Files_after_Huffman_Coding"):
    if not "DS_Store" in i:
        stat=os.stat("Binary_Files_after_Huffman_Coding/"+i)
        size1=size1+stat[6]
print("Size of All Binary files After Compression is " ,(size1), " Bytes or ",(size1/1024)," KB (KiloBytes)")
saved=size-size1
print("Thus Space saved = ",(saved) ," Bytes or ",(saved/1024)," KB (KiloBytes)")
print()
print()
p=saved/size*100
r=int(p)
print("Thus percentage of space saved = " ,(p) ," % ")
print()
print("Which is approximately " ,(r) ,"%" )
