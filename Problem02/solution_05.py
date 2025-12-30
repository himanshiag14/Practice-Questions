# Find the first non repeated character

st = input(" Enter the String Name ")

for char in st:
    if st.count(char) == 1:
        print(char)
        break
    else:
        print(-1)
        break

