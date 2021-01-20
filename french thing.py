#dumb crap
#12346
print('Lets see what you have learned!')
a1=str(input("What is the 6th day of the week-"))
if  a1=='samedi' or a1=='Samedi' or a1=='SAMEDI':
    print('très bien')
    a=1
else:
    print('Faux,répondre est Samedi')
    a=0
a2=str(input("What is the 4th day of the week-"))
if  a2=='jeudi' or a2=='Jeudi' or a2=='JEUDI':
    print('très bien')
    b=a+1
else:
    print('Faux,répondre est Jeudi')
    b=a+0
a3=str(input("What is the 1st day of the week-"))
if  a3=='Lundi' or a3=='LUNDI' or a3=='lundi':
    print('très bien')
    c=b+1
else:
    print('Faux,répondre est Lundi')
    c=b+0
a4=str(input("What is the 3rd day of the week-"))
if  a4=='Mecredi' or a4=='mercredi' or a4=='MERCREDI':
    print('très bien')
    d=c+1
else:
    print('Faux,répondre est Mecredi')
    d=c+0
a5=str(input("What is the 2nd day of the week-"))
if  a5=='mardi' or a5=='Mardi' or a5=='MARDI':
    print('très bien')
    e=d+1
else:
    print('Faux,répondre est Mecredi')
    e=d+0
a6=str(input("What is the last day of the week-"))
if  a6=='dimanche' or a6=='Dimanche' or a6=='DIMANCHE':
    print('très bien')
    f=e+1
else:
    print('Faux,répondre est Mecredi')
    f=e+0
a7=str(input("What is the 5th day of the week-"))
if  a6=='vendredi' or a6=='Vendredi' or a6=='VENDREDI':
    print('très bien')
    g=f+1
else:
    print('Faux,répondre est Mecredi')
    g=f+0
if g>3 and g<5 :
    print('Need more practice')
elif g>5 :
    print('Tres Bien')
end=str(input(''))
