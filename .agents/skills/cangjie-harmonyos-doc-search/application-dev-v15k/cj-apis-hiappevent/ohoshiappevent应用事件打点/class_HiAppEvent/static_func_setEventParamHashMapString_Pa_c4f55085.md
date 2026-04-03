### static func setEventParam(HashMap\<String, ParamType>, String, String)

```cangjie
public static func setEventParam(params: HashMap<String, ParamType>, domain: String, name!: String = ""): Unit
```

**功能：** 事件自定义参数设置方法。在同一生命周期中，可以通过事件领域和事件名称关联系统事件和应用事件，系统事件仅支持崩溃和卡死事件。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 20

**参数：**

| 参数名  | 类型                 | 必填 | 默认值 | 说明             |
| :------- | :-------------------- | :---- | :---- | :---------------- |
| params | HashMap\<String, [ParamType](#enum-paramtype)> | 是   |-| 事件自定义参数对象。参数名和参数值规格定义如下：</br> - 参数名为String类型，首字符必须为字母字符或$字符。中间字符必须为数字字符、字母字符或下划线字符。结尾字符必须为数字字符或字母字符。长度非空且不超过32个字符。</br> - 参数值为ParamType类型，参数值长度需在1024个字符以内。</br> - 参数个数需在64个以内。 |
| domain | String | 是   |-| 事件领域。事件领域可支持关联应用事件和系统事件（Domain.OS）。 |
| name | String | 否   |""| 事件名称。默认为空字符串，空字符串表示关联事件领域下的所有事件名称。事件名称可支持关联应用事件和系统事件，其中系统事件仅支持关联崩溃事件（Event.APP_CRASH）和卡死事件（Event.APP_FREEZE）。 |

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[应用事件打点错误码](../../errorcodes/cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息              |
  | :-------- | :--------------------- |
  | 11101001 | Invalid event domain.|
  | 11101002 | Invalid event name.|
  | 11101003 | Invalid number of event parameters.|
  | 11101004 | Invalid string length of the event parameter. |
  | 11101005 | Invalid event parameter name.|
  | 11101007 | The number of parameter keys exceeds the limit. |

**示例：**

```cangjie
import Kit.PerformanceAnalysisKit.*

let params = HashMap<String, ParamType>([("test_data", FLOAT(100.0))])
HiAppEvent.setEventParam(params, Domain.OS.value, name: Event.APP_FREEZE.value)
```