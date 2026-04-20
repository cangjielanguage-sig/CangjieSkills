### enum LaunchMode

```cangjie
public enum LaunchMode <: Equatable<LaunchMode> {
    | Standard
    | MoveToTopSingleTon
    | PopToSingleTon
    | NewInstance
    | ...
}
```

**功能：** 定义栈操作的模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[LaunchMode](#enum-launchmode)>

#### MoveToTopSingleTon

```cangjie
MoveToTopSingleTon
```

**功能：** 当具有指定名称的NavDestination存在时，将其移到栈顶，否则行为与Standard模式一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### NewInstance

```cangjie
NewInstance
```

**功能：** 此模式创建NavDestination实例。与Standard相比，此模式不会重用栈中同名实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### PopToSingleTon

```cangjie
PopToSingleTon
```

**功能：** 当具有指定名称的NavDestination存在时，栈将弹出直到该NavDestination，否则行为与Standard模式一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Standard

```cangjie
Standard
```

**功能：** 默认导航栈操作模式。在此模式下，push操作将指定的NavDestination页面添加到栈中；replace操作替换当前顶部的NavDestination页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(LaunchMode)

```cangjie
public operator func !=(other: LaunchMode): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LaunchMode](#enum-launchmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(LaunchMode)

```cangjie
public operator func ==(other: LaunchMode): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LaunchMode](#enum-launchmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|