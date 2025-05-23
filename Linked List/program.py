class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def allsee(self):
        """Linked Listdagi barcha obyektlar"""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def add(self, data):
        """Headga qo'shish"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Linked Listning eng oxiriga abyekt qo'shish"""
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = Node(data)
            return
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert(self, value, data):
        """LinkedList ichida 'value' qiymatiga ega tugundan keyin 'data' qiymatli yangi tugun qo'shadi."""
        temp = self.head
        while temp:
            if temp.data == value:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"{value} qiymatli tugun topilmadi.")

    def delete(self, target):
        """Linked listdan berilgan qiymatdagi elementni o'chirish"""
        temp = self.head
        prev = None

        if temp is None:
            print("Bo'sh Linked List")
            return

        if temp.data == target:
            self.head = temp.next
            return

        while temp:
            if temp.data == target:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
        print("Bunday element topilmadi")

    def pop(self, target=None):
        """Index berilsa — shu qiymatdagi elementni, aks holda oxirgi elementni sug'urib oladi"""
        if self.head is None:
            print("Bo'sh ro'yxat!")
            return None

        current = self.head
        prev = None

        if target is None:
            if current.next is None:
                data = current.data
                self.head = None
                return data
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            return current.data

        if current.data == target:
            self.head = current.next
            return current.data

        while current and current.data != target:
            prev = current
            current = current.next

        if current is None:
            print("Element topilmadi.")
            return None

        prev.next = current.next
        return current.data

    # def update(self, target, value):
        # temp = self.head
        # prev = None
        # if temp.data == target:
        #     new_node = Node(value)
        #     new_node.next = temp.next
        #     self.head = new_node
        #     return
        # while temp.next:
        #     if target == temp.data:
        #         temp.data = value
        #         prev.next = temp
        #         return
        #     else:
        #         prev = temp
        #         temp = temp.next
        # return print("Bunday qiymat topilmadi")

    def update(self, target, value):
        """Linked Listdagi birinchi uchragan target qiymatni value ga almashtiradi"""
        temp = self.head

        while temp:
            if temp.data == target:
                temp.data = value
                return
            temp = temp.next

        print("Bunday qiymat topilmadi")

    def to_list(self):
        data = []
        temp = self.head
        while temp:
            data.append(temp.data)
            temp = temp.next
        return data

    def length(self):
        """linked List uzunligini qaytartadi"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        """Linked Listni tozalash"""
        self.head = None

    def is_empty(self):
        return self.head is None
