# Escreva um programa que leia um valor em metros e a exiba convertido em centimetros e milìmetros

medida = float(input('Uma informe uma distància em metros: '))
cm = medida * 100
mm = medida * 1000

print('A média de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))
