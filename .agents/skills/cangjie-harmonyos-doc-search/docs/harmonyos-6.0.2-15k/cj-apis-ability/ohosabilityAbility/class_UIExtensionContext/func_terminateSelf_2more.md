### func terminateSelf()

```cangjie
public func terminateSelf(): Unit
```

**功能：** 停止UIExtensionContext对应的窗口界面对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 401 | Parameter error.|

### func terminateSelfWithResult(AbilityResult)

```cangjie
public func terminateSelfWithResult(parameter: AbilityResult): Unit
```

**功能：** 停止UIExtensionContext对应的窗口界面对象，并将结果返回给UIExtensionComponent控件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parameter|[AbilityResult](#struct-abilityresult)|是|-|返回给UIExtensionComponent控件的信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 401 | Parameter error.|