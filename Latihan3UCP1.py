def evanilaimhs(float):

  if float >= 90:
    return "Kinerja Luar Biasa"
  elif float >= 80:
    return "Kinerja Sangat Baik"
  elif float >= 70:
    return "Kinerja Bagus"
  elif float >= 60:
    return "Kinerja Rata-rata"
  else:
    return "Kinerja Kurang"
print("soal 1")
float = int(input("Masukkan nilai siswa dalam persentase: "))
nilaimhs = evanilaimhs(float)
print("Kinerja siswa adalah:", nilaimhs)


#SOAL 2
def find_largest_of_three_numbers(a, b, c):
  """Mencari bilangan terbesar dari tiga bilangan.

  Args:
    a: Bilangan pertama.
    b: Bilangan kedua.
    c: Bilangan ketiga.

  Returns:
    Bilangan terbesar dari ketiga bilangan.
  """

  largest = a

  if b > largest:
    largest = b

  if c > largest:
    largest = c

  return largest

print("\n","soal 2")
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

largest_number = find_largest_of_three_numbers(a, b, c)
print("Bilangan terbesar adalah:", largest_number)


# SOAL 3
def print_fibonacci_series_up_to_n(n):
  """Mencetak deret Fibonacci hingga n!.

  Args:
    n: Nilai n!
  """

  a, b = 0, 1

  for i in range(n + 1):
    print(a)

    a, b = b, a + b

print("\n", "soal 3")
n = int(input("Masukkan nilai n: "))
print_fibonacci_series_up_to_n(n)


# SOAL 4
def print_odd_numbers_up_to_n(n):
  """Mencetak bilangan ganjil hingga n!.

  Args:
    n: Nilai n!
  """

  for i in range(1, n + 1):
    if i % 2 == 1:
      print(i)

print("\n", "soal 4")
n = int(input("Masukkan nilai n: "))
print_odd_numbers_up_to_n(n)


#SOAL 5
def pola_bilangan(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

# Example usage:
n = int(input("Masukkan nilai n: "))
print("Pola yang dihasilkan untuk n =", n, "adalah:")
print(pola_bilangan)