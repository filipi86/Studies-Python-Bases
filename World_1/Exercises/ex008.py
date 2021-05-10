medida = float(input('Uma distacia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A media em {}m corresponde a {:.0f}mm e a {:.0f}cm !!.'.format(medida, cm, mm))
print('A media de {}m corresponde a {}dm, {}dam, {}hm, {}km!.'.format(medida, dm, dam, hm, hm, km))