## class UITest

```cangjie
public class UITest {}
```

**功能：** [UITest](#class-uitest)类只包含一个静态方法[setup](#static-func-setup)，用于初始化ui_test库。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### static func setup()

```cangjie
public static func setup(): Unit
```

**功能：** 初始化ui_test库。目前[setup](#static-func-setup)必须写在[TestRunner](#class-testrunner)的[onRun](#func-onrun)中。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// unittest_enginge.cj
import ohos.base.*
import kit.TestKit.*
import ohos.test_runner.*

class MyTestRunner <: TestRunner {
    public func onRun() {
        UITest.setup()
    }

    public func onPrepare() {
        AppLog.info("CJTestRunner onPrepare")
    }
}

let _ = TestRunner.registerCreator("MyTestRunner") {MyTestRunner()}
```