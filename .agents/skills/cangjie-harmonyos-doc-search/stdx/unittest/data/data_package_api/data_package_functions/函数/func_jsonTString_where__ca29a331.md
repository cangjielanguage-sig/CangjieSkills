## func json\<T>(String) where T <: Serializable\<T>

```cangjie
public func json<T>(fileName: String): JsonStrategy<T> where T <: Serializable<T>
```

功能：该函数可从 JSON 文件中读取类型 T 的数据值，其中 T 必须可被序列化。该函数的返回值是参数化测试的一种参数源。

参数：

- fileName: String - JSON 格式的文件地址，可为相对地址。

返回值：

- [JsonStrategy](data_package_classes.md#class-jsonstrategy)\<T> - T 可被序列化，数据值从 JSON 文件中读取。

示例：

```cangjie
@Test[user in json("users.json")]
func test_user_age(user: User): Unit {
    @Expect(user.age, 100)
}
```

json 文件示例：

```json
[
    {
        "age": 100
    },
    {
        "age": 100
    }
]
```

创建一种被用作测试函数参数的类，该类实现接口 [Serializable](../../../serialization/serialization_package_api/serialization_package_interfaces.md#interface-serializable)。

<!--compile-->
```cangjie
import stdx.serialization.serialization.*
import std.convert.*

class User <: Serializable<User> {
    User(let age: Int64) {}

    public func serialize(): DataModel {
        DataModelStruct().add(Field("age", DataModelInt(age)))
    }

    public static func deserialize(dm: DataModel): User {
        if (let Some(dms) <- (dm as DataModelStruct)) {
            if (let Some(age) <- (dms.get("age") as DataModelInt)) {
                return User(age.getValue())
            }
        }

        throw Exception("Can't deserialize user.")
    }
}
```

任何实现 [Serializable](../../../serialization/serialization_package_api/serialization_package_interfaces.md#interface-serializable) 的类型都可以用作参数类型，包括默认值：

```cangjie
@Test[user in json("numbers.json")]
func test(value: Int64)
```

```cangjie
@Test[user in json("names.json")]
func test(name: String)
```