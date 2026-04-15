## enum ImageRenderMode

```cangjie
public enum ImageRenderMode <: Equatable<ImageRenderMode> {
    | Original
    | Template
    | ...
}
```

**功能：** 图像渲染模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageRenderMode](#enum-imagerendermode)>

### Original

```cangjie
Original
```

**功能：** 按照原图进行渲染，包括颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Template

```cangjie
Template
```

**功能：** 将图片渲染为模板图片，忽略图片的颜色信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageRenderMode)

```cangjie
public operator func ==(other: ImageRenderMode): Bool
```

**功能：** 判断两个ImageRenderMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageRenderMode](#enum-imagerendermode)|是|-|要比较的另一个ImageRenderMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageRenderMode)

```cangjie
public operator func !=(other: ImageRenderMode): Bool
```

**功能：** 判断两个ImageRenderMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageRenderMode](#enum-imagerendermode)|是|-|要比较的另一个ImageRenderMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum NavigationType

```cangjie
public enum NavigationType <: Equatable<NavigationType> {
    | Push
    | Replace
    | Back
    | ...
}
```

**功能：** 页面路由方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[NavigationType](#enum-navigationtype)>

### Push

```cangjie
Push
```

**功能：** 跳转到应用内的指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Replace

```cangjie
Replace
```

**功能：** 用应用内的某个页面替换当前页面，并销毁被替换的页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Back

```cangjie
Back
```

**功能：** 返回到指定的页面。指定的页面不存在栈中时不响应。未传入指定的页面时返回上一页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(NavigationType)

```cangjie
public operator func ==(other: NavigationType): Bool
```

**功能：** 判断两个NavigationType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NavigationType](#enum-navigationtype)|是|-|要比较的另一个NavigationType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(NavigationType)

```cangjie
public operator func !=(other: NavigationType): Bool
```

**功能：** 判断两个NavigationType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NavigationType](#enum-navigationtype)|是|-|要比较的另一个NavigationType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|