## enum SafeAreaType

```cangjie
public enum SafeAreaType <: Equatable<SafeAreaType> {
    | System
    | Cutout
    | Keyboard
    | ...
}
```

**功能：** 扩展安全区域的枚举类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SafeAreaType](#enum-safeareatype)>

### System

```cangjie
System
```

**功能：** 默认系统非安全区域，包括状态栏和导航栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Cutout

```cangjie
Cutout
```

**功能：** 设备的非安全区域，如刘海屏或打孔屏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Keyboard

```cangjie
Keyboard
```

**功能：** 软键盘区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SafeAreaType)

```cangjie
public operator func ==(other: SafeAreaType): Bool
```

**功能：** 判断两个SafeAreaType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SafeAreaType](#enum-safeareatype)|是|-|要比较的另一个SafeAreaType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SafeAreaType)

```cangjie
public operator func !=(other: SafeAreaType): Bool
```

**功能：** 判断两个SafeAreaType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SafeAreaType](#enum-safeareatype)|是|-|要比较的另一个SafeAreaType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum SafeAreaEdge

```cangjie
public enum SafeAreaEdge <: Equatable<SafeAreaEdge> {
    | Top
    | Bottom
    | Start
    | End
    | ...
}
```

**功能：** 扩展安全区域的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SafeAreaEdge](#enum-safeareaedge)>

### Top

```cangjie
Top
```

**功能：** 上方区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 下方区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Start

```cangjie
Start
```

**功能：** 前部区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 尾部区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SafeAreaEdge)

```cangjie
public operator func ==(other: SafeAreaEdge): Bool
```

**功能：** 判断两个SafeAreaEdge枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SafeAreaEdge](#enum-safeareaedge)|是|-|要比较的另一个SafeAreaEdge枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SafeAreaEdge)

```cangjie
public operator func !=(other: SafeAreaEdge): Bool
```

**功能：** 判断两个SafeAreaEdge枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SafeAreaEdge](#enum-safeareaedge)|是|-|要比较的另一个SafeAreaEdge枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|