## class PointerMatrix

```cangjie
public class PointerMatrix {}
```

**功能：** 用于多指操作，存储每根手指的坐标点及每一步动作的行为的二维数组。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### static func create(IntNative, IntNative)

```cangjie
public static func create(fingers: IntNative, steps: IntNative): PointerMatrix
```

**功能：** 静态方法，构造一个[PointerMatrix](#class-pointermatrix)对象，并返回该对象。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|IntNative|是|-|多指操作中注入的手指数，取值范围：[1,10]。|
|steps|IntNative|是|-|每根手指操作的步骤数，取值范围：[1,1000]。|

**返回值：**

|类型|说明|
|:----|:----|
|[PointerMatrix](#class-pointermatrix)|返回构造的[PointerMatrix](#class-pointermatrix)对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3)
```

### func setPoint(IntNative, IntNative, Point)

```cangjie
public func setPoint(fingers: IntNative, steps: IntNative, point: Point): Unit
```

**功能：** 设置[PointerMatrix](#class-pointermatrix)对象中指定手指和步骤对应动作的坐标点。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|IntNative|是|-|手指的序号。|
|steps|IntNative|是|-|步骤的序号。|
|point|[Point](#class-point)|是|-|该行为的坐标点。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3)
pointerMatrix.setPoint(0, 0, Point(230, 480))
pointerMatrix.setPoint(0, 1, Point(250, 380))
pointerMatrix.setPoint(0, 2, Point(270, 280))
pointerMatrix.setPoint(1, 0, Point(230, 680))
pointerMatrix.setPoint(1, 1, Point(240, 580))
pointerMatrix.setPoint(1, 2, Point(250, 480))
```