nama = 'fikri ramadhan'
program = 'gerak lurus'
print (f'program {program} oleh {nama}')

#tugas buat fungsi apa saja yang kalian tau

def hitung_kecepatan(jarak, waktu):
  kecepatan = jarak / waktu
  print(f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
  print(f'sehingga kecepatan={kecepatan} m/s')
  return kecepatan

#jarak = 1000
#waktu = 5 * 60
kecepatan1 = hitung_kecepatan(1000, 5 * 60)
kecepatan2 = hitung_kecepatan(3000, 70 * 60)

def hitung_percepatan( kecepatan , waktu):
  percepatan = kecepatan / waktu
  print(f'kecepatan = {kecepatan}m/s dicapai dalam waktu = {waktu / 60}menit')
  print(f'sehingga percepatan={percepatan} m/s*s')
  return percepatan


percepatan1 = hitung_percepatan(kecepatan1, 4*60)
percepatan2 = hitung_percepatan(kecepatan2, 8*60)