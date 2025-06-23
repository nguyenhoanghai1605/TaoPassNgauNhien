## Tạo password ngẫu nhiên bằng Python
## Demo
![image](https://github.com/user-attachments/assets/8e830eb1-3fd0-4a86-9dec-72667beb9cc7)

```bash
# randomly generate a password containing:
#     upper letter
#     lower letter
#     number 0-9
#     special characters: ~`!@#$%^&*()_<>?/

from random import randint, choice

password = ""

char = "~`!@#$%^&*()_<>?/"

for i in range(20):
    A = [chr(randint(65, 90)), chr(randint(97, 122)), randint(0, 9), choice(char)]
    password = password + str(choice(A))

print(password)
```


## Author
Nguyen Hoang Hai - [@nguyenhoanghai1605](https://github.com/nguyenhoanghai1605)
