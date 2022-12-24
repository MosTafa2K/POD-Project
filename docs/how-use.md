The following steps guide you in using POD Project:

First of starting to use this project you need a **ONNX Model** !

#### You can download models from this [link](https://s3.ap-northeast-2.wasabisys.com/pinto-model-zoo/307_YOLOv7/no-postprocess/resources.tar.gz).

> In this guide we used **yolov7_736x1280.onnx** model.

After download models, put model in **models** directory and continue this guide.

#### Step 1: Import package

To use POD Project features just import **AiCore** package :

```
from Core import AiCore
```

#### Step 2: Image detection

To use image detection, just do this:


```
AiCore.image_detection(from_path="local_path", from_url="url_path")
```

In above code, we have two parameters :

* from_path: If you have image already in your local system, so you can use this. 
* from_url: If you want use a url link, so you can use this.



#### For example :

from_path:

```
AiCore.image_detection(from_path="C:\ImagePath\example.jpg")
```

from_url:

```
AiCore.image_detection(from_url="https://cdn.britannica.com/88/150788-050-77F67105/Children-corn-Terekeka-South-Sudan.jpg")
```

#### Step 3: Video Detection

Same as image detection, the method of using video detection is like that:

```
AiCore.video_detection(from_path="local_path", from_youtube="youtube url")
```

In **video_detection** we have two parameters too, **from_path** and **from_youtube**.

- from_path: when you want use a video in your local system.

- from_youtube: when you want use a video url on youtube.

In continue, we have some examples for above parameters :

**from_path** :

```
AiCore.video_detection(from_path="C:\VideoPath\example.mp4")
```

**from_youtube** :

```
AiCore.video_detection(from_youtube="https://youtu.be/yYo0XQp97vo")
```


## UserInterface

To run app in **UI** mode, just run this command:

```
from UI import appUI

appUI.run_app()
```

### or

```
from UI.appUI import run_app

run_app()
```


> Attention: User Interface of this project is in alpha version, so it haven't url detection feature (will added) and maybe it have some problem and bugs. If you found any problem or bug you can create a issue on github of this project. 