## `@Configure` 宏

功能：`@Configure` 宏为测试类或测试函数提供配置参数。它可以放置在测试类或测试函数上。

语法规则为 `@Configure[parameter1: <value1>,parameter2: <value2>]`
其中 `parameter1` 是仓颉标识符，`value` 是任何有效的仓颉表达式。均大小写敏感。
`value` 可以是常量或在标有 `@Configure` 的声明范围内有效的任何仓颉表达式。
如果多个参数具有不同的类型，则它们可以有相同的名称。如果指定了多个具有相同名称和类型的参数，则使用最新的一个。

目前支持的配置参数有：

- `randomSeed`: 类型为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)， 为所有使用随机生成的函数设置起始随机种子。
- `generationSteps`: 类型为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) ：参数化测试算法中的生成值的最大步数。
- `reductionSteps` ：类型为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64): 参数化测试算法中的缩减值的最大步数。

以下参数一般用于被 `@Bench` 修饰的 Benchmark 测试函数：

- `explicitGC` ：类型为 [ExplicitGcType](../../unittest/unittest_package_api/unittest_package_enums.md#enum-explicitgctype): Benchmark 函数测试期间如何调用 [GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool)。默认值为 [ExplicitGcType](../../unittest/unittest_package_api/unittest_package_enums.md#enum-explicitgctype).Light 。
- `baseline` ：类型为 [String](../../core/core_package_api/core_package_structs.md#struct-string) : 参数值为 Benchmark 函数的名称，作为比较 Benchmark 函数执行结果的基线。该结果值将作为附加列添加到输出中，其中将包含比较结果。
- `batchSize` ：类型为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 或者 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> : 为 Benchmark 函数配置批次大小。默认值是由框架在预热期间计算得到。
- `minBatches` ：类型为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) : 配置 Benchmark 函数测试执行期间将执行多少个批次。默认值为 `10` 。
- `minDuration` ：类型为 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) : 配置重复执行 Benchmark 函数以获得更好结果的时间。默认值为 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).second * 5 。
- `warmup` ：类型为 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 或者 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) : 配置在收集结果之前重复执行 Benchmark 函数的时间或次数。默认值为 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).second 。当值为 0 时，表示没有 warmup ， 此时执行次数按用户输入的 `batchSize` 乘 `minBatches` 计算得到，当 `batchSize` 未指定时将抛出异常。

用户可以在 `@Configure` 宏中指定其他配置参数，这些参数将来可能会用到。
如果测试类使用 `@Configure` 宏指定配置，则该类中的所有测试函数都会继承此配置参数。
如果此类中的测试函数也标有 `@Configure` 宏，则配置参数将从类和函数合并，其中函数级宏优先。