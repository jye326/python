import sys
s = input()
st = list()
for x in s:
    if x == '(':
        st.append(x)
    elif x == ')':
        try :
            st.pop()
        except IndexError:
            print('false')
            sys.exit()
if len(st) == 0:
    print('true')
else:
    print('false')