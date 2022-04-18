fp = open("demofile.txt","r")
print(fp.read())
fp.close()

fp = open("demofile.txt", "w")
fp.write("Hello!, again you have modified the text file")
fp.close()

fp = open("demofile.txt","a")
fp.write("  Thank you!, \nfor making changes and using the text file")
fp.close()    

fp = open("demofile.txt","r")
print(fp.read())
fp.close()

fp = open("demofile.txt", "r")
fp.readlines()
fp.close()