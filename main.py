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
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)
