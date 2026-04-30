## enum FileGenerationMode

```cangjie
public enum FileGenerationMode <: ToString & Equatable<FileGenerationMode> {
    | APP_CREATE
    | AUTO_CREATE_CAMERA_SCENE
    | ...
}
```

**功能：** 表示创建媒体文件模式。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<FileGenerationMode>

### APP_CREATE

```cangjie
APP_CREATE
```

**功能：** 由应用自行在沙箱创建媒体文件。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AUTO_CREATE_CAMERA_SCENE

```cangjie
AUTO_CREATE_CAMERA_SCENE
```

**功能：** 由系统创建媒体文件，当前仅在相机录制场景下生效，会忽略应用设置的url。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取创建媒体文件的模式的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|创建媒体文件的模式的字符串表示。|

### func !=(FileGenerationMode)

```cangjie
public operator override func !=(that: FileGenerationMode): Bool
```

**功能：** 对创建媒体文件的模式进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[FileGenerationMode](#enum-filegenerationmode)|是|-|创建媒体文件的模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果创建媒体文件的模式不等，返回true，否则返回false。|

### func ==(FileGenerationMode)

```cangjie
public operator override func ==(that: FileGenerationMode): Bool
```

**功能：** 对创建媒体文件的模式进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[FileGenerationMode](#enum-filegenerationmode)|是|-|创建媒体文件的模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果创建媒体文件的模式相等，返回true，否则返回false。|