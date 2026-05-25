## interface MapEntryView\<K, V>

```cangjie
public interface MapEntryView<K, V> {
    prop key: K
    mut prop value: ?V
}
```

功能：提供映射中的某个 key 对应的视图。

### prop key

```cangjie
prop key: K
```

功能：返回视图中的 key，如果视图的 key 不在原始映射中，则返回一个该 key 的空视图。

类型：K

### prop value

```cangjie
mut prop value: ?V
```

功能：读取或修改视图对应原始映射的 value。
设置非空的 value 时，如果该视图的 value 不存在，则在该视图对应的原始映射中新增元素。
设置为 `None` 时，则会删除当前 Entry，删除完之后仍然能继续使用该视图。

类型：[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)(V)