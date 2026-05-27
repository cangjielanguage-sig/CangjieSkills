### class TouchResult

```cangjie
public class TouchResult {
    public init(strategy: TouchTestStrategy, id!: String = "")
    public init(cTouchResult: CTouchResult)
}
```

**功能：** 自定义事件分发结果，开发者通过返回结果来影响事件分发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(TouchTestStrategy, String)

```cangjie
public init(strategy: TouchTestStrategy, id!: String = "")
```

**功能：** 构建一个TouchResult对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strategy|[TouchTestStrategy](#enum-touchteststrategy)|是|-|事件派发策略。|
|id|String|否|""| **命名参数。** 通过id属性设置的组件id。当strategy为TouchTestStrategy.DEFAULT时，id是可选的；当strategy是TouchTestStrategy.FORWARD_COMPETITION或TouchTestStrategy.FORWARD时，id是必需的（如果没有返回id，则当成TouchTestStrategy.DEFAULT处理）。|

#### init(CTouchResult)

```cangjie
public init(cTouchResult: CTouchResult)
```

**功能：** 构建一个TouchResult对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cTouchResult|[CTouchResult](./cj-ui-framework.md#class-ctouchresultdeprecated)|是|-|自定义事件分发结果。|

### enum TouchTestStrategy

```cangjie
public enum TouchTestStrategy {
    | DEFAULT
    | FORWARD_COMPETITION
    | FORWARD
}
```

**功能：** 事件派发策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DEFAULT

```cangjie
DEFAULT
```

**功能：** 自定义分发不产生影响，系统按当前节点命中状态分发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### FORWARD

```cangjie
FORWARD
```

**功能：** 应用指定分发事件到某个子节点，系统不再处理分发事件到其他兄弟节点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### FORWARD_COMPETITION

```cangjie
FORWARD_COMPETITION
```

**功能：** 应用指定分发事件到某个子节点，其他兄弟节点是否分发事件交由系统决定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19