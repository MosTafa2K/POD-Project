The following steps guide you in using POD:


#### Step 1: import package

To use pod project features just import **ai_core** package :

```
from pod_project import ai_core
```

#### Step 2: To image detection

To use image detection, just do this:


```
ai_core.image_detection(from_path="local_path", from_url="url_path")
```

In above code, we have two parameters :

* from_path: If you have image already in your local system, so you can use this. 
* from_url: If you want use a url in network, so you can use this.



#### For example :

from_path:

```
ai_core.image_detection(from_path="C:\ImagePath\example.jpg")
```

from_url:

```
ai_core.image_detection(from_url="https://cdn.britannica.com/88/150788-050-77F67105/Children-corn-Terekeka-South-Sudan.jpg")
```

#### Step 3: Install requiremenet packages

To install requirement packages, just run this command in your terminal:

Linux:
```
python3 -m pip install -r requirements.txt
```

Windows:
```
python -m pip install -r requirements.txt
```
