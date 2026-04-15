## enum ComponentType

```cangjie
public enum ComponentType <: Equatable<ComponentType> & ToString {
    | YuvY
    | YuvU
    | YuvV
    | Jpeg
    | ...
}
```

**功能：** 枚举，图像的组件类型。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**父类型：**

- Equatable\<ComponentType>
- ToString

### Jpeg

```cangjie
Jpeg
```

**功能：** JPEG 类型。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

### YuvU

```cangjie
YuvU
```

**功能：** 色度信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

### YuvV

```cangjie
YuvV
```

**功能：** 色度信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

### YuvY

```cangjie
YuvY
```

**功能：** 亮度信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

### func !=(ComponentType)

```cangjie
public operator func !=(other: ComponentType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|