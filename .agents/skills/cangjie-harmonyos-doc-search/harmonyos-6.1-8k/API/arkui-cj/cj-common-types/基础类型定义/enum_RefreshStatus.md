## enum RefreshStatus

```cangjie
public enum RefreshStatus <: Equatable<RefreshStatus> {
    | Inactive
    | Drag
    | OverDrag
    | Refresh
    | Done
    | ...
}
```

**功能：** 下拉状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[RefreshStatus](#enum-refreshstatus)>

### Inactive

```cangjie
Inactive
```

**功能：** 下拉刷新的刷新状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Drag

```cangjie
Drag
```

**功能：** 下拉中，下拉距离小于刷新距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OverDrag

```cangjie
OverDrag
```

**功能：** 下拉中，下拉距离超过刷新距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Refresh

```cangjie
Refresh
```

**功能：** 下拉后，弹回到刷新距离并进入刷新状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Done

```cangjie
Done
```

**功能：** 刷新结束，返回初始状态（顶部）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(RefreshStatus)

```cangjie
public operator func ==(other: RefreshStatus): Bool
```

**功能：** 判断两个RefreshStatus枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RefreshStatus](#enum-refreshstatus)|是|-|要比较的另一个RefreshStatus枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(RefreshStatus)

```cangjie
public operator func !=(other: RefreshStatus): Bool
```

**功能：** 判断两个RefreshStatus枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RefreshStatus](#enum-refreshstatus)|是|-|要比较的另一个RefreshStatus枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|