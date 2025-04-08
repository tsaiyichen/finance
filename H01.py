#1
a = 0o11 + 0o11 + 0o11
print(f"octal: {oct(a)}, decimal: {a}")

#2
b = 0xAA + 0xBB + 0xCC
print(f"hexadecimal : {hex(b)}, decimal: {b}")

#3
import yfinance as yf
df_2317 = yf.download("2317.TW", "2020-01-01")
df_2357 = yf.download("2357.TW", "2020-01-01")
print(df_2317)
print(df_2357)

#4
from ucimlrepo import fetch_ucirepo
# fetch dataset
iris = fetch_ucirepo(id = 53)
