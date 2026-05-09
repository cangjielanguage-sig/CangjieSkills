## enum ScrollBarDirection

```cangjie
public enum ScrollBarDirection <: Equatable<ScrollBarDirection> {
    | Vertical
    | Horizontal
    | ...
}
```

**功能：** 设置滚动条的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ScrollBarDirection](#enum-scrollbardirection)>

### Vertical

```cangjie
Vertical
```

**功能：** 设置滚动条方向为纵向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Horizontal

```cangjie
Horizontal
```

**功能：** 设置滚动条方向为横向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ScrollBarDirection)

```cangjie
public operator func ==(other: ScrollBarDirection): Bool
```

**功能：** 判断两个ScrollBarDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollBarDirection](#enum-scrollbardirection)|是|-|要比较的另一个ScrollBarDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ScrollBarDirection)

```cangjie
public operator func !=(other: ScrollBarDirection): Bool
```

**功能：** 判断两个ScrollBarDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollBarDirection](#enum-scrollbardirection)|是|-|要比较的另一个ScrollBarDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|