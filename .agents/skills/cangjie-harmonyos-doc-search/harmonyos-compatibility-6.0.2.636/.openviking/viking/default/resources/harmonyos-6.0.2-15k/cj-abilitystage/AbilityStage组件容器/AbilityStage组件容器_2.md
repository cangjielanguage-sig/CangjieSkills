应用被切换到后台时，系统会将在后台的应用保留在缓存中。即使应用处于缓存中，也会影响系统整体性能。当系统资源不足时，系统会通过多种方式从应用中回收内存，必要时会完全停止应用，从而释放内存用于执行关键任务。为了进一步保持系统内存的平衡，避免系统停止用户的应用进程，可以在AbilityStage中的onMemoryLevel()生命周期回调中订阅系统内存的变化情况，释放不必要的资源。

```cangjie
import kit.AbilityKit.{AbilityStage, MemoryLevel}

class MyAbilityStage <: AbilityStage {
    public override func onMemoryLevel(level: MemoryLevel): Unit {
        // 根据系统可用内存的变化情况，释放不必要的内存
    }
}
```