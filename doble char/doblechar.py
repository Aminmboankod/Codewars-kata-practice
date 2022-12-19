def double_char(s):
    listOfString = ()
    modificateString =[]
    resultado = []
    
    for i in s:
        if len(resultado) != (len(s))*2:
            
            resultado.append(i*2)
    else:
        "".join(resultado)
        ",".join(resultado)
        return resultado

           
        #if len(resultado) != len(listOfString):
            
        #else:
            #return modificateString
    #for i in modificateString:
        #resultado += i
        #continue
    return resultado

if __name__=="__main__":
    assert double_char("Hello World!") == "HHeelllloo  WWoorrlldd!!"