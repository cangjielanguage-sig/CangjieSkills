## class CsvReporter

```cangjie
public class CsvReporter <: Reporter<BenchReport, Unit> {
    public CsvReporter(let directory: Path)
}
```

功能：打印性能测试用例结果数据到 CSV 文件上。

父类型：

- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[BenchReport](#class-benchreport), [Unit](../../core/core_package_api/core_package_intrinsics.md#unit)>

### CsvReporter(Path)

```cangjie
public CsvReporter(let directory: Path)
```

功能：CsvReporter 构造函数。

参数：

- directory: [Path](../../fs/fs_package_api/fs_package_structs.md#struct-path) - 打印文件生成地址。

## class CsvRawReporter

```cangjie
public class CsvRawReporter <: Reporter<BenchReport, Unit> {
    public CsvRawReporter(let directory: Path)
}
```

功能：打印性能测试用例结果数据，该数据只有批次的原始测量值，到 CSV 文件上。

父类型：

- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[BenchReport](#class-benchreport), [Unit](../../core/core_package_api/core_package_intrinsics.md#unit)>

### CsvRawReporter(Path)

```cangjie
public CsvRawReporter(let directory: Path)
```

功能：CsvRawReporter 构造函数。

参数：

- directory: [Path](../../fs/fs_package_api/fs_package_structs.md#struct-path) - 打印文件生成地址。