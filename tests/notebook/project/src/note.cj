package notebook

import stdx.encoding.json.*
import std.collection.*

public class Note {
    public var id: Int64
    public var title: String
    public var content: String
    public var tags: ArrayList<String>

    public init(id: Int64, title: String, content: String, tags: ArrayList<String>) {
        this.id = id
        this.title = title
        this.content = content
        this.tags = tags
    }

    public func toJsonValue(): JsonValue {
        let obj = JsonObject()
        obj.put("id", JsonInt(id))
        obj.put("title", JsonString(title))
        obj.put("content", JsonString(content))
        let arr = JsonArray()
        for (tag in tags) {
            arr.add(JsonString(tag))
        }
        obj.put("tags", arr)
        return obj
    }

    public static func fromJsonValue(jv: JsonValue): Note {
        let obj = jv.asObject()
        let id = obj["id"].asInt().getValue()
        let title = obj["title"].asString().getValue()
        let content = obj["content"].asString().getValue()
        let jsonTags = obj["tags"].asArray()
        let tags = ArrayList<String>()
        for (i in 0..jsonTags.size()) {
            tags.add(jsonTags[i].asString().getValue())
        }
        return Note(id, title, content, tags)
    }
}
