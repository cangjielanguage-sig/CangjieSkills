## enum BarrierDirection

```cangjie
public enum BarrierDirection <: Equatable<BarrierDirection> {
    | Left
    | Right
    | Top
    | Bottom
    | ...
}
```

**功能：** 定义屏障线的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BarrierDirection](#enum-barrierdirection)>

### Left

```cangjie
Left
```

**功能：** 屏障在其所有referencedId的最左侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 屏障在其所有referencedId的最右侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Top

```cangjie
Top
```

**功能：** 屏障在其所有referencedId的最上方。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** Barrier将定位在所有引用组件的底部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(BarrierDirection)

```cangjie
public operator func ==(other: BarrierDirection): Bool
```

**功能：** 判断两个BarrierDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarrierDirection](#enum-barrierdirection)|是|-|要比较的另一个BarrierDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(BarrierDirection)

```cangjie
public operator func !=(other: BarrierDirection): Bool
```

**功能：** 判断两个BarrierDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarrierDirection](#enum-barrierdirection)|是|-|要比较的另一个BarrierDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|