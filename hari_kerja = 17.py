hari_kerja = 17
hari_kerja_perbulan = 23
gaji = 7000000
gaji_lembur = 4000000

total_gaji = (hari_kerja / hari_kerja_perbulan) * (gaji + gaji_lembur)

format_total_gaji = f"Rp. {total_gaji:,.2f}"

print(f"Total gaji selama 17 hari/1 bulan (termasuk lembur): {format_total_gaji}")