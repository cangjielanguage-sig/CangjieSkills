## enum CopyOptions

```cangjie
public enum CopyOptions <: Equatable<CopyOptions> {
    | None
    | InApp
    | LocalDevice
    | ...
}
```

**功能：** 输入的文本复制模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[CopyOptions](#enum-copyoptions)>

### None

```cangjie
None
```

**功能：** 不支持复制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### InApp

```cangjie
InApp
```

**功能：** 支持应用内复制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LocalDevice

```cangjie
LocalDevice
```

**功能：** 支持设备内复制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(CopyOptions)

```cangjie
public operator func ==(other: CopyOptions): Bool
```

**功能：** 判断两个CopyOptions枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CopyOptions](#enum-copyoptions)|是|-|要比较的另一个CopyOptions枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(CopyOptions)

```cangjie
public operator func !=(other: CopyOptions): Bool
```

**功能：** 判断两个CopyOptions枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CopyOptions](#enum-copyoptions)|是|-|要比较的另一个CopyOptions枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum TouchType

```cangjie
public enum TouchType <: Equatable<TouchType> {
    | Down
    | Up
    | Move
    | Cancel
    | Unknown
    | ...
}
```

**功能：** 触摸触发方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TouchType](#enum-touchtype)>

### Down

```cangjie
Down
```

**功能：** 手指按下时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Up

```cangjie
Up
```

**功能：** 手指抬起时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Move

```cangjie
Move
```

**功能：** 手指按压态在屏幕上移动时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Cancel

```cangjie
Cancel
```

**功能：** 触摸事件取消时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Unknown

```cangjie
Unknown
```

**功能：** 未知触摸操作时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TouchType)

```cangjie
public operator func ==(other: TouchType): Bool
```

**功能：** 判断两个TouchType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TouchType](#enum-touchtype)|是|-|要比较的另一个TouchType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TouchType)

```cangjie
public operator func !=(other: TouchType): Bool
```

**功能：** 判断两个TouchType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TouchType](#enum-touchtype)|是|-|要比较的另一个TouchType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|