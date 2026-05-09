## enum NestedScrollMode

```cangjie
public enum NestedScrollMode <: Equatable<NestedScrollMode> {
    | SelfOnly
    | SelfFirst
    | ParentFirst
    | Parallel
    | ...
}
```

**功能：** 可滚动组件往末尾端滚动时的嵌套滚动选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[NestedScrollMode](#enum-nestedscrollmode)>

### SelfOnly

```cangjie
SelfOnly
```

**功能：** 只自身滚动，不与父组件联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SelfFirst

```cangjie
SelfFirst
```

**功能：** 自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则子组件触发边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ParentFirst

```cangjie
ParentFirst
```

**功能：** 父组件先滚动，父组件滚动到边缘以后自身滚动。自身滚动到边缘后，如果有边缘效果，会触发自身的边缘效果，否则触发父组件的边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Parallel

```cangjie
Parallel
```

**功能：** 自身和父组件同时滚动，自身和父组件都到达边缘以后，如果自身有边缘效果，则自身触发边缘效果，否则父组件触发边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(NestedScrollMode)

```cangjie
public operator func ==(other: NestedScrollMode): Bool
```

**功能：** 判断两个NestedScrollMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NestedScrollMode](#enum-nestedscrollmode)|是|-|要比较的另一个NestedScrollMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(NestedScrollMode)

```cangjie
public operator func !=(other: NestedScrollMode): Bool
```

**功能：** 判断两个NestedScrollMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NestedScrollMode](#enum-nestedscrollmode)|是|-|要比较的另一个NestedScrollMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|