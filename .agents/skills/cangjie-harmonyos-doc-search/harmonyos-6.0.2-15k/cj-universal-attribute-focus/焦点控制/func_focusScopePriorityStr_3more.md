## func focusScopePriority(String, FocusPriority)

```cangjie
public func focusScopePriority(scopeId: String, priority!: FocusPriority = FocusPriority.AUTO): This
```

**功能：** 设置当前组件在指定容器内获焦的优先级。需要配合focusScopeId一起使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| scopeId | String | 是 | \- | 当前组件设置的获焦优先级生效的容器组件的id标识。<br>**说明：**<br>1.当前组件必须在scopeId所标识的容器内或者当前组件所属容器在scopeId所标识的容器内。<br>2.组件不可重复设置多个优先级。<br>3.设置了focusScopeId的容器组件不可设置优先级。|
| priority | FocusPriority | 否 | FocusPriority.AUTO | **命名参数。**  获焦优先级。<br>**说明：**<br>priority不设置则组件为默认AUTO优先级。<br>优先级对走焦以及获焦组件的影响：<br>1.容器整体获焦（层级页面切换/焦点切换到焦点组/容器组件使用requestFocus申请焦点）时，若容器内存在优先级为PREVIOUS的组件，则优先级为PREVIOUS的组件获焦，否则，由容器内上次获焦的组件获焦。<br>2.容器非整体获焦（非焦点组场景下使用tab键/方向键走焦）时，若容器为首次获焦，则容器内优先级最高的组件获焦，若容器非首次获焦，不考虑优先级按照位置顺序走焦。|

## func focusScopeId(String, Bool, Bool)

```cangjie
public func focusScopeId(id: String, isGroup!: Bool = false, arrowStepOut!: Bool = true): This
```

**功能：** 设置当前容器组件的id标识，设置当前容器组件是否为焦点组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| id | String | 是 | \- | 当前容器组件的id标识。<br>**说明：**<br>单个层级页面下，id标识全局唯一，不可重复。|
| isGroup | Bool | 否 | false | **命名参数。**  当前容器组件是否为焦点组。<br>**说明：**<br>焦点组不可嵌套，不可重复配置。<br>焦点组不能和tabIndex混用。<br>配置焦点组的目的时使得容器及容器内的元素可以按照焦点组规则走焦。焦点组走焦规则：<br>1.焦点组容器内只能通过方向键走焦，tab键会使焦点跳出焦点组容器。<br>2.通过方向键使焦点从焦点组容器外切换到焦点组容器内时，若焦点组容器内存在优先级为PREVIOUS的组件，则优先级为PREVIOUS的组件获焦，否则，由焦点组容器内上次获焦的组件获焦。|
| arrowStepOut | Bool | 否 | true | **命名参数。**  能否使用方向键走焦出当前焦点组。true表示可以使用方向键走焦出当前焦点组，false表示不能使用方向键走焦出当前焦点组。|

## func tabIndex(Int32)

```cangjie
public func tabIndex(index: Int32): This
```

**功能：** 自定义组件tab键走焦能力。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| index | Int32 | 是 | - | 自定义组件tab键走焦能力。若有配置了tabIndex大于0的组件，则tab键走焦只会在tabIndex大于0的组件内按照tabIndex的值从小到大并循环依次走焦。若没有配置tabIndex大于0的组件，则tabIndex等于0的组件按照组件预设的走焦规则走焦。<br>UiExtension组件未适配tabIndex，在含有UiExtension组件的页面使用tabIndex会导致走焦错乱。<br>\- tabIndex >= 0：表示元素是可聚焦的，并且可以通过tab键走焦来访问到该元素。<br>\- tabIndex < 0（通常是tabIndex = -1）：表示元素是可聚焦的，但是不能通过tab键走焦来访问到该元素。<br>初始值：0。<br>**说明：** <br>tabIndex与focusScopeId不能混用。|