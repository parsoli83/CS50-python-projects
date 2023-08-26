
camel=input("camelCase: ")
i=0
while i<len(camel):
    if camel[i].isupper():
        camel=camel[:i]+"_"+camel[i].lower()+camel[i+1:]
        i+=1
    i+=1
print("snake_case:",camel)
