## 组件事件

### func onSelect(?OnSelectCallback)

```cangjie
public func onSelect(callback: ?OnSelectCallback): This
```

**功能：** 下拉菜单选中某一项时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[OnSelectCallback](#type-onselectcallback)|是|-|选中项的索引和值。<br>初始值：{ _, _ => }。|

## 基础类型定义

### class SelectOption

```cangjie
public class SelectOption {
    public var value: ?ResourceStr
    public var icon: ?ResourceStr
    public init(value!: ?ResourceStr, icon!: ?ResourceStr = None)
}
```

**功能：** 设置下拉菜单组件参数的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var value

```cangjie
public var value: ?ResourceStr
```

**功能：** 下拉选项内容。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var icon

```cangjie
public var icon: ?ResourceStr
```

**功能：** 下拉选项图标。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?ResourceStr, ?ResourceStr)

```cangjie
public init(value!: ?ResourceStr, icon!: ?ResourceStr = None)
```

**功能：** 构造SelectOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 下拉选项内容。初始值：""。|
|icon|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 下拉选项图标。初始值：""。|

### type OnSelectCallback

```cangjie
public type OnSelectCallback = (Int32, String) -> Unit
```

**功能：** 定义选择回调函数类型。

**类型：** (Int32, String) -> Unit

## 示例代码

### 示例1（设置下拉菜单）

该示例通过配置SelectOptions实现下拉菜单。

<!-- run -->

```cangjie

package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.i18n.*
import ohos.resource_manager.*
import ohos.hilog.*
import ohos.arkui.component.common.Offset as CommonOffset
import ohos.resource.__GenerateResource__

@Entry
@Component
class EntryView {
    @State var text: String = "TTTTT"
    @State var index: Int32 = 2
    @State var space: Int64 = 8

    @State var values1: Array<SelectOption> = [
            SelectOption(value: "aaa", icon: @r(app.media.startIcon)),
            SelectOption(value: "bbb", icon: @r(app.media.startIcon)),
            SelectOption(value: "ccc", icon: @r(app.media.startIcon)),
            SelectOption(value: "ddd", icon: @r(app.media.startIcon))]

    @State var arrow: ArrowPosition = ArrowPosition.End

    func build() {
        Column {
            Select(this.values1)
            .selected(1)
            .value(this.text)
            .font(size: 16.vp, weight: FontWeight.W500)
            .fontColor(0x182431)
            .selectedOptionFont(size: 16.vp, weight: FontWeight.W400)
            .space(this.space)
            .arrowPosition(this.arrow)
            .menuAlign(alignType: MenuAlignType.Start, offset: CommonOffset(0, 0))
            .optionWidth(200)
            .optionHeight(300)
            .onSelect({ index: Int32, text: String =>
                Hilog.info(0, "AppLogCj", " ==================  Select ====================: ${index}")
                Hilog.info(0, "AppLogCj", " ==================  text ====================: ${text}")
                this.index = index;
                this.text = text;
            })
        }.width(100.percent)
    }
}
```

![selectExample](./figures/selectExample.gif)