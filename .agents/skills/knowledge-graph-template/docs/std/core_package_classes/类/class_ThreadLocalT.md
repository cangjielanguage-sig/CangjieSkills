## class ThreadLocal\<T>

```cangjie
public class ThreadLocal<T> {}
```

功能：该类表示仓颉线程局部变量。

和普通变量相比，线程局部变量有不同的访问语义。当多个线程共享使用同一线程局部变量时，每个线程都有各自的一份值拷贝。线程对变量的访问会读写线程本地的值，而不会影响其他线程中变量的值。

### func get()

```cangjie
public func get(): ?T
```

功能：获得仓颉线程局部变量的值。

返回值：

- ?T - 如果当前线程局部变量不为空值，返回该值，如果为空值，返回 `None`。

### func set(?T)

```cangjie
public func set(value: ?T): Unit
```

功能：通过 value 设置仓颉线程局部变量的值，如果传入 `None`，该局部变量的值将被删除，在线程后续操作中将无法获取。

参数：

- value: ?T - 需要设置的局部变量的值。