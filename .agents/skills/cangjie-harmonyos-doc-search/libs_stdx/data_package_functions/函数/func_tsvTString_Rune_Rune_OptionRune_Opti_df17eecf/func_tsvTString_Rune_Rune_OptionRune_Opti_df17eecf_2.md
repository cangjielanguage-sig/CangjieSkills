public static func deserialize(dm: DataModel): User {
            var data: DataModelStruct = match (dm) {
                case dms: DataModelStruct => dms
                case _ => throw DataModelException("this data is not DataModelStruct")
            }

            let name = String.deserialize(data.get("username"))
            let age = String.deserialize(data.get("age"))
            return User(name, UInt32.parse(age))
        }
    }

    @Test[user in csv("testdata.csv")]
    func testUser(user: User) {
    @Assert(user.name == "Alex Great" || user.name == "Donald Sweet")
    @Assert(user.age == 21 || user.age == 28)
    }
    ```