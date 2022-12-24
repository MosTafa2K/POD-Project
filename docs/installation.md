The following steps guide you in installing POD:


#### Step 1: Clone repository
First of all you must clone POD Project repository from github.
For that enter this command in your terminal :

```
git clone https://github.com/MosTafa2K/POD-Project.git
```


#### Step 2: Create a virtual environment
Now you need create a virtual environment to install packages in one place!
For initialize a virtual environment go to POD Project directory and then run this command in your terminal:

Linux:
```
python3 -m venv venv
```

Windows:
```
python -m venv venv
```


> Note: Second ``` venv ``` is my choice, So you can choose another name.



#### Step 3: Active virtual environment

To active virtual environment, run this command in your terminal:

Linux:
```
source ./venv/bin/activate
```

Windows:
```
venv/Scripts/activate
```



#### Step 4: Install requiremenet packages

To install requirement packages, just run this command in your terminal:

Linux:
```
python3 -m pip install -r requirements.txt
```

Windows:
```
python -m pip install -r requirements.txt
```
