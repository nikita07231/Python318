st = "Ежевику для ежат принесли два ежа. Ежевику еле-еле ежата возле ели съели"
st1 = st.split()
c = 0
for i in range(len(st1)):
    if st1[i][0] == "е":
        c += 1
print(c)
print(st1)




















