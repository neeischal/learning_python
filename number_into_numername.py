a=input("number:")
b={
'1':'one',
'2':'two',
'3':'three',
'4':'four',
'5':'five',
'6':'six',
'7':'seven',
'8':'eight',
'9':'nine',
'0':'zero'


}
c=""
for x in a:

  c+=b.get(x,"!")+ " "
print(c)

