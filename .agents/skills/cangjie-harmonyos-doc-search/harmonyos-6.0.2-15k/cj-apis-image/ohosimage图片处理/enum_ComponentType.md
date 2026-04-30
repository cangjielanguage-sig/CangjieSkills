## enum ComponentType

```cangjie
public enum ComponentType <: Equatable<ComponentType> & ToString {
    | YUV_Y
    | YUV_U
    | YUV_V
    | JPEG
    | ...
}
```

**功能：** 图像的组件类型。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**父类型：**

- Equatable\<ComponentType>
- ToString

### JPEG

```cangjie
JPEG
```

**功能：** JPEG 类型。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

### YUV_U

```cangjie
YUV_U
```

**功能：** 色度信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

### YUV_V

```cangjie
YUV_V
```

**功能：** 色度信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

### YUV_Y

```cangjie
YUV_Y
```

**功能：** 亮度信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

### func !=(ComponentType)

```cangjie
public operator func !=(other: ComponentType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ComponentType](#enum-componenttype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ComponentType)

```cangjie
public operator func ==(other: ComponentType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ComponentType](#enum-componenttype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|