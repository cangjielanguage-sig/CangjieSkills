## func getUsedHeapSize()

```cangjie
public func getUsedHeapSize(): Int64
```

功能：在 Linux 平台下获取仓颉堆实际占用的物理内存大小，单位为 byte。在 Windows 及 macOs 平台下获取仓颉进程实际占用的物理内存大小，单位为 byte。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 仓颉堆或仓颉进程实际占用的物理内存大小，单位为 byte。

## func setGCThreshold(UInt64)

```cangjie
public func setGCThreshold(value: UInt64): Unit
```

功能：修改用户期望触发 [gc](runtime_package_funcs.md#func-gcbool) 的内存阈值，当仓颉堆大小超过该值时，触发 [gc](runtime_package_funcs.md#func-gcbool)，单位为 KB。

参数：

- value: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 用户期望触发 [gc](runtime_package_funcs.md#func-gcbool) 的内存阈值。

示例：
设置用户期望的 [gc](runtime_package_funcs.md#func-gcbool) 的内存阈值为 2MB。

<!-- run -->

```cangjie
import std.runtime.*
main() {
  setGCThreshold(2048)
}
```

## func SetGCThreshold(UInt64) <sup>(deprecated)</sup>

```cangjie
public func SetGCThreshold(value: UInt64): Unit
```

功能：修改用户期望触发 [GC](runtime_package_funcs.md#func-gcbool-deprecated) 的内存阈值，当仓颉堆大小超过该值时，触发 [GC](runtime_package_funcs.md#func-gcbool-deprecated)，单位为 KB。

> **注意：**
>
> 未来版本即将废弃，使用 [setGCThreshold(UInt64)](./runtime_package_funcs.md#func-setgcthresholduint64) 替代。

参数：

- value: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 用户期望触发 [GC](runtime_package_funcs.md#func-gcbool-deprecated) 的内存阈值。

示例：
设置用户期望的 [GC](runtime_package_funcs.md#func-gcbool-deprecated) 的内存阈值为 2MB。

<!-- run -->

```cangjie
import std.runtime.*
main() {
  SetGCThreshold(2048)
}
```

## func startCPUProfiling()

```cangjie
public func startCPUProfiling(): Unit
```

功能：启动 CPU profiler 跟踪。

> **注意：**
>
> [startCPUProfiling](./runtime_package_funcs.md#func-startcpuprofiling) 与 [stopCPUProfiling(Path)](./runtime_package_funcs.md#func-stopcpuprofilingpath) 两个函数必须一一对应。

异常：

- ProfilingInfoException - 若调用了 [startCPUProfiling](./runtime_package_funcs.md#func-startcpuprofiling) 后，没有调用 [stopCPUProfiling(Path)](./runtime_package_funcs.md#func-stopcpuprofilingpath)，而是又调用了 [startCPUProfiling](./runtime_package_funcs.md#func-startcpuprofiling) 则抛出异常。

## func stopCPUProfiling(Path)

```cangjie
public func stopCPUProfiling(path: Path): Unit
```

功能：停止 CPU profiler 跟踪，并将记录写入指定路径的文件。

> **注意：**
>
> [startCPUProfiling](./runtime_package_funcs.md#func-startcpuprofiling) 与 [stopCPUProfiling(Path)](./runtime_package_funcs.md#func-stopcpuprofilingpath) 两个函数必须一一对应。

参数：

- path: [Path](../../fs/fs_package_api/fs_package_structs.md#struct-path) - 生成记录文件的文件路径。

异常：

- ProfilingInfoException - 若没有调用了 [startCPUProfiling](./runtime_package_funcs.md#func-startcpuprofiling)，直接调用 [stopCPUProfiling(Path)](./runtime_package_funcs.md#func-stopcpuprofilingpath) 则抛出异常。