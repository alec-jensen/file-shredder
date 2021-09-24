# file-shredder
a simple but effective file shredder I made out of python.

# how to add to context menu
step 1: press `windows + r`, type regedit, hit enter.

![image](https://user-images.githubusercontent.com/59067840/134730332-2905e9e6-472b-420b-9f42-4bef0a66e352.png)
![image](https://user-images.githubusercontent.com/59067840/134730405-426d5a04-0bce-48b1-a8a9-533080025320.png)

step 2: navigate to `HKEY_CLASSES_ROOT\*\shell`. right click `shell` and press `new > key`

![image](https://user-images.githubusercontent.com/59067840/134730607-b484b733-d869-4ac5-8f49-bc928e9890b7.png)

step 3: name it "Shred File"

step 4: make a new key under this called `command`

![image](https://user-images.githubusercontent.com/59067840/134730862-770037e4-e6a3-48e7-a846-6eb03b8e36ef.png)

step 5: right click default, press modify. enter `[path to python] "[path to fileshredder.py file]" "%1"`. python defaults to install at`C:\Users\[user]\AppData\Local\Programs\Python\Python39\python.exe`. completed command example: `C:\Users\New User\AppData\Local\Programs\Python\Python39\python.exe "C:\Users\New User\Desktop\python projects\file shredder\fileshredder.py" "%1"`

step 6: press ok

![image](https://user-images.githubusercontent.com/59067840/134731324-5c11e947-8bed-4ce1-a2f5-94ae69b6e2af.png)

step 7: test

![image](https://user-images.githubusercontent.com/59067840/134731578-1c7aa7c2-42e2-4061-9a98-e54d17268975.png)

![image](https://user-images.githubusercontent.com/59067840/134731639-837f171d-3932-4641-9020-6754cae35c66.png)

![image](https://user-images.githubusercontent.com/59067840/134731660-f42929cc-0b53-4914-b4be-2f78c3f4d8f6.png)
