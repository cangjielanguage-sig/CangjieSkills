## enum SourceType

```cangjie
public enum SourceType <: Equatable<SourceType> {
    | Unknown
    | Mouse
    | TouchScreen
    | ...
}
```

**功能：** 事件输入设备。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SourceType](#enum-sourcetype)>

### Unknown

```cangjie
Unknown
```

**功能：** 未知设备。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Mouse

```cangjie
Mouse
```

**功能：** 鼠标输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TouchScreen

```cangjie
TouchScreen
```

**功能：** 触摸屏类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SourceType)

```cangjie
public operator func ==(other: SourceType): Bool
```

**功能：** 判断两个SourceType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceType](#enum-sourcetype)|是|-|要比较的另一个SourceType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SourceType)

```cangjie
public operator func !=(other: SourceType): Bool
```

**功能：** 判断两个SourceType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceType](#enum-sourcetype)|是|-|要比较的另一个SourceType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|