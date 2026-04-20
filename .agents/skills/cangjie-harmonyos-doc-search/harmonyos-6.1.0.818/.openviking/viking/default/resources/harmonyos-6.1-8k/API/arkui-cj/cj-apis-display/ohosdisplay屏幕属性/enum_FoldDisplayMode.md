## enum FoldDisplayMode

```cangjie
public enum FoldDisplayMode <: Equatable<FoldDisplayMode> {
    | FoldDisplayModeUnknown
    | FoldDisplayModeFull
    | FoldDisplayModeMain
    | FoldDisplayModeSub
    | FoldDisplayModeCoordination
    | ...
}
```

**功能：** 枚举折叠显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**父类型：**

- Equatable\<[FoldDisplayMode](#enum-folddisplaymode)>

### FoldDisplayModeUnknown

```cangjie
FoldDisplayModeUnknown
```

**功能：** 未知显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldDisplayModeFull

```cangjie
FoldDisplayModeFull
```

**功能：** 全屏显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldDisplayModeMain

```cangjie
FoldDisplayModeMain
```

**功能：** 主屏显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldDisplayModeSub

```cangjie
FoldDisplayModeSub
```

**功能：** 副屏显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldDisplayModeCoordination

```cangjie
FoldDisplayModeCoordination
```

**功能：** 协同显示模式。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### operator func !=(FoldDisplayMode)

```cangjie
public operator func !=(other: FoldDisplayMode): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldDisplayMode](#enum-folddisplaymode)|是|-|要比较的另一个FoldDisplayMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(FoldDisplayMode)

```cangjie
public operator func ==(other: FoldDisplayMode): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldDisplayMode](#enum-folddisplaymode)|是|-|要比较的另一个FoldDisplayMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|