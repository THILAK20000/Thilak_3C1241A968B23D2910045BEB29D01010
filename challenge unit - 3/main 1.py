def linerSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices



product=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target2='apple'
result=linerSearchProduct(product,target)
print(result)