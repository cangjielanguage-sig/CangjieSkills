# ohos.component_utils（ComponentUtils）

提供获取组件绘制区域坐标和大小的能力。

## 导入模块

```cangjie
import ohos.component_utils.*
```

## class ComponentUtils

```cangjie
public class ComponentUtils {}
```

**功能：** 提供获取指定组件绘制区域坐标和大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func getRectangleById(String)

```cangjie
public static func getRectangleById(id: String): ComponentInfo
```

**功能：** 根据组件ID获取组件实例对象, 通过组件实例对象将获取的坐标位置和大小同步返回给开发者。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|指定组件id。|

**返回值：**

|类型|说明|
|:----|:----|
|[ComponentInfo](#class-componentinfo)|组件大小、位置、平移缩放旋转及仿射矩阵属性信息。|

**示例：**

```cangjie
import ohos.component_utils.ComponentUtils

let info = ComponentUtils.getRectangleById("ButtonClick")
```