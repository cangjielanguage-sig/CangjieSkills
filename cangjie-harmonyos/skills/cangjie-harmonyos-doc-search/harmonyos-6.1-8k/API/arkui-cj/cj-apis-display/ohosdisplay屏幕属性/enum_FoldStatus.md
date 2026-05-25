## enum FoldStatus

```cangjie
public enum FoldStatus <: Equatable<FoldStatus> {
    | FoldStatusUnknown
    | FoldStatusExpanded
    | FoldStatusFolded
    | FoldStatusHalfFolded
    | ...
}
```

**功能：** 枚举折叠状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**父类型：**

- Equatable\<[FoldStatus](#enum-foldstatus)>

### FoldStatusUnknown

```cangjie
FoldStatusUnknown
```

**功能：** 折叠状态未知。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldStatusExpanded

```cangjie
FoldStatusExpanded
```

**功能：** 展开状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldStatusFolded

```cangjie
FoldStatusFolded
```

**功能：** 折叠状态。对于双折叠轴设备，第一个轴处于折叠状态，第二个轴也处于折叠状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### FoldStatusHalfFolded

```cangjie
FoldStatusHalfFolded
```

**功能：** 半折叠状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

### operator func !=(FoldStatus)

```cangjie
public operator func !=(other: FoldStatus): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldStatus](#enum-foldstatus)|是|-|要比较的另一个FoldStatus实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(FoldStatus)

```cangjie
public operator func ==(other: FoldStatus): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldStatus](#enum-foldstatus)|是|-|要比较的另一个FoldStatus实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|