### extend\<T> HashSet\<T> <: Arbitrary\<HashSet\<T>> where T <: Arbitrary\<T>

```cangjie
extend<T> HashSet<T> <: Arbitrary<HashSet<T>> where T <: Arbitrary<T>
```

功能：为 [HashSet](../../collection/collection_package_api/collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T>  实现了 [Arbitrary](#interface-arbitraryt) 接口，且 T 需实现 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[HashSet](../../collection/collection_package_api/collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T>>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<HashSet<T>>
```

功能：获取生成 HashSet\<T> 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<HashSet\<T>> - 生成 HashSet\<T> 类型随机值生成器。

### extend\<K, V> HashMap\<K, V> <: Arbitrary\<HashMap\<K, V>> where K <: Arbitrary\<K>, V <: Arbitrary\<V>

```cangjie
extend<K, V> HashMap<K, V> <: Arbitrary<HashMap<K, V>> where K <: Arbitrary<K>, V <: Arbitrary<V>
```

功能：为 [HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<T>  实现了 [Arbitrary](#interface-arbitraryt) 接口，且 T 需实现 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V>>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<HashMap<K, V>>
```

功能：获取生成 HashMap\<K, V> 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<HashMap\<K, V>> - 生成 HashMap\<K, V> 类型随机值生成器。