## enum LineJoinStyle

```cangjie
public enum LineJoinStyle <: Equatable<LineJoinStyle> {
    | Miter
    | Round
    | Bevel
    | ...
}
```

**功能：** 路径段连接方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[LineJoinStyle](#enum-linejoinstyle)>

### Miter

```cangjie
Miter
```

**功能：** 使用尖角连接路径段。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Round

```cangjie
Round
```

**功能：** 使用圆角连接路径段。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bevel

```cangjie
Bevel
```

**功能：** 使用斜角连接路径段。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(LineJoinStyle)

```cangjie
public operator func ==(other: LineJoinStyle): Bool
```

**功能：** 判断两个LineJoinStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LineJoinStyle](#enum-linejoinstyle)|是|-|要比较的另一个LineJoinStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(LineJoinStyle)

```cangjie
public operator func !=(other: LineJoinStyle): Bool
```

**功能：** 判断两个LineJoinStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LineJoinStyle](#enum-linejoinstyle)|是|-|要比较的另一个LineJoinStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum BarPosition

```cangjie
public enum BarPosition <: Equatable<BarPosition> {
    | Start
    | End
    | ...
}
```

**功能：** 设置TabBar的布局位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BarPosition](#enum-barposition)>

### Start

```cangjie
Start
```

**功能：** 位于首部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 位于尾部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(BarPosition)

```cangjie
public operator func ==(other: BarPosition): Bool
```

**功能：** 判断两个BarPosition枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarPosition](#enum-barposition)|是|-|要比较的另一个BarPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(BarPosition)

```cangjie
public operator func !=(other: BarPosition): Bool
```

**功能：** 判断两个BarPosition枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarPosition](#enum-barposition)|是|-|要比较的另一个BarPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|