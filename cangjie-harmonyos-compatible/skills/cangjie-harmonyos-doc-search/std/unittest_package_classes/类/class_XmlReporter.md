## class XmlReporter

```cangjie
public class XmlReporter <: Reporter<TestReport, Unit> {
    public XmlReporter(let directory: Path)
}
```

功能：打印单元测试用例结果数据到 Xml 文件上。

父类型：

- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[TestReport](#class-testreport), [Unit](../../core/core_package_api/core_package_intrinsics.md#unit)>

### XmlReporter(Path)

```cangjie
public XmlReporter(let directory: Path)
```

功能：XmlReporter 构造函数。

参数：

- directory: [Path](../../fs/fs_package_api/fs_package_structs.md#struct-path) - 打印文件生成地址。