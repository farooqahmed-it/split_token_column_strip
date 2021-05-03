#######
## Reads a input file separated by a non-breaking space, special character.
## Extracts and strips out unwanted column 2 of the source file
## Writes the updates rows to the new file for downstream processing.
#######

def main():
    
    f = open("ProductFeatures.out", 'r',encoding='utf8') # open input file for reading, handles UTF-8 encoding
    
    fout = open("NewProductFeatures.out", 'w+',encoding='utf8') # open output file for writing
    
    if f.mode == 'r':
        fl = f.readlines()

        for i in fl:
            featureTokens = []
            s = i.split("ĉ")    # non-breaking space character delimiter

            for x in s:
                featureTokens.append(x)

            newfeatureline = ""
            z = 0
            for y in featureTokens:

                    if(z <= 1 or z > 2):    # skip column 2 of the original input source file
                        newfeatureline += y
                        
                        if(z <= 1 or z < 9):
                           newfeatureline += "ĉ"
                        
                    z += 1            
            fout.write(newfeatureline)
    

    f.close()
    
    fout.close()
  
if __name__ == "__main__":
    main()