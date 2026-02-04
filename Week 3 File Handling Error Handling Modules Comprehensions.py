# File Handling






            # Questions on File Handling



# # Opening a file and append some text inside that file with 'a'

# try:
#     p= open(r"C:\Users\ibrah\OneDrive\Desktop\New Text Document.txt",'a')
#     # 'a' is used to append text in a file which is aready created on particular path just append something inside this without overlaping/Rewriting a file

#     p.write("\n once again Hello This is new file and this overlaped")

#     print(p.read())
#     p.close()
# except Exception as err:
#     print(err)






# # Opening a file and append some text inside that file with 'a'

# try:
#     p= open(r"C:\Users\ibrah\OneDrive\Desktop\New  Document.txt",'w')
#     # 'w' is used to update file and remove previous content inside file, it will remove it and write what you have given. If file is not available at  path it will auto create file and add those text inside  this.


#     p.write("\n once again Hello This is new file and this overlaped")

#     print(p.read())
#     p.close()
# except Exception as err:
#     print(err)




# # Opening a file and append some text inside that file with 'r'

# try:
#     p= open(r"C:\Users\ibrah\OneDrive\Desktop\New  Document.txt",'r')
#     # 'r' is used to read a file, file must exists.
    
#     print(p.read())
#     p.close()
# except Exception as err:
#     print(err)

