## class PointerMatrix

```cangjie
public class PointerMatrix {}
```

**功能：** 存储多指操作中每根手指每一步动作的坐标点及其行为的二维数组。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### static func create(Int32, Int32)

```cangjie
public static func create(fingers: Int32, steps: Int32): PointerMatrix
```

**功能：** 静态方法，构造一个[PointerMatrix](#class-pointermatrix)对象，并返回该对象。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|是|-|多指操作中注入的手指数，取值范围：[1,10]的整数。|
|steps|Int32|是|-|每根手指操作的步骤数，取值范围：[1,1000]的整数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PointerMatrix](#class-pointermatrix)|返回构造的[PointerMatrix](#class-pointermatrix)对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setPoint(Int32, Int32, Point)

```cangjie
public func setPoint(finger: Int32, step: Int32, point: Point): Unit
```

**功能：** 设置[PointerMatrix](#class-pointermatrix)对象中指定手指和步骤对应动作的坐标点。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|finger|Int32|是|-|手指的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的手指数。|
|step|Int32|是|-|步骤的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的操作的步骤数。|
|point|[Point](#class-point)|是|-|该行为的坐标点。建议相邻的坐标点距离在10px至80px范围内。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.ui_test.Point as PT
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3)
    pointerMatrix.setPoint(0, 0, PT(230, 480))
    pointerMatrix.setPoint(0, 1, PT(250, 380))
    pointerMatrix.setPoint(0, 2, PT(270, 280))
    pointerMatrix.setPoint(1, 0, PT(230, 680))
    pointerMatrix.setPoint(1, 1, PT(240, 580))
    pointerMatrix.setPoint(1, 2, PT(250, 480))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```