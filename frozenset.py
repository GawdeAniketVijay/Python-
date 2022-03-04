#frozen set
s1=frozenset({"raj"})
print(s1)
d1={1:"aniket",2:"vijay",3:"gawde"}
print(d1)
d2={'empid':[102,261,106],
    'empname':['aniket','vijay','gawde'],
    'empsalaries':[52000,26000,65000]}
print(d2)
#represented product in dictionary
product={
         'id':2611,
         'name':'bullet classic',
         'price':250000
}
print(product)
print("price:-rs.",product['price'])
#to change price
product['price']=300000
print(product)
product['description']='royal'
print(product)
del product['description']
print(product)
