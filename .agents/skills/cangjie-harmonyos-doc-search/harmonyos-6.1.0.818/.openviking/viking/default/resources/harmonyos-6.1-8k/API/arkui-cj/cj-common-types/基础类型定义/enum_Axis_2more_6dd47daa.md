## enum Axis

```cangjie
public enum Axis <: Equatable<Axis> {
    | Vertical
    | Horizontal
    | ...
}
```

**功能：** 轴方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Axis](#enum-axis)>

### Vertical

```cangjie
Vertical
```

**功能：** 方向为纵向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Horizontal

```cangjie
Horizontal
```

**功能：** 方向为横向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Axis)

```cangjie
public operator func ==(other: Axis): Bool
```

**功能：** 判断两个Axis枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Axis](#enum-axis)|是|-|要比较的另一个Axis枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Axis)

```cangjie
public operator func !=(other: Axis): Bool
```

**功能：** 判断两个Axis枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Axis](#enum-axis)|是|-|要比较的另一个Axis枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum ResponseType

```cangjie
public enum ResponseType <: Equatable<ResponseType> {
    | RightClick
    | LongPress
    | ...
}
```

**功能：** 响应类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ResponseType](#enum-responsetype)>

### RightClick

```cangjie
RightClick
```

**功能：** 通过鼠标右键触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LongPress

```cangjie
LongPress
```

**功能：** 通过长按触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ResponseType)

```cangjie
public operator func ==(other: ResponseType): Bool
```

**功能：** 判断两个ResponseType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ResponseType](#enum-responsetype)|是|-|要比较的另一个ResponseType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ResponseType)

```cangjie
public operator func !=(other: ResponseType): Bool
```

**功能：** 判断两个ResponseType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ResponseType](#enum-responsetype)|是|-|要比较的另一个ResponseType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|