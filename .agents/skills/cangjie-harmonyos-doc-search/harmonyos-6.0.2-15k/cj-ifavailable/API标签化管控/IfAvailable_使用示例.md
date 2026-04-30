## `@IfAvailable` 使用示例

### 使用 `IfAvailable` 控制 `APILevel`

前置依赖，提供不同标签的 API：

<!-- compile -pkg0 -->

```cangjie
package ohos.sample

@!APILevel[17]
public func f17() {
    println("level-17")
}

@!APILevel[18]
public func f18() {
    println("level-18")
}

@!APILevel[19]
public func f19() {
    println("level-19")
}
```

假设 `ohos.sample` 为 sdk 提供的包，用户使用 Deveco Studio 仓颉项目工程时可以选择所需的 level 等级：

![image-Create-Project-With-Level](./figures/image-Create-Project-With-Level.png)

使用 `@IfAvailable` 时，`<label>: <value>` 为 `level: xx`，`xx` 为数值字面量。

<!-- compile -pkg0 -->

```cangjie
import ohos.sample.*

func demo() {
    @IfAvaliable(level: 19, { =>
        // 编译期：此作用域允许调用 level 为 19 或 19 以下的 API。即该分支能够使用 f17, f18, f19，调用更高等级接口会编译报错。
        // 运行期：当执行设备支持 level 19，那么执行该分支。
        f17();
        f18();
        f19();
    }, { =>
        // 编译期：此作用域使用工程提供的能力，允许调用 level 为 18 或 18 以下的 API。即该分支能够使用 f17, f18，调用更高等级接口会编译报错（如 f19）。
        // 运行期：当执行设备支持 level 18，那么执行该分支。
        f17();
        f18();
        f19(); // compile error
    })
}
```

### 使用 `IfAvailable` 控制 `syscap`

前置依赖，提供不同标签 `syscap` 的 API：

<!-- compile -pkg1 -->

```cangjie
package ohos.sample

@!APILevel[18, syscap: "SystemCapability.A"]
public func f1() {
    println("SystemCapability.A")
}

@!APILevel[18, syscap: "SystemCapability.B"]
public func f2() {
    println("SystemCapability.B")
}

@!APILevel[18, syscap: "SystemCapability.C"]
public func f3() {
    println("SystemCapability.C")
}

@!APILevel[18, syscap: "SystemCapability.D"]
public func f4() {
    println("SystemCapability.D")
}
```

Deveco Studio 默认读取所有设备支持的 SystemCapability，用于检查作用域中是否允许使用带有标签的 API。

假设 `ohos.sample` 为 sdk，此时设备1的 syscap 为 `["SystemCapability.A", "SystemCapability.B"]`，设备2的 syscap 为 `["SystemCapability.B", "SystemCapability.C"]`

使用 `@IfAvailable` 时，`<label>: <value>` 为 `syscap: "SystemCapability.xx"`，`"SystemCapability.xx"` 为字符串字面量。

<!-- compile -pkg1 -->

```cangjie
import ohos.sample.*

func demo() {
    @IfAvaliable(syscap: "SystemCapability.D", { =>
        // 此作用域最高允许使用 ["SystemCapability.A", "SystemCapability.B", "SystemCapability.C", "SystemCapability.D"]，其中：
        // ["SystemCapability.B", "SystemCapability.D"] 不告警；
        // ["SystemCapability.A", "SystemCapability.C"] 告警；
        // 非 ["SystemCapability.A", "SystemCapability.B", "SystemCapability.C", "SystemCapability.D"] 报错
        f1(); // warning
        f2(); // ok
        f3(); // warning
        f4(); // ok
    }, { =>
        // 此作用域最高允许使用 ["A", "B", "C"]，其中：
        // ["B"] 不告警；
        // ["A", "C"] 告警；
        // 非 ["A", "B", "C"] 报错
        f1(); // warning
        f2(); // ok
        f3(); // warning
        f4(); // error
    })
}
```