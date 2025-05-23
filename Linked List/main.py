from program import Node, LinkedList

salom = LinkedList()
example = LinkedList()
salom.head = Node("Dushanba")
tuesday = Node("Seshanba")
wendesday = Node("Chorshanba")
thursday = Node("Payshanba")
friday = Node("Juma")
satuday = Node("Shanba")
sunday = Node("Yakshanba")

salom.head.next = tuesday
salom.head.next.next = wendesday
wendesday.next = thursday
thursday.next = friday
friday.next = satuday
friday.next.next = sunday

kunlar = salom
# 1. Barcha kunlarni chiqarish
print("📅 Haftalik ro'yxat:")
kunlar.allsee()

# 2. Boshi (head)ga yangi kun qo‘shish
print("\n➕ Boshi (head)ga 'Dam olish' qo‘shildi:")
kunlar.add("Dam olish")
kunlar.allsee()

# 3. Oxiriga yangi kun qo‘shish
print("\n📌 Oxiriga 'Haftaning oxiri' qo‘shildi:")
kunlar.append("Haftaning oxiri")
kunlar.allsee()

# 4. Ichidan 'Juma'dan keyin 'Juma oqshomi' qo‘shish
print("\n🎯 'Juma'dan keyin 'Juma oqshomi' qo‘shildi:")
kunlar.insert("Juma", "Juma oqshomi")
kunlar.allsee()

# 5. Tugunni o‘chirish ('Dushanba')
print("\n❌ 'Dushanba' o‘chirildi:")
kunlar.delete("Dushanba")
kunlar.allsee()

# 6. Tugunni yangilash ('Yakshanba' → 'Juma kuni')
print("\n🔄 'Yakshanba' ni 'Juma kuni'ga almashtirish:")
kunlar.update("Yakshanba", "Juma kuni")
kunlar.allsee()

# 7. Pop qilish (oxirgi elementni sug‘urib olish)
print("\n📤 Oxirgi element sug'urib olindi:", kunlar.pop())
kunlar.allsee()

# 8. Ro‘yxat uzunligi
print("\n📏 Ro'yxat uzunligi:", kunlar.length())

# 9. Python listga o‘girish
print("\n📋 Ro'yxatni listga o‘girish:", kunlar.to_list())

# 10. Tozalash
print("\n🧹 Ro'yxat tozalandi:")
kunlar.clear()
print("Bo‘shmi:", kunlar.is_empty())
