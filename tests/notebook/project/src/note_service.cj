package notebook

import stdx.encoding.json.*
import std.collection.*

public class NoteService {
    private var notes = ArrayList<Note>()
    private var nextId: Int64 = 1

    public init() {}

    public func createNote(title: String, content: String, tags: ArrayList<String>): Note {
        let note = Note(nextId, title, content, tags)
        nextId += 1
        notes.add(note)
        return note
    }

    public func getNote(id: Int64): ?Note {
        for (note in notes) {
            if (note.id == id) {
                return note
            }
        }
        return None
    }

    public func getAllNotes(): ArrayList<Note> {
        return notes
    }

    public func getNotesByTag(tag: String): ArrayList<Note> {
        let result = ArrayList<Note>()
        for (note in notes) {
            for (t in note.tags) {
                if (t == tag) {
                    result.add(note)
                    break
                }
            }
        }
        return result
    }

    public func updateNote(id: Int64, title: String, content: String, tags: ArrayList<String>): ?Note {
        for (i in 0..notes.size) {
            if (notes[i].id == id) {
                notes[i].title = title
                notes[i].content = content
                notes[i].tags = tags
                return notes[i]
            }
        }
        return None
    }

    public func deleteNote(id: Int64): Bool {
        for (i in 0..notes.size) {
            if (notes[i].id == id) {
                notes.remove(i..(i+1))
                return true
            }
        }
        return false
    }

    public func getStats(): JsonValue {
        let obj = JsonObject()
        obj.put("total_notes", JsonInt(notes.size))
        let tagCounts = JsonObject()
        for (note in notes) {
            for (tag in note.tags) {
                if (tagCounts.containsKey(tag)) {
                    let count = tagCounts[tag].asInt().getValue()
                    tagCounts.put(tag, JsonInt(count + 1))
                } else {
                    tagCounts.put(tag, JsonInt(1))
                }
            }
        }
        obj.put("tag_counts", tagCounts)
        return obj
    }
}
