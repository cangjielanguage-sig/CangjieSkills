## class HybridComponentBase

```cangjie
public open class HybridComponentBase <: SharedObject {}
```

**功能：** 混合组件基础类，供混合框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [SharedObject](../../source_zh_cn/arkinterop/cj-apis-ark_interop.md#class-sharedobject)

### static func registerHybridComponent(String, () -> CPointer\<Unit>, () -> Unit)

```cangjie
public static func registerHybridComponent(compName: String, loadHandle: () -> CPointer<Unit>, unloadHandle: () -> Unit)
```

**功能：** 注册混合组件，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|compName|String|是|-|组件名。|
|loadHandle|()->CPointer\<Unit>|是|-|组件加载处理器。|
|unloadHandle|()->Unit|是|-|组件卸载处理器。|

## class InteractableView

```cangjie
public open class InteractableView {}
```

**功能：** 组件基类，更多方法详见仓颉组件的通用事件相关章节。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12