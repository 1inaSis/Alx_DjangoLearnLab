
---

### ✅ 6. Fill in `delete.md`

```markdown
# DELETE Operation

```python
# Python command:
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
